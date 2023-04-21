import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import re


def search_autos(url) -> str:
    try:
       response = requests.get(url)
       if response.status_code == 200:
           return response.text
    except Exception as error:
        print("Erro to search veicule")
        print(error)


def parsing_html(html) -> str:
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as error:
        print("Error to parse html")
        print(error)


def get_links(soup) -> list:
    links = []
    cards_sup = soup.find("div", class_="cards")
    cards = cards_sup.find_all("a")
    for card in cards:
        links.append(card["href"])
    return links


def extract_phones(text) -> list:
    pattern = r"\(?0?([1-9]{2})[ -\.\)]{0,2}?(9?\d{4})[ -\.]?(\d{4})"
    numbers = re.findall(pattern, text)
    return numbers


def get_phones(soup) -> str:
    try:
        description = soup.find_all("div", class_="sixteen wide column")[2].p.get_text().strip()
        return extract_phones(description)
    except Exception as error:
        print("Error to get phones")
        print(error)


def get_advertisement(URL, link) -> str:
    try:
        response = requests.get(f"{URL}{link}")
        if response.status_code == 200:
            return response.text
        else:
            print("Erro to get advertisement")
    except Exception as error:
        print("Erro to get phones")
        print(error)


def save_phones(phones) -> None:
    if len(phones) > 0:
        print(phones)


def get_infos_soup_adv(soup) -> None:
    phones = []
    adv_phones = get_phones(soup)
    if adv_phones:
        phones.append(adv_phones)
    save_phones(phones)


def validate_adv(text) -> None:
    if text:
        soup_adv = parsing_html(text)
        get_infos_soup_adv(soup_adv)


def request_links(URL, links) -> None:
    for link in links:
        adv = get_advertisement(URL, link)
        validate_adv(adv)


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("BASE_URL")
    response = search_autos(f'{url}/automoveis')
    if response:
        soup = parsing_html(response)
        links = get_links(soup)
        request_links(url, links)
        
