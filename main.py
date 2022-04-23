from dotenv import load_dotenv
import argparse
import os
import requests
import json
from urllib.parse import urlparse


def shorten_link(url, headers):
    payloads = {
        'long_url': url,
        "domain": "bit.ly",
    }

    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=payloads
    )

    response.raise_for_status()

    return response.json()['link']


def count_clicks(url, headers):
    link = urlparse(url).netloc + urlparse(url).path

    params = {"units": -1}

    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary',
        headers=headers,
        params=params
        )

    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(url, headers):
    link = urlparse(url).netloc + urlparse(url).path

    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{link}',
        headers=headers
        )

    return response.ok


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    return parser


def main():
    load_dotenv()

    parser = createParser()
    user_link = parser.parse_args().link

    headers = {
        'Authorization': 'Bearer {}'.format(os.environ['API-TOKEN'])
    }

    try:
        requests.get(user_link)
    except requests.exceptions.ConnectionError:
        return 'Неверная ссылка'

    if is_bitlink(user_link, headers):
        return count_clicks(user_link, headers)
    else:
        return shorten_link(user_link, headers)


if __name__ == '__main__':
    print(main())
