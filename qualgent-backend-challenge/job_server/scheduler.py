def schedule_jobs(jobs):
    grouped_jobs = {}
    
    for job in jobs:
        app_version_id = job['app_version_id']
        if app_version_id not in grouped_jobs:
            grouped_jobs[app_version_id] = []
        grouped_jobs[app_version_id].append(job)

    return grouped_jobs

def assign_jobs_to_agents(grouped_jobs, agents):
    assigned_jobs = {}
    
    for app_version_id, jobs in grouped_jobs.items():
        for job in jobs:
            target = job['target']
            available_agents = [agent for agent in agents if agent['target'] == target and agent['available']]
            
            if available_agents:
                agent = available_agents[0]  # Assign to the first available agent
                if agent['id'] not in assigned_jobs:
                    assigned_jobs[agent['id']] = []
                assigned_jobs[agent['id']].append(job)
                agent['available'] = False  # Mark agent as busy

    return assigned_jobs

def release_agent(agent_id, agents):
    for agent in agents:
        if agent['id'] == agent_id:
            agent['available'] = True
            break

def check_agent_availability(agents):
    return [agent for agent in agents if agent['available']]