# pr_reporter.py
#!/usr/bin/env python3
"""
pr_reporter.py

Fetch all merged PRs for a given GitHub repo within a date range,
and emit them as JSON to an output file.
"""

import os
import sys
import argparse
import datetime
import json
import requests

GITHUB_API = "https://api.github.com"


def parse_args():
    p = argparse.ArgumentParser(
        description="Export merged PRs in a date range to JSON"
    )
    p.add_argument(
        "repo",
        help="GitHub repository in owner/repo format, e.g. ubicloud/ubicloud",
    )
    p.add_argument(
        "start_date",
        help="Start date (inclusive) in YYYY-MM-DD format",
    )
    p.add_argument(
        "end_date",
        help="End date (inclusive) in YYYY-MM-DD format",
    )
    p.add_argument(
        "-o",
        "--output",
        default="prs.json",
        help="Output JSON file (default: prs.json)",
    )
    return p.parse_args()


def iso_to_date(iso_str):
    # e.g. "2025-05-12T14:23:45Z"
    return datetime.datetime.fromisoformat(iso_str.rstrip("Z")).date()


def fetch_merged_prs(owner, repo, start_date, end_date, token):
    """
    Fetch all pull requests merged between start_date and end_date
    (inclusive) by using the Search API.
    """
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    per_page = 100
    page = 1
    collected = []

    date_range = f"{start_date.isoformat()}..{end_date.isoformat()}"
    while True:
        # separate qualifiers by spaces so requests encodes them as '+'
        q = f"repo:{owner}/{repo} type:pr is:merged merged:{date_range}"
        url = f"{GITHUB_API}/search/issues"
        params = {"q": q, "per_page": per_page, "page": page}

        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()

        items = data.get("items", [])
        for pr in items:
            collected.append({
                "number": pr["number"],
                "title": pr["title"],
                "body": pr.get("body") or "",
            })

        if len(items) < per_page:
            break
        page += 1

    return collected


def parse_body(body):
    """
    Split a PR body into:
      - description: everything before the first <!-- ELLIPSIS_HIDDEN --> marker
      - ellipsis_summary: everything between the two <!-- ELLIPSIS_HIDDEN --> markers
    If no markers are present, ellipsis_summary is empty.
    """
    marker = "<!-- ELLIPSIS_HIDDEN -->"
    parts = body.split(marker)

    # No marker at all
    if len(parts) < 2:
        return body.strip(), ""

    # parts[0] is description, parts[1] contains the summary + maybe extra,
    # parts[2:] is anything after closing marker which we ignore.
    description = parts[0].strip()

    # extract summary between first and second marker
    summary = ""
    if len(parts) >= 3:
        summary = parts[1].strip()
    else:
        # unclosed marker — treat everything after it as summary
        summary = parts[1].strip()

    # 1) Remove the standard Ellipsis prefix if present
    #    "----\n\n> [!IMPORTANT]\n> "
    prefix = "----\n\n> [!IMPORTANT]\n> "
    if summary.startswith(prefix):
        summary = summary[len(prefix):]

    # 2) Remove the Ellipsis footer (badge + link + auto‐update text),
    #    which always starts with "<sup>This description was created by"
    footer_marker = "<sup>This description was created by"
    idx = summary.find(footer_marker)
    if idx != -1:
        summary = summary[:idx].rstrip()

    return description, summary


def write_json(prs, out_path):
    """
    Write the list of PRs to a JSON file. Each entry:
      {
        "pr": <number>,
        "title": <title>,
        "description": <text before ellipsis>,
        "ellipsis_summary": <text between markers>
      }
    """
    output = []
    for pr in sorted(prs, key=lambda x: x["number"]):
        desc, summary = parse_body(pr["body"])
        output.append({
            "pr": pr["number"],
            "title": pr["title"],
            "description": desc,
            "ellipsis_summary": summary,
        })

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


def main():
    args = parse_args()

    try:
        start = datetime.date.fromisoformat(args.start_date)
        end = datetime.date.fromisoformat(args.end_date)
    except ValueError:
        print("Error: start_date and end_date must be YYYY-MM-DD", file=sys.stderr)
        sys.exit(1)

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print(
            "Warning: no GITHUB_TOKEN set; unauthenticated rate-limit is 60 requests/hour.",
            file=sys.stderr,
        )

    try:
        owner, repo = args.repo.split("/")
    except ValueError:
        print("Error: repo must be in owner/repo format", file=sys.stderr)
        sys.exit(1)

    prs = fetch_merged_prs(owner, repo, start, end, token)
    if not prs:
        print("No merged PRs found in the given date range.")
        sys.exit(0)

    write_json(prs, args.output)
    print(f"Wrote {len(prs)} PRs (JSON) to {args.output}")


if __name__ == "__main__":
    main()
