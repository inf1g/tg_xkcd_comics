import requests
import os
import time
import random
from dotenv import load_dotenv
import telegram
from pathlib import Path
from telegram.error import NetworkError


def try_send_tg_message(load_key, path_photo, token, message):
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
    load_dotenv()
    tg_channel = os.environ["TG_CHANNEL"]
    tg_key = os.environ["TG_KEY"]
    total_comics_pages = 2965
    path = "Files"
    page = random.randrange(total_comics_pages)
    url = f'https://xkcd.com/{page}/info.0.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        response_img = requests.get(response['img'])
        response_img.raise_for_status()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, path, f"{page}")
        os.makedirs(path, exist_ok=True)
        photo_path = f"{full_path}.jpeg"
        with open(photo_path, 'wb') as file:
            file.write(response_img.content)
        with open(photo_path, 'rb') as photo:
            photo = photo.read()
            try_send_tg_message(tg_channel, photo, tg_key, response['alt'])
    finally:
        Path.unlink(photo_path)


if __name__ == '__main__':
    main()
