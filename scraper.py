import re
import argparse
import os
from imgur_scraper import ImgurScraper

parser = argparse.ArgumentParser()
parser.add_argument("client_id", help="imgur API client id")
parser.add_argument("url", help="URL of the imgur album to scrape")
parser.add_argument("path", help="path to save album images")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

"""
Check if the inputted path exists.
Make sure it ends with a forward slash.
"""
if not os.path.exists(os.path.expanduser(args.path)):
    raise ValueError('Incorrect path.')

if not args.path.endswith('/'):
    args.path = args.path + '/'

"""
Check the validity of the inputted URL.
"""
url_regex = re.compile('^(?:https?://)?(?:i\.)?imgur\.com/(.*[^\/])')
regex_match = re.match(url_regex, args.url)

if regex_match == None:
    raise ValueError('Enter a valid imgur URL.')

imgur_resource = regex_match.group(1)
if 'gallery' not in imgur_resource and 'a' not in imgur_resource and 'album' not in imgur_resource:
    raise ValueError('Enter the valid URL of an imgur album or gallery album.')

client = ImgurScraper(args.client_id)
request = client.request(imgur_resource)
if 'gallery' in imgur_resource and request['data']['is_album'] != True:
    raise ValueError('This gallery resource is not an album.')

"""
Retrieve the album ID and create a sub-directory
of the type: path/album_id.
"""
album_id = request['data']['id']
album_dir = args.path + album_id

if os.path.exists(album_dir):
    pass
else:
    try:
        os.mkdir(album_dir)
    except Exception as e:
        exit('Could not create directory: {0}'.format(e))

"""
Get the number of images in the album.
"""
number_of_images = request['data']['images_count']

"""
Verbose: indicate album ID and images count.
"""
if args.verbose:
    print('Album ID: {0} \nNumber of images: {1}\n'.format(album_id, number_of_images))

"""
Prepare a regex to get the ID and extension of images.
"""
image_regex = re.compile('^(?:https?://)?(?:i\.)?imgur\.com/(.*)$')

"""
Loop through the list of URLs retrieved from the API
to download each image in the album.
Verbose: indicate download progress (image_nr/images_count).
"""
for i in range(0, number_of_images, 1):
    image_url = request['data']['images'][i]['link']
    request_regex = re.match(image_regex, image_url)
    image_name = request_regex.group(1)
    path = '{0}/{1}/{2}'.format(args.path, album_id, image_name)
    if os.path.exists(path):
        if args.verbose:
            print('{0}/{1} already downloaded'.format(i+1, number_of_images))
        else:
            pass
    else:
        client.save_image(image_url, path)
        if args.verbose:
            print('Downloaded {0}/{1}'.format(i+1, number_of_images))
