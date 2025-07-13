from collections import defaultdict

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