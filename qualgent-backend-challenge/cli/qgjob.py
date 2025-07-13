import argparse
import requests
import sys

API_URL = "http://localhost:5000"  # Change if your server runs elsewhere

def submit_job(args):
    payload = {
        "org_id": args.org_id,
        "app_version_id": args.app_version_id,
        "test_path": args.test,
        "priority": args.priority,
        "target": args.target
    }
    resp = requests.post(f"{API_URL}/submit", json=payload)
    if resp.status_code == 201:
        data = resp.json()
        print(f"Job submitted! Job ID: {data['job_id']}, Assigned Agent: {data['assigned_agent']}")
    else:
        print("Failed to submit job:", resp.text)
        sys.exit(1)

def check_status(args):
    resp = requests.get(f"{API_URL}/status/{args.job_id}")
    if resp.status_code == 200:
        data = resp.json()
        print(f"Job {data['job_id']} status: {data['status']}, Assigned Agent: {data['assigned_agent']}")
    else:
        print("Failed to get status:", resp.text)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog="qgjob", description="QualGent Job CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Submit command
    submit_parser = subparsers.add_parser("submit", help="Submit a test job")
    submit_parser.add_argument("--org-id", required=True)
    submit_parser.add_argument("--app-version-id", required=True)
    submit_parser.add_argument("--test", required=True, help="Test file path")
    submit_parser.add_argument("--priority", type=int, default=1)
    submit_parser.add_argument("--target", required=True, choices=["emulator", "device", "browserstack"])
    submit_parser.set_defaults(func=submit_job)

    # Status command
    status_parser = subparsers.add_parser("status", help="Check job status")
    status_parser.add_argument("--job-id", required=True)
    status_parser.set_defaults(func=check_status)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()