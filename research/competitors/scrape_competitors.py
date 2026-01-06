import requests
from bs4 import BeautifulSoup
import json
import time
import os

def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_ctu(html, url):
    """
    Parses Cable Ties Unlimited
    """
    soup = BeautifulSoup(html, 'html.parser')
    results = {
        "url": url,
        "competitor": "Cable Ties Unlimited",
        "title": soup.title.text.strip() if soup.title else "",
        "b2b_signals": [],
        "categories": [],
        "products": []
    }
    
    # 1. B2B Signals
    if "Distributor" in html or "Wholesale" in html:
        results["b2b_signals"].append("Distributor/Wholesale focus")
    if "Purchase Order" in html: results["b2b_signals"].append("Purchase Order Support")
    if "Tax Exempt" in html: results["b2b_signals"].append("Tax Exempt Support")
    
    # 2. Categories
    cats = soup.select('.category-list a, .nav-item a')
    for cat in cats:
        name = cat.text.strip()
        if name:
            results["categories"].append({"name": name, "url": cat.get("href")})
            
    return results

def parse_ziptie_com(html, url):
    """
    Parses ZipTie.com
    """
    soup = BeautifulSoup(html, 'html.parser')
    results = {
        "url": url,
        "competitor": "ZipTie.com",
        "title": soup.title.text.strip() if soup.title else "",
        "b2b_signals": [],
        "categories": [],
        "products": []
    }
    
    # 1. B2B Signals
    if "Bulk" in html: results["b2b_signals"].append("Bulk Pricing Highlighted")
    if "Custom" in html: results["b2b_signals"].append("Custom Printing Services")
    
    # 2. Categories
    cats = soup.select('nav a, .category-tile a')
    for cat in cats:
        name = cat.text.strip()
        if name:
            results["categories"].append({"name": name, "url": cat.get("href")})
            
    return results

def parse_cable_ties_and_more(html, url):
    """
    Parses Cable Ties & More
    """
    soup = BeautifulSoup(html, 'html.parser')
    results = {
        "url": url,
        "competitor": "Cable Ties & More",
        "title": soup.title.text.strip() if soup.title else "",
        "b2b_signals": [],
        "categories": [],
        "products": []
    }
    
    # 1. B2B Signals
    if "Government" in html: results["b2b_signals"].append("Government/Military Sales")
    if "Schools" in html: results["b2b_signals"].append("Education Sales")
    
    # 2. Categories (Often in sidebar or mega menu)
    cats = soup.select('.side-menu a, .megamenu a')
    for cat in cats:
        name = cat.text.strip()
        if name and len(name) > 3: # Filter out small icons/noise
            results["categories"].append({"name": name, "url": cat.get("href")})
            
    return results

def parse_cable_ties_plus(html, url):
    """
    Parses Cable Ties Plus
    """
    soup = BeautifulSoup(html, 'html.parser')
    results = {
        "url": url,
        "competitor": "Cable Ties Plus",
        "title": soup.title.text.strip() if soup.title else "",
        "b2b_signals": [],
        "categories": [],
        "products": []
    }
    
    # 1. B2B Signals
    if "Nelco" in html: results["b2b_signals"].append("Nelco Products Subsidiary")
    if "Distributor" in html: results["b2b_signals"].append("Distributor Focus")
    
    # 2. Categories
    cats = soup.select('.category-links a, .nav-bar a')
    for cat in cats:
        name = cat.text.strip()
        if name:
            results["categories"].append({"name": name, "url": cat.get("href")})
            
    return results

def parse_general(html, url):
    """
    Fallback parser for other sites
    """
    soup = BeautifulSoup(html, 'html.parser')
    return {
        "url": url,
        "competitor": "Unknown",
        "title": soup.title.text.strip() if soup.title else "N/A",
        "is_b2b": "Wholesale" in html or "Distributor" in html or "Business" in html
    }

def main():
    targets = [
        {"url": "https://www.cabletiesunlimited.com/", "parser": parse_ctu},
        {"url": "https://ziptie.com/", "parser": parse_ziptie_com},
        {"url": "https://www.cabletiesandmore.com/", "parser": parse_cable_ties_and_more},
        # {"url": "https://www.cabletiesplus.com/", "parser": parse_cable_ties_plus} # 403 error previously, might need to skip or try alternate
    ]
    
    # Attempting a known working page for Cable Ties Plus if main page fails, or just re-trying carefully
    # For now, we'll keep it commented out if it failed hard, or try a sub-page if we knew one.
    # Let's try adding it back to see if it was a transient glitch, or if we need to be more stealthy (which we can't really do easily).
    # Actually, let's try a different User-Agent or just skip if it fails again.
    
    output_dir = "research/competitors/general_data"
    os.makedirs(output_dir, exist_ok=True)

    all_results = []
    
    for target in targets:
        url = target["url"]
        parser = target["parser"]
        print(f"Researching {url}...")
        
        html = get_content(url)
        if html:
            data = parser(html, url)
            all_results.append(data)
        else:
            print(f"Skipping {url} due to fetch error.")
        time.sleep(3) # Increase delay to be more polite

    with open(f"{output_dir}/competitor_deep_dive_extended.json", "w") as f:
        json.dump(all_results, f, indent=4)
    
    print(f"Saved extended research to {output_dir}/competitor_deep_dive_extended.json")

if __name__ == "__main__":
    main()
