import pytest
from githubcrawler import *
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

with open("test_repo.html") as fp:
    test_soup_1 = BeautifulSoup(fp, 'html.parser')
test_soup_2 = BeautifulSoup(html_doc, 'html.parser')

github_crawler = GithubCrawler()

class TestGetRepoInfo:

    def test_get_repo_info(self):
        proxies = ["177.92.79.10:80", "41.139.9.47:8080", "5.189.133.231:80"]
        repo_url = "https://github.com/google-research/football"
        assert github_crawler.get_repo_info(repo_url, proxies) == {"owner": "google-research", "language_stats": {"Python": 98.4, "Shell": 1.1, "Dockerfile": 0.5}}

    def test_get_repo_owner(self):
        assert github_crawler.get_repo_owner(test_soup_1) == "google-research"

    def test_get_repo_owner_no_matches(self):
        assert github_crawler.get_repo_owner(test_soup_2) == ""

    def test_get_repo_language_stats(self):
        assert github_crawler.get_repo_language_stats(test_soup_1) == {"Python": 98.4, "Shell": 1.1, "Dockerfile": 0.5}

    def test_get_repo_language_stats_no_matches(self):
        assert github_crawler.get_repo_language_stats(test_soup_2) == {}