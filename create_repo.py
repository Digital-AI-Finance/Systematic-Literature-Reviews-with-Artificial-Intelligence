"""
Create GitHub repository on Digital-AI-Finance organization
"""
import requests
import json
from pathlib import Path

# Load token from user config
config_path = Path.home() / ".claude" / "user-config.json"
with open(config_path) as f:
    config = json.load(f)

token = config["github"]["token"]
org = "Digital-AI-Finance"
repo_name = "Systematic-Literature-Reviews-with-Artificial-Intelligence"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Create repository
url = f"https://api.github.com/orgs/{org}/repos"
data = {
    "name": repo_name,
    "description": "Resources and tools for conducting Systematic Literature Reviews using Artificial Intelligence",
    "private": True,  # Must be private per user rules
    "auto_init": True,
    "has_issues": True,
    "has_projects": True,
    "has_wiki": True
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    repo_data = response.json()
    print(f"SUCCESS: Repository created!")
    print(f"URL: {repo_data['html_url']}")
    print(f"Clone URL: {repo_data['clone_url']}")
    print(f"SSH URL: {repo_data['ssh_url']}")
elif response.status_code == 422:
    print("Repository may already exist. Checking...")
    check_url = f"https://api.github.com/repos/{org}/{repo_name}"
    check_resp = requests.get(check_url, headers=headers)
    if check_resp.status_code == 200:
        repo_data = check_resp.json()
        print(f"Repository already exists: {repo_data['html_url']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.json())
