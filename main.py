import requests
from dotenv import load_dotenv
import os


def search_autos(url):
    try:
       response = requests.get(url)
       if response.status_code == 200:
           print(response.text)
    except Exception as error:
        print("Erro to search veicule")
        print(error)


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("BASE_URL")
    search_autos(f'{url}/automoveis')
