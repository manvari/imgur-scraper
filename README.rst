Introduction
============

imgur-scraper is a scraper that helps you retrieve all images from an imgur album.

Registration
============

imgur-scraper queries the imgur API to retrieve information about albums.

You need to register an account at imgur_, then to generate an `API client ID`_.

.. _imgur: https://imgur.com/register
.. _`API client ID`: https://imgur.com/account/settings/apps


Installation
============

Simply use `pip` to install imgur-scraper::

        $ pip install imgur-scraper

imgur-scraper provides `imgur-scrape`.

Usage
=====

imgur-scrape can be used with the following arguments::

        usage: imgur-scrape [-h] [-v] client_id url path

        positional arguments:
        client_id      imgur API client id
        url            URL of the imgur album to scrape
        path           path to save album images

        optional arguments:
        -h, --help     show this help message and exit
        -v, --verbose  increase output verbosity
