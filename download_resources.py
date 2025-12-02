"""
Download academic papers and resources for Systematic Literature Reviews with AI
"""
import requests
import os
from pathlib import Path
import time

BASE_DIR = Path(__file__).parent
PAPERS_DIR = BASE_DIR / "papers"
PAPERS_DIR.mkdir(exist_ok=True)

# Headers to mimic browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# List of downloadable PDFs and resources
RESOURCES = [
    # Open access papers
    {
        "name": "otto-SR_manuscript.pdf",
        "url": "https://ottosr.com/manuscript.pdf",
        "description": "Automation of Systematic Reviews with Large Language Models"
    },
    {
        "name": "LLM_systematic_reviews_scoping.pdf",
        "url": "https://www.medrxiv.org/content/10.1101/2024.12.19.24319326v1.full.pdf",
        "description": "Large language models for conducting systematic reviews - scoping review"
    },
    {
        "name": "otto-SR_full_paper.pdf",
        "url": "https://www.medrxiv.org/content/10.1101/2025.06.13.25329541v1.full.pdf",
        "description": "otto-SR full paper from medRxiv"
    },
    # ASReview paper
    {
        "name": "ASReview_paper_info.txt",
        "url": None,
        "description": "ASReview: van de Schoot et al. Nature Machine Intelligence 2021. DOI: 10.1038/s42256-020-00287-7",
        "content": """ASReview: An open source machine learning framework for efficient and transparent systematic reviews

Authors: van de Schoot, R., de Bruin, J., Schram, R. et al.
Journal: Nature Machine Intelligence 3, 125-133 (2021)
DOI: https://doi.org/10.1038/s42256-020-00287-7

GitHub: https://github.com/asreview/asreview
Website: https://asreview.nl/
"""
    },
]

def download_file(url, filename, description):
    """Download a file from URL"""
    filepath = PAPERS_DIR / filename
    if filepath.exists():
        print(f"[SKIP] {filename} already exists")
        return True

    try:
        print(f"[DOWNLOADING] {filename}")
        print(f"  Source: {url}")
        response = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)

        size_kb = len(response.content) / 1024
        print(f"[SUCCESS] Downloaded {filename} ({size_kb:.1f} KB)")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to download {filename}: {e}")
        return False

def write_text_file(filename, content, description):
    """Write a text file with content"""
    filepath = PAPERS_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[CREATED] {filename}")

def main():
    print("=" * 60)
    print("Downloading SLR with AI Resources")
    print("=" * 60)

    successful = 0
    failed = 0

    for resource in RESOURCES:
        if resource.get("url"):
            if download_file(resource["url"], resource["name"], resource["description"]):
                successful += 1
            else:
                failed += 1
        elif resource.get("content"):
            write_text_file(resource["name"], resource["content"], resource["description"])
            successful += 1
        time.sleep(1)  # Be polite to servers

    print("\n" + "=" * 60)
    print(f"Download complete: {successful} successful, {failed} failed")
    print("=" * 60)

if __name__ == "__main__":
    main()
