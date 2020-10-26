import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: "xxxxx"):
        self.token = token

    def upload(self, path: "/Users/evgenym/Downloads/Программируем_на_Python..pdf"):
        self.path = path
        token = "xxxxx"
        HEADERS = {"Authorization": f"OAuth {token}"}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                params={"path": "https://disk.yandex.ru/client/disk"},
                                headers=HEADERS,
                                )
        pprint(response.json())
        # return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('xxxxx')
    result = uploader.upload('/Users/evgenym/Downloads/Программируем_на_Python..pdf')
