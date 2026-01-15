Act as an expert technical writer and developer relations engineer. Your task is to generate a weekly changelog in Markdown format based on a list of pull requests (PRs) provided in a JSON file.

You will be given a JSON object containing an array of PRs. Each PR object includes a `pr` number, `title`, `description`, and an `ellipsis_summary`.

Your generated changelog must adhere to the following structure and rules:

**Output Format:**

1.  **Date Header:** Start with a Markdown H3 header for the current week's date. For example: `### 2025-07-22`.
2.  **Categories:** Group the PRs into these four exact categories, in this specific order:
    * `### Customer facing features: Now available! 🚀`
    * `### Customer facing features: Not yet released ⌛`
    * `### Bug fixes / maintenance 🔧`
    * `### Internal improvements 🌟`
3.  **List Items:** Under each category, list the changes as bullet points (`*`).
4.  **Summaries:** Each bullet point should contain a concise, human-readable summary of the feature or fix. Use the PR's `title` and `ellipsis_summary` to create a clear and brief description of the change from a user's perspective.
5.  **PR Linking:** At the end of each bullet point, include the corresponding PR number formatted as a Markdown link to the `ubicloud/ubicloud` GitHub repository. For example, a change from PR #3586 should end with `[#3586](https://github.com/ubicloud/ubicloud/pull/3586)`.

**Categorization Rules:**

Your most important task is to correctly categorize each pull request based on its content and impact. Use the following guidelines:

* **Customer facing features: Now available! 🚀**
    * Include features and significant enhancements that are immediately available and usable by end-users. Examples include new user interface functionalities (like multi-phase login), new commands, or newly supported services that are fully released.

* **Customer facing features: Not yet released ⌛**
    * Include work on new features that are still in development, are behind a feature flag, or are foundational pieces for a larger, upcoming feature.
    * **Crucially, all AWS-related features and `VmHost` related changes are not yet customer-facing.** These should be placed in this category if they represent new functionality, or in the other categories below if they are fixes or internal changes.

* **Bug fixes / maintenance 🔧**
    * Include all changes that fix incorrect behavior, bugs, or errors.
    * This category also includes routine maintenance like dependency updates (e.g., bumping Ruby or Alma Linux versions), security patches, and correcting misconfigurations.

* **Internal improvements 🌟**
    * Include changes that improve the codebase or developer experience but have no direct, immediate impact on the end-user.
    * Examples: refactoring code, improving test coverage, enhancing CI/CD pipelines, adding logging, or optimizing performance.

Now, using these instructions, process the following JSON input and generate the weekly changelog.

**[Paste the content of weekly_prs.json here]**