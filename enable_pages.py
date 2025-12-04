"""
Enable GitHub Pages via GitHub Actions
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
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Enable GitHub Pages with GitHub Actions as source
url = f"https://api.github.com/repos/{org}/{repo_name}/pages"

# First check if pages already exists
check_response = requests.get(url, headers=headers)
if check_response.status_code == 200:
    print("GitHub Pages already enabled!")
    print(f"URL: {check_response.json().get('html_url', 'N/A')}")
else:
    # Create pages with GitHub Actions source
    data = {
        "build_type": "workflow"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code in [201, 204]:
        print("SUCCESS: GitHub Pages enabled!")
        pages_data = response.json() if response.text else {}
        print(f"URL: {pages_data.get('html_url', 'Pending...')}")
    elif response.status_code == 409:
        print("GitHub Pages already configured")
    else:
        print(f"Status: {response.status_code}")
        print(response.text)

# Trigger the workflow manually
print("\nTriggering deployment workflow...")
workflow_url = f"https://api.github.com/repos/{org}/{repo_name}/actions/workflows/hugo.yaml/dispatches"
workflow_data = {"ref": "main"}
workflow_response = requests.post(workflow_url, headers=headers, json=workflow_data)

if workflow_response.status_code == 204:
    print("SUCCESS: Workflow triggered!")
    print(f"\nSite will be available at:")
    print(f"https://digital-ai-finance.github.io/{repo_name}/")
else:
    print(f"Note: Workflow will run automatically on next push")
    print(f"Status: {workflow_response.status_code}")
