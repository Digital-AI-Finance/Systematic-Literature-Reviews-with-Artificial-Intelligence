"""
Make repository public for GitHub Pages
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

# Update repository visibility to public
url = f"https://api.github.com/repos/{org}/{repo_name}"
data = {
    "visibility": "public"
}

response = requests.patch(url, headers=headers, json=data)

if response.status_code == 200:
    repo_data = response.json()
    print(f"SUCCESS: Repository is now {repo_data['visibility'].upper()}")
    print(f"URL: {repo_data['html_url']}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
