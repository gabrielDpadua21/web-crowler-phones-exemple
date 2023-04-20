import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import re


def search_autos(url):
    try:
       response = requests.get(url)
       if response.status_code == 200:
           return response.text
    except Exception as error:
        print("Erro to search veicule")
        print(error)


def parsing_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as error:
        print("Error to parse html")
        print(error)


def get_links(soup):
    links = []
    cards_sup = soup.find("div", class_="cards")
    cards = cards_sup.find_all("a")
    for card in cards:
        links.append(card["href"])
    return links


def extract_phones(text):
    pattern = "\(?0?([1-9]{2})[ -\.\)]{0,2}?(9?\d{4})[ -\.]?(\d{4})"
    return re.findall(pattern, text)


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("BASE_URL")
    response = search_autos(f'{url}/automoveis')
    if response:
        soup = parsing_html(response)
        links = get_links(soup)
        print(links)
