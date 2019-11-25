import json
from requesthandler import *
from bs4 import BeautifulSoup
import re

class GitHubCrawler:

    github_url = "https://github.com"
    request_handler = RequestHandler()

    def load_input(self, file_name):
        with open("{0}.json".format(file_name), encoding='utf-8') as json_file:
            input = json.load(json_file)
            return input

    def get_search_results(self, input):
        search_url = self.get_search_url(input)
        proxies = input['proxies']
        search_type = input['type']
        output = []
        soup = self.request_handler.make_request(search_url, proxies)
        for list_item in soup.find_all(class_=re.compile("-list-item")):
            url = "{0}{1}".format(self.github_url, list_item.find("a", attrs={"data-hydro-click":True}).get('href'))
            if(search_type.lower()=="repositories"):
                repo_info = self.get_repo_info(url, proxies)
                output.append({"url": url, "extra": repo_info})
            else:
                output.append({"url": url})
        return output

    def get_search_url(self, input):
        search_keywords = input['keywords']
        search_type = input['type']
        return "{0}/search?utf8=✓&q={1}&type={2}".format(self.github_url, "+".join(search_keywords), search_type)

    def get_repo_info(self, repo_url, proxies):
        soup = self.request_handler.make_request(repo_url, proxies)
        author = self.get_repo_owner(soup)
        language_stats = self.get_repo_language_stats(soup)
        return {"owner": author, "language_stats": language_stats}

    def get_repo_owner(self, soup):
        try:
            return soup.find("a", attrs={"rel": "author"}).get('href')[1:]
        except Exception:
            return ""

    def get_repo_language_stats(self, soup):
        language_stats = {}
        try:
            for lang_span in soup.select(".repository-lang-stats-graph > span"):
                lang_label = lang_span["aria-label"].split(" ")
                language_stats[lang_label[0]] = float(lang_label[1][:-1])
        except Exception:
            pass
        return language_stats

    def download_output(self, output, file_name):
        with open("{0}.json".format(file_name), "w") as write_file:
            json.dump(output, write_file)

