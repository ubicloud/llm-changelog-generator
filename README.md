## Introduction

At Ubicloud, we publish [monthly
changelogs](https://www.ubicloud.com/docs/changelog) that summarize new
features. We recently ran an experiment to use large language models (LLMs) to
generate our changelogs; and we were surprised by the variance in quality
between LLMs. So, we wanted to share our observations.

Also, we thought that our methodology is general enough to be helpful to
others. So, we decided to open source our script and "prompt generating prompt"
for anyone who publishes changelogs.

## LLM Results

We took past changelogs from our website and applied the methodology below to
have LLMs generate our changelogs. We then scored each output.

The following table shows each LLM, a link to the generated output for our May
changelog, and our assigned score (between 0-10).

| LLM Name            | Output                                  | Score     |
| ------------------- | --------------------------------------- | --------: |
| Our website (human) | [Link](2025-05-original.mdx)            | 7 |
| DeepSeek-R1         | n/a                                     | fail (\*) |
| OpenAI 4o           | [Link](openai-4o/2025-05.mdx)           | 2 |
| OpenAI o3           | [Link](openai-o3/2025-05.mdx)           | 3 |
| o4-mini-high        | [Link](openai-o4-mini-high/2025-05.mdx) | 4 |
| Claude Opus 4       | [Link](claude-opus-4/2025-05.mdx)       | 7 |
| Claude Opus 4 (**)  | [Link](claude-opus-4-tweak/2025-05.mdx) | 8 |

For DeepSeek-R1, we tried its native chat interface and it failed saying that
the context window exceeded its 128K token limit. Our input had 28K tokens, so
we didn't investigate further. (*)

For Claude Opus 4, we were surprised how much better it performed than OpenAI's
models. The final output had one mistake, where Claude didn't follow its own
instructions (prompt) properly. We fixed that by removing half of the prompt
that we thought didn't contribute to the final result much. (**)

### How we scored the output

We publish a changelog each month that summarizes our new features. We group
these features by our cloud services, provide a list of features for each
service, and a short description for each feature.

We provided a score based on (a) how many new features each LLM could pick up
(from a JSON file that contained all pull requests for the month), (b) how well
the LLM could describe the feature, (c) how well it grouped the features, and
(d) pull requests it referenced (in that order).

Here's what 4o generated (click on details to expand):

<details>

## Ubicloud Kubernetes

<PrList ids={[2632, 3154, 3254]} />

## AI & GPUs

<PrList ids={[3190, 3236, 3238]} />

## Managed PostgreSQL

<PrList ids={[3202, 3248]} />

## Other Services

<PrList ids={[3170, 3233]} />

</details>

Here's what Claude Opus 4 generated.

<details>

---
title: "May 2025"
---

import { PrList } from "/snippets/pr-list.mdx";

## Managed PostgreSQL

### PostgreSQL Metrics Dashboard

We've introduced a comprehensive metrics dashboard for PostgreSQL databases, providing real-time insights into your database performance. The dashboard includes CPU usage breakdown by mode (user, system, iowait, steal), memory utilization, disk I/O operations, network activity, and transaction statistics.

![PostgreSQL Metrics Dashboard](/changelog/2025-05-postgres-metrics.png)

The metrics system automatically collects data every 15 seconds and stores up to one month of historical data, with up to 480 data points per time series for detailed analysis.

### Firewall Rules with Descriptions

PostgreSQL firewall rules now support custom descriptions, making it easier to manage and understand your database security configuration. You can add meaningful descriptions when creating rules and edit them inline directly from the database overview page.

![PostgreSQL Firewall Rules](/changelog/2025-05-postgres-firewall-rules.png)

### Enhanced Authentication Support

PostgreSQL instances now support both `md5` and `scram-sha-256` authentication methods in `pg_hba.conf`. This change allows users migrating from legacy systems to continue using `md5` authentication without changing passwords, while new users automatically benefit from the more secure `scram-sha-256` encryption.

<PrList ids={[3274, 3290, 3299, 3309, 3333, 3366, 3379, 3343]} />

## GitHub Runners

### Premium Runner Performance Tier

We've launched a new premium runner tier that provides access to higher-performance CPU hosts for demanding CI/CD workloads. Premium runners can be enabled through a simple toggle in your GitHub integration settings and will automatically upgrade your runners when capacity is available.

![Premium Runner Toggle](/changelog/2025-05-premium-runners.png)

The runner interface has been redesigned to be more compact and informative, showing runner family (standard vs premium), runtime status, and VM specifications all in an easy-to-scan format.

### Improved Runner Management

Runner rows now display more relevant information including how long a runner has been waiting for jobs, current job execution time, and VM family details. We've also hidden runners that are being destroyed to reduce confusion in the interface.

<PrList ids={[3255, 3256, 3268, 3273, 3300, 3302, 3303, 3313, 3314]} />

## Ubicloud Kubernetes

### Kubernetes Version Selection

You can now select your preferred Kubernetes version when creating clusters, with support for both v1.32 and v1.33. Kubernetes v1.33 is now the default version for new clusters, ensuring you get the latest features and security updates.

### Worker Node Configuration

Kubernetes cluster creation now allows you to specify the VM size for worker nodes independently, giving you more flexibility in resource allocation and cost optimization. Pricing updates dynamically based on your selected worker node size.

### Performance Improvements

We've significantly improved Kubernetes cluster bootstrap time by parallelizing worker node initialization. Workers now start their bootstrap process after the first control plane node completes, reducing total deployment time substantially.

### Enhanced Service Support

Kubernetes clusters now support sub-subdomains for services (e.g., `app.subdomain.cluster-services.example.com`), enabling more complex application architectures and better integration with tools like Okteto that require multiple service endpoints.

<PrList ids={[3154, 3254, 3264, 3267, 3277, 3311, 3325, 3367]} />

## AI & GPUs

### GPU-Enabled Virtual Machines

We've introduced support for GPU-enabled VMs, currently featuring NVIDIA A100 80GB PCIe cards. GPU VMs are available through both the UI and API when the `gpu_vm` feature flag is enabled for your project. The interface shows only available GPU options for your selected region.

![GPU VM Creation](/changelog/2025-05-gpu-vms.png)

VM details now display GPU information, showing specifications like "2x NVIDIA A100 80GB PCIe" when GPUs are attached.

### AI Playground Enhancements

The AI playground now supports multimodal input, allowing you to upload images and PDFs for processing with compatible models. Each model card includes a direct "Try in Playground" link for easier experimentation.

### New Model Support

Added billing rates for the new Llama-4 Maverick model, expanding our AI model offerings with competitive pricing for both input and output tokens.

<PrList ids={[3365, 3372, 3383, 3354]} />

## Load Balancers

### HTTPS-Only Certificate Provisioning

Load balancers now intelligently provision SSL certificates only when needed. If your health check protocol is not set to HTTPS, certificates won't be automatically created, reducing unnecessary resource usage and setup complexity.

<PrList ids={[3345, 3348]} />

## Platform Improvements

### Enhanced Project Limits

To maintain optimal performance and resource allocation, we've implemented a limit of 10 projects per account. This ensures better resource management while still providing flexibility for most use cases.

### Discount Code System

We've introduced a discount code system that allows customers to apply promotional credits to their accounts. The system automatically creates billing information when needed, streamlining the process for new users.

### Location URL Format Update

API endpoints now accept location identifiers in the more user-friendly UBID format instead of UUIDs, making URLs more readable and consistent across the platform.

<PrList ids={[3243, 3272, 3337]} />

## Developer Experience

### Improved Development Setup

Updated our development documentation to use `mise` for software version management, replacing `asdf` for better reliability and performance. The new setup process includes comprehensive instructions for managing dependencies including PostgreSQL and Node.js.

### Enhanced Error Handling

Improved error messages and handling across the platform, including better parameter validation that prevents SQL injection attempts and provides clearer 400 error responses for malformed requests.

<PrList ids={[3139, 3323]} />

</details>


## Methodology

We wanted to follow a methodology that wasn't specific to Ubicloud. We also
wanted to evaluate different LLMs, without our process necessarily favoring
one. This two criteria removed the possibility of creating/tuning one prompt to
run across all models.

Instead, we did the following:

* We created a short prompt (prompt generating prompt). Here, we provided a json
  file that contains all pull requests for a month and our changelog for the
  month. We then asked each LLM to generate us a prompt that given all pull
  requests for a month, can create a change log for the month.
  
* We then took what each LLM generated as an intermediate prompt. We then fed
  that prompt and the pull requests for the month to the same LLM. We looked at
  the output and did the scoring above.

Here's how you can reproduce our experiment step by step:

```
python3 pr_reporter.py ubicloud/ubicloud 2025-05-01 2025-05-31 -o may-pull-requests.json
```

Then, go to your favorite LLM, copy/paste the prompt in
[prompt_generating_prompt.txt](prompt-generating-prompt.txt), and attach the
files [may-pull-requests.json](may-pull-requests.json) and
[2025-05-original.mdx](2025-05-original.mdx) to your prompt.

```
We generate a change log for our product every month. For this, we use completed
pull requests for the month. We then group pull requests into four categories:
(1) customer facing features: now available, (2) customer facing features: not
yet released, (3) bug fixes and maintenance, and (4) internal improvements. Our
change log then includes (1) customer facing features that are available.

I'm including (a) our pull requests for May in json format to this prompt. In
this prompt, you're going to find (i) each completed pull request that has a pr
number, title, description, and an auto generated ellipsis summary.

We used these pull requests to create the attached markdown-like file (b)
2025-05.mdx. This markdown file groups customer facing features into
our cloud services such as Managed PostgreSQL, GitHub Runners, Ubicloud
Kubernetes, AI & GPUs, Compute, and other major services. For each cloud
service, the mdx file contains a list pf pull requests. These PrList ids
correspond to the pr identifiers in (a)(i) pr number. For example, the Managed
PostgreSQL has an id 3170 in 2025-05.mdx. This 3170 corresponds to the "pr" :
3170 in may-pull-requests.json.

Again, we start with may-pull-requests.json, group each pull request into four
categories, take mostly customer facing improvements, group those pull requests
into our cloud services, and then create a change log in mdx format that we
provide to our customers.

If I wanted to automate this process through an LLM, what type of a prompt
should I generate to feed into the LLM? I'd like the LLM then to take input as
pull-requests.json and produce an mdx file for the month that's our change log.
```

Finally, create a new chat window, copy/paste the prompt generated by your LLM
along with pull requests in json format for a given month.


## Two Observations

When we passed the above "prompt generating prompt", each model generated
"changelog generating prompts" of various detail. You can see each model's
generated prompt and generated changelog in the following folders:
[openai-4o](openai-4o), [openai-o3](openai-o3),
[openai-o4-mini-high](openai-o4-mini-high), [claude-opus-4](claude-opus-4).

First, among these "changelog generating prompts", Claude 4's was the most
detailed one. We were curious and applied Claude's intermediate prompt to o3 and
o4-mini-high. This improved OpenAI's performance for the final changelog by
1/10, but not enough to consider it as an alternative to Claude 4. So, we ran
our experiments for other months only on Claude 4.

For reference, you can see Claude 4's "changelog generating prompt" by expanding
the details below.

<details>

You are a technical writer creating a monthly changelog for Ubicloud's cloud platform. Your task is to analyze pull requests from [MONTH YEAR] and create a customer-facing changelog in MDX format.

## Input
You will receive a JSON file containing pull requests with the following structure:
- pr: pull request number
- title: PR title
- description: detailed description
- ellipsis_summary: auto-generated summary

## Task Overview
1. Categorize each PR into one of four categories:
   - Customer-facing features: now available (include in changelog)
   - Customer-facing features: not yet released (exclude from changelog)
   - Bug fixes and maintenance (exclude from changelog)
   - Internal improvements (exclude from changelog)

2. For customer-facing available features, group them by Ubicloud service:
   - Managed PostgreSQL
   - GitHub Runners
   - Ubicloud Kubernetes
   - AI & GPUs
   - Compute
   - [Other services as needed]

3. Create an MDX changelog with engaging descriptions and proper PR references.

## Categorization Guidelines

### Include as Customer-Facing Features (Available):
- New UI features or improvements mentioned in PR descriptions
- New API endpoints or capabilities
- Performance improvements visible to users
- New configuration options or settings
- Features with screenshots or UI changes
- Billing/pricing changes
- New supported versions or deprecations
- Features explicitly marked as released or available

### Exclude from Changelog:
- Internal refactoring (e.g., "Remove usage of from_ubid", "Speed up prog flow control")
- Test additions or modifications
- CI/CD changes
- Development environment updates
- Bug fixes unless they significantly impact user experience
- Features marked as "preview" or "not yet released" in descriptions
- Security fixes (unless disclosure is intended)
- Code optimization without user-visible impact

## Output Format

Create an MDX file with this structure:

```mdx
---
title: "[Month Year]"
---

import { PrList } from "/snippets/pr-list.mdx";

## [Service Name]

### [Feature Title]

[Engaging description of the feature, its benefits, and how customers can use it. Include links to documentation when relevant.]

![Description](/changelog/[year]-[month]-[feature-image].png)

[Additional features for this service...]

<PrList ids={[comma-separated PR numbers]} />

## [Next Service Name]

[Continue pattern for each service with features...]

```

Writing Guidelines

1. Tone: Professional yet approachable, focusing on customer value

2. Feature Descriptions:
  * Lead with the benefit to the customer
  * Explain what's new or improved
  * Include actionable information (how to use/enable)
  * Add documentation links where applicable

3. Organization:
  * Group related features under clear subheadings
  * Order services by importance/impact
  * Place most significant updates first within each service

4. Technical Details:
  * Translate technical PR titles into user-friendly feature names
  * Focus on outcomes rather than implementation details
  * Include version numbers, deprecation notices, and migration information

Example Transformations

PR Title: "Add inline edit functionality for PostgreSQL firewall rules" → Changelog: "You can now add descriptions to your PostgreSQL firewall rules and edit both the range and description inline for better management."

PR Title: "Enable VM assembly with specific gpu_device" → Changelog: "Ubicloud GPU VMs are now available in Germany as part of our preview program."

PR Title: "Parallelize bootstrapping worker nodes" → Changelog: "We have optimized cluster provisioning for Ubicloud Kubernetes, reducing deployment times to under 5 minutes."

Special Instructions

1. If a feature is marked as "preview" or "beta", include that designation
2. For deprecations, clearly state the deprecation and provide migration guidance
3. Include image references only if the PR description mentions screenshots
4. Generate appropriate image filenames following the pattern: /changelog/[year]-[month]-[feature-name].png
5. Combine related PRs into cohesive feature descriptions rather than listing each PR separately
6. Only include PRs that represent completed, available features

Please analyze the provided pull requests and create a polished changelog following these guidelines.

</details>

Second, when we used Claude 4's prompt above, it consistently made the same
mistake. The Ubicloud changelog follows a structure where we talk about each
cloud service, new features announced within that service, and then provide a
list of pull requests relevant to the service. Our documentation engine Mintlify
than resolves links to those pull requests.

Claude 4's intermediate prompt correctly identified this pattern. Still, Claude
4 generated a changelog that talked about a cloud service, a new feature, and
the pull request associated with the feature. We figured Claude 4's intermediate
output was too long so it couldn't follow its own instructures.

One of our coding principles at Ubicloud is simplicity. So, we cut Claude 4's
intermediate prompt and removed the part on writing guidelines. This helped
Claude 4 fix its mistake. The writing style also changed, but we didn't think
that change made the changelog better or worse.
