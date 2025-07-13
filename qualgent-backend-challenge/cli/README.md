# qgjob CLI Tool

The `qgjob` CLI tool is designed to facilitate the submission and management of test jobs for the AppWright QA automation platform. This document provides usage instructions and examples for utilizing the CLI tool effectively.

## Installation

To install the `qgjob` CLI tool, ensure you have Python installed and then run:

```bash
pip install -r requirements.txt
```

## Usage

### Submit a Test Job

To submit a test job, use the following command:

```bash
qgjob submit --org-id=<org_id> --app-version-id=<app_version_id> --test=<test_path>
```

**Parameters:**
- `--org-id`: The organization ID for which the tests are being submitted.
- `--app-version-id`: The specific application version ID that the tests will target.
- `--test`: The path to the test script that you want to run.

**Example:**

```bash
qgjob submit --org-id=qualgent --app-version-id=xyz123 --test=tests/onboarding.spec.js
```

### Check Job Status

To check the status of a submitted job, use the following command:

```bash
qgjob status --job-id=<job_id>
```

**Parameters:**
- `--job-id`: The unique identifier of the job whose status you want to check.

**Example:**

```bash
qgjob status --job-id=abc456
```

## Additional Information

For more detailed information about the commands and options available, you can run:

```bash
qgjob --help
```

This will display a list of available commands and their descriptions.

## Contributing

If you would like to contribute to the `qgjob` CLI tool, please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.