# Github Crawler

## Project Description

The crawler implements the GitHub search and returns all the links from the search result.

The input is a JSON object, containing:

* search keywords
* list of proxies
* type

Example:
```
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Repositories"
}
```

The output is a JSON object, containing:

* list of links
* author and language statistics for repositories

Example:
```
[
  {
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage",
    "extra": {
      "owner": "atuldjadhav",
      "language_stats": {
        "CSS": 52,
        "JavaScript": 47.2,
        "HTML": 0.8
      }
    }
  }
 ]
  ```
  
## Getting Started

### Prerequisites

* Python 3
* requests
* beautifulsoup4
* pytest

### Installation
Download repository and if needed add more input data.
Currently there is one test file ```test_input.JSON``` for testing purposes.

## Running
### Github Crawl and Extra Information

Type in the command prompt:

``` python main.py [x.JSON] [y]```

where ```x.JSON``` is the input search terms you want to return the links for,
and ```y``` is the name of the JSON file you want the resulting links to be saved in.

### Testing
There is a pytest module in the tests folder.
Change the current working directory to it and type:

``` pytest -q```

for running all tests, or

``` pytest -q test_module.py```

where test_module.py is the specific module you want to test. 
