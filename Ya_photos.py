import requests
import os
from tqdm import tqdm
from pprint import pprint


class YaUploader:
    def __init__(self, auth_token):
        self.token = auth_token
        self.headers = {"Authorization": f"OAuth {token}"}

    def get_upload_url(self, file_name):
        URL = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        PARAMS = {'path': '/Photos/' + file_name, 'overwrite': True}
        upload_url = requests.get(url=URL, params=PARAMS, headers=self.headers)
        if upload_url.status_code == 200:
            return upload_url.json()['href']
        else:
            print('Error!')

    def upload(self, url, file_path):
        with open(file_path, 'rb') as f:
            response = requests.put(url, data=f)
            if response.status_code == 201:
                print('file uploaded successfully!')

    def ya_disk_info(self):
        url_disk = "https://cloud-api.yandex.net/v1/disk/resources"
        PARAMS = {'path': '/Photos/', 'fields': '_embedded.items.name,_embedded.items.size'}
        response = requests.get(url=url_disk, params=PARAMS, headers=self.headers)
        pprint(response.json())


if __name__ == '__main__':
    token = "AgAAAAAz9gVGAAas58LXmOoJAUnZsjQ0wcbhzwM"
    files = os.listdir()
    for file in tqdm(files):
        if '.jpg' in file:
            path = file
            uploader = YaUploader(token)
            upload_url = uploader.get_upload_url(file)
            result = uploader.upload(upload_url, path)
disk_info = uploader.ya_disk_info()
