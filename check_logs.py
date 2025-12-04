"""
Get GitHub Actions workflow logs
"""
import requests
import json
from pathlib import Path
import zipfile
import io

config_path = Path.home() / ".claude" / "user-config.json"
with open(config_path) as f:
    config = json.load(f)

token = config["github"]["token"]
org = "Digital-AI-Finance"
repo_name = "Systematic-Literature-Reviews-with-Artificial-Intelligence"
run_id = "19910673212"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

# Get jobs for this run
jobs_url = f"https://api.github.com/repos/{org}/{repo_name}/actions/runs/{run_id}/jobs"
jobs_response = requests.get(jobs_url, headers=headers)

if jobs_response.status_code == 200:
    jobs = jobs_response.json().get("jobs", [])
    for job in jobs:
        print(f"Job: {job['name']}")
        print(f"  Status: {job['status']}")
        print(f"  Conclusion: {job.get('conclusion', 'N/A')}")

        # Get steps
        for step in job.get("steps", []):
            status_icon = "Y" if step.get("conclusion") == "success" else "X"
            print(f"  [{status_icon}] {step['name']}: {step.get('conclusion', 'pending')}")
        print()

# Try to get logs
logs_url = f"https://api.github.com/repos/{org}/{repo_name}/actions/runs/{run_id}/logs"
logs_response = requests.get(logs_url, headers=headers, allow_redirects=True)

if logs_response.status_code == 200:
    # Logs come as a zip file
    try:
        z = zipfile.ZipFile(io.BytesIO(logs_response.content))
        for name in z.namelist():
            if "Build with Hugo" in name or "build" in name.lower():
                print(f"\n=== {name} ===")
                content = z.read(name).decode('utf-8')
                # Get last 100 lines
                lines = content.split('\n')[-100:]
                for line in lines:
                    if 'error' in line.lower() or 'ERROR' in line:
                        print(line)
    except Exception as e:
        print(f"Could not parse logs: {e}")
else:
    print(f"Could not get logs: {logs_response.status_code}")
