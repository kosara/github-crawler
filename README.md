# Github Crawler

## Project Description

The crawler implements the GitHub search and returns all the links from the search result.

## Getting Started

### Prerequisites

* requests
* beautifulsoup4
* pytest

### Installation
Download repository and if needed add more input data. Currently there is one test_input.JSON for testing purposes.
## Running
### Github Crawl and Extra Information

Type in the command prompt:

``` python main.py input.JSON ```

where input.JSON is the input search terms you want to return the links for.
A file called output.JSON will be automatically downloaded in the same folder with the resulting links.

### Testing
There is a pytest module in the tests folder. Change the current working directory to it and type

``` pytest -q```

for running all tests, or

``` pytest -q test_module.py```

where test_module.py is the specific module you want to test. 
