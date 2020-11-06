import requests


class YaUploader:
    def __init__(self, auth_token):
        self.token = auth_token
        self.headers = {"Authorization": f"OAuth {token}"}
        

    def get_upload_url(self, file_name):
        URL="https://cloud-api.yandex.net/v1/disk/resources/upload"
        
        PARAMS = {'path': '/Photos/' + file_name, 'overwrite': True}
        
        upload_url = requests.get(url=URL, params=PARAMS, headers=self.headers)
        if upload_url.status_code == 200:
            return upload_url.json()['href']
        else:
            print('Error!')

    def upload(self, url, file_path):
        print(file_path)
        with open(file_path, 'rb') as f:
            response = requests.put(url, data=f)
            if response.status_code == 201:
                print('file uploaded successfully!')


if __name__ == '__main__':
    
    token = "..."
    
    path = 'Hello world!.txt'
    file = path
    
    uploader = YaUploader(token)

    upload_url = uploader.get_upload_url(file)
    result = uploader.upload(upload_url, path)
    
