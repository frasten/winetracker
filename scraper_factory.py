from urllib.parse import urlparse
from bs4 import BeautifulSoup

from utilities import parse_italian_price

class AbstractScraper:
    def scrape_price(self, soup: BeautifulSoup) -> float:
        raise Exception("NOT IMPLEMENTED")

    def scrape_name(self, soup: BeautifulSoup) -> str:
        raise Exception("NOT IMPLEMENTED")


class TannicoScraper(AbstractScraper):
    def scrape_price(self, soup: BeautifulSoup) -> float:
        tag = soup.find("span", class_="new-price")
        priceText = tag.text
        return parse_italian_price(priceText)

    def scrape_name(self, soup: BeautifulSoup) -> str:
        tag = soup.find("h1", class_="productPage__title")
        return tag.text


def buid_scraper(url: str) -> AbstractScraper:
    domain = urlparse(url).netloc

    try:
        return {
            "www.tannico.it": TannicoScraper(),
        }[domain]
    except:
        raise Exception(f"Website {domain} not yet supported!")

    

