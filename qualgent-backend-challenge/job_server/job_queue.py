from redis import Redis
from rq import Queue
import subprocess
import json

def process_job(payload_json):
    job_payload = json.loads(payload_json)
    job_id = job_payload["job_id"]
    test_path = job_payload["test_path"]
    target = job_payload["target"]

    # Map your target to an AppWright project name if needed
    project = target  # e.g., "emulator", "device", "browserstack"

    print(f"Processing job: {json.dumps(job_payload)}")

    # Run the AppWright test
    try:
        result = subprocess.run(
            ["npx", "appwright", "test", "--project", project, test_path],
            capture_output=True, text=True, check=True
        )
        print(result.stdout)
        status = "completed"
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        status = "failed"

    return {"status": status, "job_id": job_id}


class JobQueue:
    def __init__(self, redis_url='redis://localhost:6379'):
        self.redis = Redis.from_url(redis_url)
        self.queue = Queue(connection=self.redis)
        self.status_map = {}  # Track job status in memory

    def add_job(self, job):
        job_payload = job.to_dict()
        job_id = job.id
        self.status_map[job_id] = "queued"
        
        # Serialize the job payload to a JSON string
        payload_json = json.dumps(job_payload)
        
        self.queue.enqueue(process_job, payload_json)
        return job_id


    def get_jobs(self):
        return list(self.status_map.keys())

    def get_job_status(self, job_id):
        return self.status_map.get(job_id, None)