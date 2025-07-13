from redis import Redis
from rq import Queue, Worker
import json
from models import Job
from collections import defaultdict

class JobQueue:
    def __init__(self, redis_url='redis://localhost:6379'):
        self.redis = Redis.from_url(redis_url)
        self.queue = Queue(connection=self.redis)
        self.status_map = {}  # Track job status in memory

    def add_job(self, job):
        # job: Job instance
        job_payload = job.to_dict()
        job_id = job.id
        self.status_map[job_id] = "queued"
        self.queue.enqueue(self.process_job, job_payload)
        return job_id

    def process_job(self, job_payload):
        job_id = job_payload["job_id"]
        self.status_map[job_id] = "running"
        try:
            print(f"Processing job: {json.dumps(job_payload)}")
            # Simulate job processing
            # ... your processing logic ...
            self.status_map[job_id] = "completed"
            return {"status": "completed", "job_id": job_id}
        except Exception as e:
            self.status_map[job_id] = "failed"
            return {"status": "failed", "job_id": job_id, "error": str(e)}

    def get_jobs(self):
        return list(self.status_map.keys())

    def get_job_status(self, job_id):
        return self.status_map.get(job_id, None)

class JobScheduler:
    def __init__(self):
        # Group jobs by app_version_id
        self.job_groups = defaultdict(list)
        # Simulate available agents per target type
        self.agents = {
            "emulator": ["emu-1", "emu-2"],
            "device": ["dev-1", "dev-2"],
            "browserstack": ["bs-1", "bs-2"]
        }
        self.agent_assignments = {}  # job_id -> agent

    def schedule_job(self, job):
        # Group jobs by app_version_id
        self.job_groups[job.app_version_id].append(job)
        # Assign to an available agent for the target
        agent = self._assign_agent(job.target)
        if agent:
            self.agent_assignments[job.id] = agent
            return agent
        return None

    def _assign_agent(self, target):
        # Pick the first available agent for the target type
        agents = self.agents.get(target, [])
        return agents[0] if agents else None

    def get_jobs_for_app_version(self, app_version_id):
        return self.job_groups.get(app_version_id, [])

    def get_agent_for_job(self, job_id):
        return self.agent_assignments.get(job_id)