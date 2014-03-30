import re
import argparse
import os
from imgur import ImgurScraper

"""
Checks if the inputted URL is a valid imgur album URL.
Returns a string of the form: 'album/id' or 'gallery/id'.
"""
def prepare_url(client_id, url):
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

"""
Gets an album ID from the imgur API.
"""
def get_album_id(client_id, imgur_resource):
    client = ImgurScraper(client_id)
    request = client.request(imgur_resource)

    album_id = request['data']['id']
    return album_id

"""
Creates a sub-directory for an album to store images,
within a specified path (i.e. path/album_id).

Returns the full path to the directory.
"""
def mkdir_album(path, album_id):
    if not os.path.exists(os.path.expanduser(path)):
        raise ValueError('Incorrect path.')
    if not path.endswith('/'):
        path = path + '/'

    album_dir = path + album_id
    if os.path.exists(album_dir):
        return album_dir
    else:
        try:
            os.mkdir(album_dir)
            return album_dir
        except:
            exit(1)

"""
Scrapes images from an imgur album.
Verbose: indicates the album ID, the number of images in
the album, and the current download progress.
"""
def scrape(client_id, album_id, resource, verbose=False):
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
        path = '{0}/{1}/{2}'.format(args.path, album_id, image_id)
        if os.path.exists(path):
            if verbose:
                print('{0}/{1} already downloaded'.format(i+1, images_count))
            else:
                pass
        else:
            client.save_image(image_url, path)
            if verbose:
                print('Downloaded {0}/{1}'.format(i+1, images_count))
        if verbose and i+1 == images_count:
            print('Finished downloading the album.')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("client_id", help="imgur API client id")
    parser.add_argument("url", help="URL of the imgur album to scrape")
    parser.add_argument("path", help="path to save album images")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
    args = parser.parse_args()

    imgur_resource = prepare_url(args.client_id, args.url)
    album_id = get_album_id(args.client_id, imgur_resource)
    scrape(args.client_id, album_id, imgur_resource, args.verbose)
