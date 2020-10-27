import requests


def get_hero_iq(heroes):
    hero_iq = {}
    for hero in heroes:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['results'][0]['powerstats']['intelligence']
        hero_iq[hero] = int(data)
        top_hero = sorted(hero_iq.items(), key=lambda x: x[1], reverse=True)[0][0]
    return top_hero


if __name__ == '__main__':
    superheroes = [
        'Hulk',
        'Captain America',
        'Thanos'
    ]

print(get_hero_iq(superheroes))
