import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

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


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("BASE_URL")
    response = search_autos(f'{url}/automoveis')
    if response:
        soup = parsing_html(response)
        print(soup)
