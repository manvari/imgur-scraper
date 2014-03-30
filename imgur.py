# -*- coding: utf8 -*-

import json
import requests
import shutil

class ImgurScraper(object):
    def __init__(self, client_id):
        """
        Sets the client_id (obtain yours here: https://api.imgur.com/oauth2/addclient),
        the imgur API URL and the default path to save images.
        """
        self.client_id = client_id
        self.api_url = "https://api.imgur.com/3/"

    def request(self, input):
        """
        Sends a request to the API. Only publicly available data is accessible.
        Returns data as JSON.
        """
        headers = {'Authorization': 'Client-ID ' + self.client_id,
                   'Accept': 'application/json'}
        request = requests.get(self.api_url + input, headers=headers)
        request.raise_for_status()
        return request.json()

    def resource(self, resource, id):
        """
        Retrieves a resource from the imgur API.
        Returns data as JSON.
        """
        api_request_path = '{0}/{1}'.format(resource, id)
        return self.request(api_request_path)

    def save_image(self, link, path):
        """
        Downloads an image from imgur.
        """
        request = requests.get(link, stream=True)
        request.raise_for_status()
        with open(path, 'wb') as out_file:
            return shutil.copyfileobj(request.raw, out_file)

