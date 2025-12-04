"""
Check all links on the GitHub Pages site
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://digital-ai-finance.github.io/Systematic-Literature-Reviews-with-Artificial-Intelligence/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def check_url(url, timeout=10):
    """Check if a URL is accessible"""
    try:
        response = requests.head(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        if response.status_code == 405:  # Method not allowed, try GET
            response = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        return response.status_code, response.status_code < 400
    except requests.exceptions.Timeout:
        return "TIMEOUT", False
    except requests.exceptions.ConnectionError:
        return "CONN_ERR", False
    except Exception as e:
        return str(e)[:20], False

def main():
    print("=" * 70)
    print("LINK CHECKER - SLR with AI GitHub Pages")
    print("=" * 70)

    # Fetch the main page
    print(f"\nFetching: {BASE_URL}")
    try:
        response = requests.get(BASE_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"ERROR: Could not fetch page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Collect all links
    all_links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text(strip=True)[:40]
        all_links.append((href, text))

    # Categorize links
    anchor_links = []
    internal_links = []
    external_links = []

    for href, text in all_links:
        if href.startswith('#'):
            anchor_links.append((href, text))
        elif href.startswith('/') or href.startswith(BASE_URL):
            internal_links.append((href, text))
        elif href.startswith('http'):
            external_links.append((href, text))

    # Check anchor links (verify ID exists)
    print(f"\n{'='*70}")
    print(f"ANCHOR LINKS ({len(anchor_links)})")
    print(f"{'='*70}")

    all_ids = [tag.get('id') for tag in soup.find_all(id=True)]
    anchor_results = []

    for href, text in anchor_links:
        anchor_id = href[1:]  # Remove #
        exists = anchor_id in all_ids
        status = "OK" if exists else "MISSING"
        anchor_results.append((href, text, status))
        icon = "Y" if exists else "X"
        print(f"[{icon}] {href:20} -> {status}")

    # Check internal links
    print(f"\n{'='*70}")
    print(f"INTERNAL LINKS ({len(internal_links)})")
    print(f"{'='*70}")

    internal_results = []
    for href, text in internal_links:
        full_url = urljoin(BASE_URL, href)
        status_code, ok = check_url(full_url)
        internal_results.append((href, text, status_code, ok))
        icon = "Y" if ok else "X"
        print(f"[{icon}] {href[:50]:50} -> {status_code}")
        time.sleep(0.2)

    # Check external links
    print(f"\n{'='*70}")
    print(f"EXTERNAL LINKS ({len(external_links)})")
    print(f"{'='*70}")

    external_results = []
    for href, text in external_links:
        status_code, ok = check_url(href)
        external_results.append((href, text, status_code, ok))
        icon = "Y" if ok else "X"
        domain = urlparse(href).netloc
        print(f"[{icon}] {domain:30} {text[:25]:25} -> {status_code}")
        time.sleep(0.3)

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")

    anchor_ok = sum(1 for _, _, s in anchor_results if s == "OK")
    internal_ok = sum(1 for _, _, _, ok in internal_results if ok)
    external_ok = sum(1 for _, _, _, ok in external_results if ok)

    print(f"Anchor links:   {anchor_ok}/{len(anchor_results)} OK")
    print(f"Internal links: {internal_ok}/{len(internal_results)} OK")
    print(f"External links: {external_ok}/{len(external_results)} OK")

    # List failures
    failures = []
    failures.extend([(h, t, s) for h, t, s in anchor_results if s != "OK"])
    failures.extend([(h, t, s) for h, t, s, ok in internal_results if not ok])
    failures.extend([(h, t, s) for h, t, s, ok in external_results if not ok])

    if failures:
        print(f"\n{'='*70}")
        print(f"FAILED LINKS ({len(failures)})")
        print(f"{'='*70}")
        for href, text, status in failures:
            print(f"  {status:10} {href[:55]}")
            if text:
                print(f"            Text: {text[:50]}")

if __name__ == "__main__":
    main()
