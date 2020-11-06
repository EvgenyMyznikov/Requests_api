import requests
import json
from tqdm import tqdm
from pprint import pprint

# https://oauth.vk.com/authorize?client_id=.....&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.52

VK_USER_ID = 41609559
VK_TOKEN = ''


def write_json(data):
    with open('photos.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_largest_foto(foto_sizes):
    if foto_sizes['width'] >= foto_sizes['height']:
        return foto_sizes['width']
    else:
        return foto_sizes['height']


def download_foto(url):
    response = requests.get(url, stream=True)
    file_name = url.split('/')[-1].split('?')[0]
    with open(file_name, 'wb') as file:
        for chunk in response.iter_content(4096):
            file.write(chunk)


def main():
    response = requests.get('https://api.vk.com/method/photos.get', params={
        'access_token': VK_TOKEN,
        'owner_id': VK_USER_ID,
        'album_id': 'wall',
        'photo_sizes': 1,
        'v': 5.52})
    write_json(response.json())

    photos = json.load(open('photos.json'))['response']['items']

    for photo in tqdm(photos):
        sizes = photo['sizes']
        max_size_url = max(sizes, key=get_largest_foto)['src']
        download_foto(max_size_url)


if __name__ == '__main__':
    main()
