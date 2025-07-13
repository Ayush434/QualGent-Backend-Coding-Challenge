from redis import Redis
from rq import Queue
import json

def process_job(payload_json):
    job_payload = json.loads(payload_json)
    job_id = job_payload["job_id"]
    print(f"Processing job: {json.dumps(job_payload)}")
    return {"status": "completed", "job_id": job_id}


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