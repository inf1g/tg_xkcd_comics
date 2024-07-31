## Комикс xkcd про Python.

Скачивает случайный комикс xkcd и публикует указанную фотографию в Telegram канал.
 

## Установка

1. Для запуска должен быть установлен [Python 3](https://www.python.org/downloads/release/python-3124/)
2. Клонируйте репозиторий с github
3. Установите зависимости 
```bash
pip install -r requirements.txt
```
4. Создайте файл `.env` укажите 'Токен' для Telegram бота как на примере ниже, замените `0123456789abcdefgh` на свой сервисный ключ – “токен” Telegram.
```bash
TG_KEY==0123456789abcdefgh
```
### Как его получить:
- Зарегистрируйтесь в Telegram — [зарегистрируйтесь](https://web.telegram.im/)
- Откройте чат с [@BotFather](https://telegram.me/BotFather).
- Для создания нового бота отправьте команду в чат 
```bash
/newbot
```
- Выберите имя для своего бота и имя пользователя Telegram для вашего бота. Оно должно заканчиваться на bot. 

![Static Badge](https://way23.ru/images/telegram_newbot.png)

- В ответном сообщении приходит токен который нужен для управления ботом через API.


---
#### Укажите Telegram канал куда будут публиковаться фото.

5. В файл `.env` укажите имя вашего канала Telegram, как на примере ниже. Замените @tg_test_channel на имя канала, куда будут публиковаться фото.
```bash
TG_CHANNEL=@tg_test_channel
```

6. Запустите скрипт 'main.py'
```bash
python main.py
```
---
## Создано с помощью 

![!Static Badge](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)

## Цель проекта

Код написан в учебных целях - для урока в курсе Python и API веб-сервисов на сайте [Devman](https://dvmn.org/) 
