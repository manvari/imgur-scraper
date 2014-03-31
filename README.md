imgur-scraper
=============

An imgur album scraper written in Python.

### Installation

imgur-scraper can either be installed through pip (stable version) or manually (dev or stable version).

Using pip:
```
$ (sudo) pip install imgur-scraper
```

Manually:

* Stable version: download the [latest release version](https://github.com/iceTwy/imgur-scraper/releases/latest)
* Development version: clone this git repository (`$ git clone https://github.com/iceTwy/imgur-scraper.git`)

Then run `$ (sudo) python setup.py install` to install imgur-scraper.

### Requirements

Installation requirements:

* Python 2.6+ or Python 3
* [requests](https://github.com/kennethreitz/requests)

Runtime requirements:

* An [account](https://imgur.com/register) at [imgur](https://imgur.com) with a valid [API client ID](https://imgur.com/account/settings/apps).

### Usage

Use `imgur-scrape` (a script provided by imgur-scraper) to scrape an album from imgur:

```
usage: imgur-scrape [-h] [-v] client_id url path

positional arguments:
  client_id      imgur API client id
  url            URL of the imgur album to scrape
  path           path to save album images

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
```

### License

imgur-scraped is licensed under the MIT license; refer to the LICENSE file.
