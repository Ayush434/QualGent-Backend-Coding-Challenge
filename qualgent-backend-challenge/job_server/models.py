import uuid


class Job:
    def __init__(self, org_id, app_version_id, test_path, priority, target, job_id=None, status="queued"):
        self.id = job_id or str(uuid.uuid4())
        self.org_id = org_id
        self.app_version_id = app_version_id
        self.test_path = test_path
        self.priority = priority
        self.target = target
        self.status = status

    def to_dict(self):
        return {
            "job_id": self.id,
            "org_id": self.org_id,
            "app_version_id": self.app_version_id,
            "test_path": self.test_path,
            "priority": self.priority,
            "target": self.target,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            org_id=data["org_id"],
            app_version_id=data["app_version_id"],
            test_path=data["test_path"],
            priority=data["priority"],
            target=data["target"],
            job_id=data.get("job_id"),
            status=data.get("status", "queued")
        )