import re
import argparse
import os
from imgurscraper.imgur import ImgurScraper

def prepare_url(client_id, url):
    """
    Checks if the inputted URL is a valid imgur album URL.
    Returns a string of the form: 'album/id' or 'gallery/id'.
    """
    url_regex = re.compile('^(?:https?://)?(?:i\.)?imgur\.com/(.*[^\/])')
    regex_match = re.match(url_regex, url)

    if regex_match == None:
        raise ValueError('Enter a valid imgur URL.')

    imgur_resource = regex_match.group(1)
    if 'gallery' not in imgur_resource and 'a' not in imgur_resource and 'album' not in imgur_resource:
        raise ValueError('Enter the valid URL of an imgur album or gallery album.')

    client = ImgurScraper(client_id)
    request = client.request(imgur_resource)
    if 'gallery' in imgur_resource and request['data']['is_album'] != True:
        raise ValueError('This gallery resource is not an album.')

    return imgur_resource

def get_album_id(client_id, imgur_resource):
    """
    Gets an album ID from the imgur API.
    """
    client = ImgurScraper(client_id)
    request = client.request(imgur_resource)

    album_id = request['data']['id']
    return album_id

def mkdir_album(path, album_id):
    """
    Creates a sub-directory for an album to store images,
    within a specified path (i.e. path/album_id).

    Returns the full path to the directory.
    """
    if not os.path.exists(os.path.expanduser(path)):
        raise ValueError('Incorrect path.')
    if not path.endswith('/'):
        path = {}{}.format(path, '/')

    album_dir = {}{}.format(path, album_id)
    if os.path.exists(album_dir):
        return album_dir
    else:
        os.mkdir(album_dir)
        return album_dir

def scrape(client_id, album_id, album_dir, resource, verbose=False):
    """
    Scrapes images from an imgur album.
    Verbose: indicates the album ID, the number of images in
    the album, and the current download progress.
    """
    client = ImgurScraper(client_id)
    request = client.request(resource)

    images_count = request['data']['images_count']
    if verbose:
        print('Album ID: {0}\nNumber of images: {1}'.format(album_id, images_count))

    image_regex = re.compile('^(?:https?://)?(?:i\.)?imgur\.com/(.*)$')
    for i in range(0, images_count, 1):
        image_url = request['data']['images'][i]['link']
        request_regex = re.match(image_regex, image_url)
        image_id = request_regex.group(1)
        path = '{0}/{1}'.format(album_dir, image_id)
        if os.path.exists(path):
            if verbose:
                print('{0}/{1} already downloaded'.format(i+1, images_count))
        else:
            client.save_image(image_url, path)
            if verbose:
                print('Downloaded {0}/{1}'.format(i+1, images_count))
        if verbose and i+1 == images_count:
            print('Finished downloading the album.')
