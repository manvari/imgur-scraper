from setuptools import setup

with open('README.rst') as file:
        README = file.read()

setup(
    name = 'imgur-scraper',
    packages = ['imgurscraper'],
    scripts = ['bin/imgur-scrape'],
    install_requires = ['requests'],
    version = '0.1.2',
    description = 'An imgur album scraper',
    long_description = README,
    author = 'iceTwy',
    author_email = 'icetwy@icetwy.re',
    license = 'MIT',
    url = 'https://github.com/iceTwy/imgur-scraper',
    keywords = ['imgur', 'album', 'scraper'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet'
    ]
)
