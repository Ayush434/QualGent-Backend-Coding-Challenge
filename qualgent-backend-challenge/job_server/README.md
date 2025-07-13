# Job Server Documentation

## Overview
The job server is a backend service designed to manage and orchestrate test jobs for the AppWright QA automation platform. It receives job submissions, queues them, groups them by application version, and assigns them to available agents for execution.

## Setup Instructions
To set up the job server, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/qualgent-backend-challenge.git
   cd qualgent-backend-challenge/job_server
   ```

2. **Install Dependencies**
   Ensure you have Python and pip installed. Then, install the required packages:
   ```bash
   pip install -r ../requirements.txt
   ```

3. **Run the Server**
   Start the job server using the following command:
   ```bash
   python server.py
   ```

   The server will start listening for incoming requests on the specified port.

## Job Orchestration
The job server handles the following tasks:

- **Receive Job Submissions**: The server accepts job submissions via REST API endpoints.
- **Queue Jobs**: Jobs are added to a queue for processing. The queueing mechanism can be configured to use Redis or another preferred service.
- **Group Jobs**: Jobs are grouped by `app_version_id` to minimize the overhead of reinstalling applications on devices.
- **Assign Jobs**: The server assigns jobs to available agents based on device availability and target type (emulator, device, or BrowserStack).
- **Track Status**: The server tracks the status of each job, allowing users to check the progress and results of their submissions.

## Grouping and Scheduling
Jobs are grouped based on the `app_version_id` to ensure that tests targeting the same version are executed together. This approach reduces the need for multiple installations of the same application on devices, optimizing the testing process.

## End-to-End Test Submission
To submit a test job, use the `qgjob` CLI tool. For example:
```bash
qgjob submit --org-id=qualgent --app-version-id=xyz123 --test=tests/onboarding.spec.js
```
This command will submit a job for the specified test, which will be processed by the job server.

## Additional Information
For more details on the CLI tool, refer to the documentation in the `cli/README.md` file.