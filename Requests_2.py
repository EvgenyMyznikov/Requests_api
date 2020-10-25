import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: "AgAAAAAz9gVGAAarDl-c_IdTxEw-lZm2WMQeVz8"):
        self.token = token

    def upload(self, path: "/Users/evgenym/Downloads/Программируем_на_Python..pdf"):
        self.path = path
        token = "AgAAAAAz9gVGAAarDl-c_IdTxEw-lZm2WMQeVz8"
        HEADERS = {"Authorization": f"OAuth {token}"}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                params={"path": "https://disk.yandex.ru/client/disk"},
                                headers=HEADERS,
                                )
        pprint(response.json())
        # return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('AgAAAAAz9gVGAAarDl-c_IdTxEw-lZm2WMQeVz8')
    result = uploader.upload('/Users/evgenym/Downloads/Программируем_на_Python..pdf')
