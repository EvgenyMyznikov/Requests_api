from urllib.parse import urljoin
import requests

TOKEN = '38c4452d974e17aecca5f09b6fed67c7b4eb4adc5839a6608003dbd1b412aa6f1e486f698ced2c6bbabc2'
API_BASE_URL = 'https://api.vk.com/method/'
V = '5.124'


class VKApiClient:

    def __init__(self, user_id, token=TOKEN, version=V):
        self.token = token
        self.version = version
        self.user_id = user_id
        self.user_link = 'http://www.vk.com/id' + str(self.user_id)

    def __and__(self, other):
        response = self.get_mutual_friends(other.user_id)
        return response

    def __str__(self):
        return f'{self.user_link}'

    def get_mutual_friends(self, target_id):
        mutual_url = urljoin(API_BASE_URL, 'friends.getMutual')
        response = requests.get(mutual_url, params={
            'access_token': self.token,
            'v': self.version,
            'source_uid': self.user_id,
            'target_uid': target_id
        })
        friends_list = []
        for elem in response.json()['response']:
            friend = VKApiClient(elem)
            friends_list.append(friend)
        return friends_list


if __name__ == '__main__':
    user1 = VKApiClient(41609559)
    user2 = VKApiClient(40831845)
    print(user1)
    print(user2)

    mutual_friends_list = user1 & user2
    count = 0
    print(f'Number of mutual friends - {len(mutual_friends_list)}:')
    for friend in mutual_friends_list:
        count += 1
        print(count, end='. ')
        print(friend)
