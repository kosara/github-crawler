from sys import argv
from githubcrawler import *

def main(args): 
    if len(args) == 3:
        github_crawler = GithubCrawler()
        input = github_crawler.load_input(argv[1])
        output = github_crawler.get_search_results(input)
        github_crawler.download_output(output, argv[2])
    else:
        print("Please provide a JSON input file as the first argument and the name of the file you want to save your output in as second.")

if __name__ == '__main__':
    main(argv)