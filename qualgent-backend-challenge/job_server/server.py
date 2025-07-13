from flask import Flask, request, jsonify
from job_queue import JobQueue
from scheduler import JobScheduler
from models import Job

app = Flask(__name__)
job_queue = JobQueue()
job_scheduler = JobScheduler()

@app.route('/submit', methods=['POST'])
def submit_job():
    data = request.json
    org_id = data.get('org_id')
    app_version_id = data.get('app_version_id')
    test_path = data.get('test_path')
    priority = data.get('priority', 1)
    target = data.get('target')

    job = Job(org_id, app_version_id, test_path, priority, target)
    # Schedule the job (group by app_version_id and assign agent)
    agent = job_scheduler.schedule_job(job)
    job_queue.add_job(job)
    return jsonify({
        "message": "Job submitted successfully",
        "job_id": job.id,
        "assigned_agent": agent
    }), 201

@app.route('/status/<job_id>', methods=['GET'])
def check_status(job_id):
    status = job_queue.get_job_status(job_id)
    if status is None:
        return jsonify({"error": "Job not found"}), 404
    agent = job_scheduler.get_agent_for_job(job_id)
    return jsonify({"job_id": job_id, "status": status, "assigned_agent": agent})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)