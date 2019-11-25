import pytest
from bs4 import BeautifulSoup
from requesthandler import *

url = "https://github.com/google-research/football"
proxies = ["177.92.79.10:80", "41.139.9.47:8080", "5.189.133.231:80"]

request_handler = RequestHandler()

class TestRequestHandler:

    def test_make_request(self):
        assert type(request_handler.make_request(url, proxies)) == BeautifulSoup

    def test_make_request_IndexError(self):
        with pytest.raises(SystemExit):
            request_handler.make_request("", [])

    def test_make_request_ConnectionError(self):
        with pytest.raises(SystemExit):
            request_handler.make_request("https://git/google-research/football", proxies)

    def test_make_request_NotFound(self):
        expected_output_soup = BeautifulSoup("Not Found", 'html.parser')
        assert request_handler.make_request("https://github.com/searchnova+css&type=repositories", proxies) == expected_output_soup