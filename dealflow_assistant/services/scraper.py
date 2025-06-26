import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

TECH_FINGERPRINTS = {
    "HubSpot": ["js.hs-scripts.com", "forms.hsforms.com", "hs-analytics"],
    "Salesforce": ["salesforce.com", "pardot.com"],
    "Marketo": ["mktoweb.com"],
    "Shopify": ["cdn.shopify.com", "Shopify.theme"],
    "WooCommerce": ["/wp-content/plugins/woocommerce"],
    "Magento": ["mage.js", "Magento_"],
    "Google Analytics": ["google-analytics.com", "gtag/js"],
    "Hotjar": ["hotjar.com", "hj.js"],
    "Segment": ["cdn.segment.com"],
    "WordPress": ["/wp-content/", "/wp-includes/"],
    "Wix": ["wix.com", "static.parastorage.com"],
    "Squarespace": ["squarespace.com"],
    "Intercom": ["widget.intercom.io"],
    "Zendesk": ["zendesk.com", "zdassets.com"],
    "Drift": ["js.driftt.com"],
}

def detect_footer_year(soup):
    text = soup.get_text(separator=' ')
    years = re.findall(r"\b(19|20)\d{2}\b", text)
    years = [int(y) for y in years if int(y) <= 2025]
    return max(years) if years else None

def detect_last_blog_post(soup):
    dates = []

    for tag in soup.find_all("time"):
        if tag.has_attr("datetime"):
            date = tag["datetime"]
            if re.match(r"\d{4}-\d{2}-\d{2}", date):
                dates.append(date)

    for link in soup.find_all('a', href=True):
        match = re.search(r'(\d{4})[-/](\d{2})[-/](\d{2})', link['href'])
        if match:
            dates.append("-".join(match.groups()))

    return max(dates) if dates else None

def detect_keywords(text, keywords):
    return [kw for kw in keywords if kw.lower() in text.lower()]

def detect_internal_links(soup, substrings):
    matches = []
    for link in soup.find_all("a", href=True):
        href = link["href"].lower()
        if any(sub in href for sub in substrings):
            matches.append(href)
    return matches

def detect_tech_stack(html):
    tech_stack = []
    html_lower = html.lower()
    for tech, fingerprints in TECH_FINGERPRINTS.items():
        if any(f.lower() in html_lower for f in fingerprints):
            tech_stack.append(tech)
    
    return tech_stack

def scrape_signals(url, driver):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        text = soup.get_text(separator=' ', strip=True)

        growth_keywords = ["careers", "we're hiring", "join our team", "job openings", "now hiring", "open roles"]
        stability_keywords = ["family-owned", "since", "established", "founded in", "legacy", "serving since", "tradition"]
        
        return {
            "url": url,
            "tech_stack": detect_tech_stack(html),
            "neglect_signals": {
                "footer_year": detect_footer_year(soup),
                "last_blog_post": detect_last_blog_post(soup)
            },
            "stability_signals": (
                detect_keywords(text, stability_keywords) +
                detect_internal_links(soup, ["about", "history", "legacy"])
            ),
            "growth_signals": (
                detect_keywords(text, growth_keywords) +
                detect_internal_links(soup, ["careers", "jobs", "join"])
            )
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None