from bs4 import BeautifulSoup
import requests
from scraper_factory import buid_scraper
from datetime import datetime

class ScrapeData:
    url = None
    price = 0.0
    name = None
    timestamp = datetime.now()


def scrape(url: str) -> ScrapeData:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }

    scraper = buid_scraper(url)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price = scraper.scrape_price(soup)
    name = scraper.scrape_name(soup)

    data = ScrapeData()
    data.url = url
    data.price = price
    data.name = name
    data.timestamp = datetime.now()

    return data