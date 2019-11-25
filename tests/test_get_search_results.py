import pytest
from githubcrawler import *

github_crawler = GitHubCrawler()

class TestGetSearchResults:
  
    def test_get_search_results_repositories(self):
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
        test_output = [
            {
            "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage",
            "extra": {
                "owner": "atuldjadhav",
                "language_stats": {"CSS": 52.0, "JavaScript": 47.2, "HTML": 0.8}}},
            {"url": "https://github.com/michealbalogun/Horizon-dashboard",
            "extra": {
                "owner": "michealbalogun",
                "language_stats": {"Python": 100.0}}
            }
        ]
        assert github_crawler.get_search_results(test_input) == test_output

    def test_get_search_results_issues(self):
        test_input_issues = {
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
          "type": "issues"
        }
        test_output_issues = [
          {"url": "https://github.com/rclone/rclone/issues/2713"},
          {"url": "https://github.com/altai/nova-billing/issues/1"},
          {"url": "https://github.com/novnc/websockify/issues/180"},
          {"url": "https://github.com/sfPPP/openstack-note/issues/8"},
          {"url": "https://github.com/hellowj/blog/issues/37"},
          {"url": "https://github.com/moby/moby/issues/19758"},
          {"url": "https://github.com/YumaInaura/YumaInaura/issues/1322"},
          {"url": "https://github.com/bblfsh/python-driver/issues/202"},
          {"url": "https://github.com/jupyterhub/the-littlest-jupyterhub/issues/108"},
          {"url": "https://github.com/aaronkurtz/gourmand/pull/35"}]
        assert github_crawler.get_search_results(test_input_issues) == test_output_issues

    def test_get_search_results_wikis(self):
        test_input_wikis = {
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
            "type": "wikis"
        }
        test_output_wikis = [
            {"url": "https://github.com/vault-team/vault-website/wiki/Quick-installation-guide"},
            {"url": "https://github.com/iwazirijr/wiki_learn/wiki/Packstack"},
            {"url": "https://github.com/marcosaletta/Juno-CentOS7-Guide/wiki/2.-Controller-and-Network-Node-Installation"},
            {"url": "https://github.com/MirantisDellCrowbar/crowbar/wiki/Release-notes"},
            {"url": "https://github.com/dellcloudedge/crowbar/wiki/Release-notes"},
            {"url": "https://github.com/eryeru12/crowbar/wiki/Release-notes"},
            {"url": "https://github.com/rhafer/crowbar/wiki/Release-notes"},
            {"url": "https://github.com/jamestyj/crowbar/wiki/Release-notes"},
            {"url": "https://github.com/vinayakponangi/crowbar/wiki/Release-notes"},
            {"url": "https://github.com/kingzone/node/wiki/Modules"}]
        assert github_crawler.get_search_results(test_input_wikis) == test_output_wikis

    def test_get_search_results_unicode(self):
        test_input_unicode = {
            "keywords": [
              "chloé",
              "python"
            ],
            "proxies": [
              "177.92.79.10:80",
              "41.139.9.47:8080",
              "5.189.133.231:80"
            ],
            "type": "repositories"
        }
        test_output_unicode = [
            {"url": "https://github.com/tansaku/twss",
            "extra": 
            {"owner": "tansaku",
            "language_stats": {"Python": 100.0}}},
            {"url": "https://github.com/jimchim/Diary-Exchange",
            "extra": {"owner": "jimchim",
            "language_stats": {"JavaScript": 70.5, "CSS": 25.1, "Python": 4.4}}}
        ]
        assert github_crawler.get_search_results(test_input_unicode) == test_output_unicode

    def test_get_search_results_unicode_diff(self):
        test_input_no_unicode = {
          "keywords": [
            "chloe",
            "python"
          ],
          "proxies": [
            "177.92.79.10:80",
            "41.139.9.47:8080",
            "5.189.133.231:80"
          ],
          "type": "repositories"
        }
        test_input_unicode = {
          "keywords": [
            "chloé",
            "python"
          ],
          "proxies": [
            "177.92.79.10:80",
            "41.139.9.47:8080",
            "5.189.133.231:80"
          ],
          "type": "repositories"
        }
        test_ouput_no_unicode = github_crawler.get_search_results(test_input_no_unicode)
        test_output_unicode = github_crawler.get_search_results(test_input_unicode)
        assert test_ouput_no_unicode != test_output_unicode