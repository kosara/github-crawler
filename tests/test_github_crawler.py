import pytest
from githubcrawler import *

github_crawler = GithubCrawler()
test_input = {
          "keywords": [
            "openstack",
            "nova",
            "css"
          ],
          "proxies": [
            "177.92.79.10:80",
            "41.139.9.47:8080",
            "5.189.133.231:80"
          ],
          "type": "repositories"
        }


class TestGithubCrawler:

    def test_load_input(self):
        input = github_crawler.load_input('test_input.json')
        assert input == test_input

    def test_get_search_url(self):
        assert github_crawler.get_search_url(test_input) == "https://github.com/search?utf8=✓&q=openstack+nova+css&type=repositories"
