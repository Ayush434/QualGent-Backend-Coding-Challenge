# QualGent Backend Challenge

## Overview
The QualGent Backend Challenge is designed to build a CLI tool and a backend service for queuing, grouping, and deploying AppWright tests across various devices, emulators, and BrowserStack. This project aims to streamline the testing process for different app versions while minimizing installation overhead.

## Project Structure
The project consists of the following main components:

- **CLI Tool (`cli/qgjob.py`)**: A command-line interface for submitting test jobs and checking their status.
- **Job Server (`job_server/`)**: A backend service that manages job orchestration, including job queuing, scheduling, and execution.
- **GitHub Actions (`github-actions/`)**: A workflow for integrating the CLI tool into CI/CD pipelines.
- **Tests (`tests/`)**: Example test scripts for AppWright tests.

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/qualgent-backend-challenge.git
   cd qualgent-backend-challenge
   ```

2. **Install Dependencies**
   Ensure you have Python and pip installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Job Server**
   You can start the job server using:
   ```
   python job_server/server.py
   ```

4. **Run the CLI Tool**
   To submit a test job, use:
   ```
   python cli/qgjob.py submit --org-id=qualgent --app-version-id=xyz123 --test=tests/onboarding.spec.js
   ```

## Architecture
The architecture consists of a modular design with clear separation of concerns:
- **CLI Tool**: Handles user interactions and communicates with the backend.
- **Job Server**: Receives and processes job submissions, manages job queues, and schedules jobs based on device availability.
- **Database/Queue**: Utilizes Redis or another queueing mechanism for job management.

## Grouping and Scheduling
Jobs are grouped by `app_version_id` to minimize the need for multiple installations of the same app version. The scheduler assigns jobs to available agents based on device availability and target type (emulator, device, BrowserStack).

## Running End-to-End Test Submission
To run an end-to-end test submission:
1. Start the job server.
2. Use the CLI tool to submit a test job.
3. Check the status of the job using:
   ```
   python cli/qgjob.py status --job-id=abc456
   ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.