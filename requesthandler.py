import random
import requests
import sys
from bs4 import BeautifulSoup

class RequestHandler:

    def make_request(self, url, proxies):
        try:
            response = requests.get(url, proxies={"http": random.choice(proxies)})
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        except IndexError as e:
            print("Your proxies' list is empty.")
            sys.exit(1)
        return BeautifulSoup(response.content, 'html.parser')
