# test_pr_reporter.py
import os
import datetime
import pytest
import pr_reporter
import json

# Helper to create a fake PR dict like the search API returns
def make_pr(number, title, body):
    return {"number": number, "title": title, "body": body}


class DummyResponse:
    def __init__(self, json_data, status=200):
        self._json = json_data
        self.status_code = status

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")


@pytest.fixture(autouse=True)
def fake_token(monkeypatch):
    # Ensure a GITHUB_TOKEN is present
    monkeypatch.setenv("GITHUB_TOKEN", "fake-token")


def test_iso_to_date():
    assert pr_reporter.iso_to_date("2025-06-13T12:00:00Z") == datetime.date(2025, 6, 13)


def test_fetch_merged_prs_single_page(monkeypatch):
    inside = make_pr(1, "Inside", "OK")

    def fake_get(url, headers, params):
        assert "search/issues" in url
        return DummyResponse({"items": [inside]})

    monkeypatch.setattr(pr_reporter.requests, "get", fake_get)

    start = datetime.date(2025, 6, 1)
    end = datetime.date(2025, 6, 30)
    prs = pr_reporter.fetch_merged_prs("u", "r", start, end, "tok")

    assert len(prs) == 1
    assert prs[0]["number"] == 1
    assert prs[0]["title"] == "Inside"
    assert prs[0]["body"] == "OK"


def test_fetch_merged_prs_multiple_pages(monkeypatch):
    items_page1 = [make_pr(i, f"Title {i}", "Body") for i in range(1, 101)]
    items_page2 = [make_pr(101, "Title 101", "Body101")]

    def fake_get(url, headers, params):
        page = params["page"]
        if page == 1:
            return DummyResponse({"items": items_page1})
        elif page == 2:
            return DummyResponse({"items": items_page2})
        else:
            raise AssertionError("Should not request page >2")

    monkeypatch.setattr(pr_reporter.requests, "get", fake_get)

    start = datetime.date(2025, 6, 1)
    end = datetime.date(2025, 6, 30)
    prs = pr_reporter.fetch_merged_prs("o", "r", start, end, "tok")

    assert len(prs) == 101
    assert prs[0]["number"] == 1
    assert prs[-1]["number"] == 101


def test_parse_body_no_marker():
    body = "Just a simple PR body without any markers."
    desc, summary = pr_reporter.parse_body(body)
    assert desc == "Just a simple PR body without any markers."
    assert summary == ""


def test_parse_body_with_ellipsis():
    # Ellipsis summary blocks always come with a standard prefix
    # and a footer; both should be stripped out.
    body = (
        "First line of description.\n\n"
        "Second paragraph.\n\n"
        "<!-- ELLIPSIS_HIDDEN -->\n\n"
        "----\n\n"
        "> [!IMPORTANT]\n"
        "> Summary line one\n"
        "> Summary line two\n\n"
        # footer (URL + badge + auto-update text) that must be removed
        "<sup>This description was created by </sup>"
        "[<img alt=\"Ellipsis\" src=\"https://img.shields.io/badge/Ellipsis-blue?color=175173\">]"
        "(https://www.ellipsis.dev/ubicloud?ref=ubicloud%2Fubicloud&utm_source=github&utm_medium=referral)"
        "<sup> for d6019161b06471ae577f2a9ffa162e1fae3a9861. "
        "You can [customize](https://app.ellipsis.dev/ubicloud/settings/summaries) "
        "this summary. It will automatically update as commits are pushed.</sup>\n\n"
        "<!-- ELLIPSIS_HIDDEN -->\n\n"
        "Trailing text that should be ignored."
    )
    desc, summary = pr_reporter.parse_body(body)

    expected_desc = "First line of description.\n\nSecond paragraph."
    # after stripping prefix & footer, we only keep the actual summary lines
    expected_summary = "Summary line one\n> Summary line two"

    assert desc == expected_desc
    assert summary == expected_summary


def test_write_json(tmp_path):
    # PR #1 has ellipsis-marked summary
    body1 = (
        "Desc1 paragraph.\n\n"
        "More desc.\n\n"
        "<!-- ELLIPSIS_HIDDEN -->\n\n"
        "Sum1 line A\nSum1 line B\n\n"
        "<!-- ELLIPSIS_HIDDEN -->"
    )
    # PR #2 has no summary markers
    body2 = "Just a description with no summary."
    prs = [
        make_pr(2, "T2", body2),
        make_pr(1, "T1", body1),
    ]
    out = tmp_path / "out.json"
    pr_reporter.write_json(prs, str(out))

    data = json.loads(out.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) == 2

    first = data[0]
    assert first["pr"] == 1
    assert first["title"] == "T1"
    assert first["description"] == "Desc1 paragraph.\n\nMore desc."
    assert first["ellipsis_summary"] == "Sum1 line A\nSum1 line B"

    second = data[1]
    assert second["pr"] == 2
    assert second["title"] == "T2"
    assert second["description"] == "Just a description with no summary."
    assert second["ellipsis_summary"] == ""
