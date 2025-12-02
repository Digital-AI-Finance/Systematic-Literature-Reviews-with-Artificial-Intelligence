"""
Download List.js library for sortable tables
"""
import requests
from pathlib import Path

# List.js CDN URL
url = "https://cdnjs.cloudflare.com/ajax/libs/list.js/2.3.1/list.min.js"
output_path = Path(__file__).parent / "static" / "js" / "list.min.js"

print(f"Downloading List.js from {url}")
response = requests.get(url)

if response.status_code == 200:
    output_path.write_bytes(response.content)
    print(f"SUCCESS: Saved to {output_path}")
    print(f"Size: {len(response.content) / 1024:.1f} KB")
else:
    print(f"Error: {response.status_code}")
