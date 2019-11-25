from sys import argv
from githubcrawler import *

def main(args): 
    if len(args) == 2:
        github_crawler = GithubCrawler()
        input = github_crawler.load_input(argv[1])
        output = github_crawler.get_search_results(input)
        github_crawler.download_output(output)
    else:
        print("Please provide a JSON input file as an argument.")

if __name__ == '__main__':
    main(argv)