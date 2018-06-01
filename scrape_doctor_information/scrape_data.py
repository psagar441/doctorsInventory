import json
import os

import requests
from bs4 import BeautifulSoup
from .constants import FileConstants


class FetchData:
    def __init__(self, url):
        self.base_url = url
        self.city = FileConstants.CITY_TO_FETCH

    def fetch_city_data(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        url = self.base_url + self.city
        page = requests.get(url, headers=headers)
        tree = BeautifulSoup(page.content, 'html.parser')

        available_states = []
        city_data = {}
        for item in tree.findAll('li', {'class': 'index-item'}):
            a = item.findChildren()
            available_states.append(a[0]['href'])
            print(a[0]['href'])
        city_data.update({'names': available_states})
        with open(FileConstants.STATE_LIST_JSON_FILE, 'w') as f:
            json.dumps(city_data, f)


if __name__ == '__main__':
    website_name = FileConstants.BASE_URL
    get_data = FetchData(website_name)

    if os.path.exists(FileConstants.STATE_LIST_JSON_FILE):
        print('File is there...!!')
    else:
        get_data.fetch_city_data()
