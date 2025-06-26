from fastapi import FastAPI
from typing import List
from .services.scraper import scrape_signals
from .services.gemini_llm import get_deal_memo, get_outreach_email, get_fit_score
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from .schemas import ScrapeRequest, ScrapeResult, GenerateSingleRequest

app = FastAPI()

@app.post("/scrape", response_model=List[ScrapeResult])
def scrape(request: ScrapeRequest):
    options = Options()
    
    options.add_argument("--headless")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/chromium"

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(options=options)
    
    results = []
    for url in request.urls:
        result = scrape_signals(url, driver)
        if not result.get("error"):
            result["fit_score"] = get_fit_score(result)
            result["deal_memo"] = get_deal_memo(result)
        results.append(result)
        
    driver.quit()
    return results

@app.post("/generate-outreach-email", response_model=dict)
def generate_outreach_email(request: GenerateSingleRequest):
    return {
        "outreach_email": get_outreach_email(request.data.dict())
    }

