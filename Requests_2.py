import requests
from pprint import pprint

token = "..."


class YaUploader:
    def __init__(self, token: "..."):
        self.token = token

    def get_url_disk(self, url="https://cloud-api.yandex.net/v1/disk/resources/upload"):
        self.url = url
        HEADERS = {"Authorization": f"OAuth {token}"}
        response = requests.get(url, params={"path": 'https://yadi.sk/d/GdxAH0dkrbmOaA?w=1'}, headers=HEADERS)
        return response.json()['href']

    def upload(self, file_path: "/Users/evgenym/Documents/NETOLOGY-DIPLOM/Hello world!.txt"):
        self.file_path = file_path
        with open('Hello world!.txt', 'rb') as f:
            response = requests.put('https://uploader7j.disk.yandex.net:443/upload-target/20201027T123137.939.utd.dzi57s2nkad8i8f907ms8bsug-k7j.21048142', files={"file": f})
        return response.status_code


if __name__ == '__main__':
    uploader = YaUploader('...')
    result = uploader.upload('/Users/evgenym/Documents/NETOLOGY-DIPLOM/Hello world!.txt')

pprint(YaUploader(token))
