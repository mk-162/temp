import requests
from bs4 import BeautifulSoup
import json
import time
import os

def get_uline_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_product_group(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    results = {
        "url": url,
        "title": soup.title.text.strip() if soup.title else "",
        "subcategories": [],
        "products": [],
        "b2b_signals": []
    }
    
    # 1. Extract B2B signals
    if "In Stock" in html: results["b2b_signals"].append("In Stock visibility")
    if "Same Day Shipping" in html: results["b2b_signals"].append("Same Day Shipping")
    if "Quick Order" in html: results["b2b_signals"].append("Quick Order Feature")
    if "Request a Catalog" in html: results["b2b_signals"].append("Physical Catalog support")

    # 2. Look for Subcategories/Guided Nav
    nav_links = soup.select('a[id*="SubCatLink"], .GuidedNav a')
    for link in nav_links:
        name = link.text.strip()
        href = link.get("href")
        if name and href:
            results["subcategories"].append({
                "name": name,
                "url": "https://www.uline.com" + href if href.startswith("/") else href
            })

    # 3. Look for Product Tables (Pricing and SKUs)
    rows = soup.select('tr[class*="Row"]')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            sku = cols[0].text.strip()
            if len(sku) >= 3:
                desc = cols[1].text.strip()
                price = cols[-1].text.strip()
                results["products"].append({
                    "sku": sku,
                    "description": desc,
                    "price": price
                })
                
    return results

def main():
    urls = [
        "https://www.uline.com/Grp_56/Cable-Ties",
        "https://www.uline.com/Grp_233/Nylon-Cable-Ties",
        "https://www.uline.com/Grp_357/Heavy-Duty-Cable-Ties",
        "https://www.uline.com/Grp_615/Stainless-Steel-Cable-Ties"
    ]
    
    all_data = []
    output_dir = "research/competitors/uline/data"
    os.makedirs(output_dir, exist_ok=True)

    for url in urls:
        print(f"Scraping {url}...")
        html = get_uline_content(url)
        if html:
            data = parse_product_group(html, url)
            all_data.append(data)
            time.sleep(1)
            
    with open(f"{output_dir}/product_research.json", "w") as f:
        json.dump(all_data, f, indent=4)
    
    print(f"Saved research data to {output_dir}/product_research.json")

if __name__ == "__main__":
    main()
