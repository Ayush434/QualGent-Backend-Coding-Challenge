# QualGent Backend Coding Challenge

## Overview

This project is a simple job scheduling backend with:
- A Flask API for job submission and status checking
- Redis + RQ for job queueing and processing
- A CLI tool for submitting and tracking jobs
- GitHub Actions workflow for CI/CD testing

---

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd QualGent-Backend-Coding-Challenge
   ```

2. **Install Python dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   *(If you don’t have a `requirements.txt`, install manually: `pip install flask requests redis==3.5.3 rq`)*

3. **Start Redis**
   - **Locally:**  
     ```sh
     redis-server
     ```
   - **Or with Docker:**  
     ```sh
     docker run -p 6379:6379 redis
     ```

4. **Start the backend server**
   ```sh
   python qualgent-backend-challenge/job_server/server.py
   ```

5. **(Optional) Start an RQ worker**
   ```sh
   rq worker
   ```

---

## Architecture Diagram

```
+-------------------+         +-------------------+         +-------------------+
|    CLI / API      | <-----> |    Flask Server   | <-----> |    Redis + RQ     |
| (qgjob.py, curl)  |         | (server.py)       |         | (job queue/worker)|
+-------------------+         +-------------------+         +-------------------+
         |                           |                                 |
         |---------------------------|---------------------------------|
                                 |
                        +-------------------+
                        |   JobScheduler    |
                        |   (scheduler.py)  |
                        +-------------------+
```

---

## How Grouping/Scheduling Works

- When a job is submitted, it is grouped by `app_version_id` in the `JobScheduler`.
- Jobs with the same `app_version_id` are batched together for efficient scheduling.
- Each job is assigned to an available agent based on its `target` (e.g., emulator, device, browserstack).
- The job is then enqueued for processing by an RQ worker.

---

## How to Run an End-to-End Test Submission

1. **Start Redis and the backend server** (see Setup above).

2. **Submit a job using the CLI:**
   ```sh
   python qualgent-backend-challenge/cli/qgjob.py submit \
     --org-id=qualgent \
     --app-version-id=xyz123 \
     --test=tests/onboarding.spec.js \
     --target=emulator
   ```

3. **Check job status:**
   ```sh
   python qualgent-backend-challenge/cli/qgjob.py status --job-id=<JOB_ID>
   ```

4. **(Optional) Run the GitHub Actions workflow**
   - Push your code to GitHub.
   - Go to the Actions tab to see the workflow run an end-to-end test.

---

## Notes

- Make sure Redis is running before starting the backend.
- The CLI tool requires the backend server to be running on `localhost:5000`.
- The GitHub Actions workflow will automatically test the full flow on every push.

---
