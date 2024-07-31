import requests
import os
import time
import random
from dotenv import load_dotenv
import telegram
from pathlib import Path
from telegram.error import NetworkError


def load_keys(token):
    load_dotenv()
    key = os.environ[token]
    return key


def requests_img(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_img(url, filename, image_format="jpeg", path="Files"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if path == "Files":
        full_path = os.path.join(script_dir, path, f"{filename}")
    else:
        full_path = os.path.join(path, f"{filename}")
    os.makedirs(path, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(f"{full_path}.{image_format}", 'wb') as file:
        file.write(response.content)


def create_full_path(file_name, image_path):
    os.makedirs(image_path, exist_ok=True)
    for path in Path(image_path).rglob('{}.{}'.format(file_name, "*")):
        if path.stem == str(file_name):
            return path.resolve()


def open_file(file):
    with open(file, 'rb') as photo:
        return photo.read()


def trying_send_tg_message(load_key, path_photo, token, message):
    bot = telegram.Bot(token=token)
    retries = 0
    for attempt in range(31):
        try:
            bot.send_photo(chat_id=load_key, photo=path_photo, caption=message)
            break
        except NetworkError:
            if retries == 0:
                time.sleep(1)
            else:
                time.sleep(10)
            retries += 1


def main():
    tg_channel = load_keys("TG_CHANNEL")
    tg_key = load_keys("TG_KEY")
    page = random.randrange(2965)
    url = f'https://xkcd.com/{page}/info.0.json'
    resp = requests_img(url)
    save_img(resp['img'], page)
    photo_path = create_full_path(file_name=page, image_path='Files')
    trying_send_tg_message(tg_channel, open_file(photo_path), tg_key, resp['alt'])
    Path.unlink(photo_path)


if __name__ == '__main__':
    main()
