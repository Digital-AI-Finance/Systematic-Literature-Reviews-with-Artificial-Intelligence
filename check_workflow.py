"""
Check GitHub Actions workflow status
"""
import requests
import json
from pathlib import Path

config_path = Path.home() / ".claude" / "user-config.json"
with open(config_path) as f:
    config = json.load(f)

token = config["github"]["token"]
org = "Digital-AI-Finance"
repo_name = "Systematic-Literature-Reviews-with-Artificial-Intelligence"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

url = f"https://api.github.com/repos/{org}/{repo_name}/actions/runs?per_page=3"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    runs = response.json().get("workflow_runs", [])
    for run in runs:
        print(f"Workflow: {run['name']}")
        print(f"  Status: {run['status']}")
        print(f"  Conclusion: {run.get('conclusion', 'pending')}")
        print(f"  URL: {run['html_url']}")
        print()
else:
    print(f"Error: {response.status_code}")
