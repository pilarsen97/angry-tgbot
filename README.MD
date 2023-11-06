Этот темплейт используется для разработки Telegram ботов с использованием библиотеки [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x).

## SQLAlchemy + Alembic
В коде есть примеры таблички User с использованием SQLAlchemy 2.0, и скрипты для алембика (инициализация алембик, создание и применение миграций).

![img.png](https://img-c.udemycdn.com/course/240x135/5320614_a8af_2.jpg)

### Для того, чтобы начать использовать:
1. Скопируйте'.env.dist 'в'.env ' и заполните необходимые данные.
2. Создайте новые хэндлеры.
3. **Docker:**
   1. Можете сразу запускать проект из Docker, а если у вас его нет, то [загрузите, и установите](https://docs.docker.com/get-docker/).
   2. Запустите проект из команды ' docker-compose up`
4. **Без Docker:**
   1. Создать [venv](https://docs.python.org/3/library/venv.html)
   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```
   2. Установить зависимости с requirements.txt:
      - `pip install -r requirements.txt`
      - `pip install -r requirements.txt --pre` - пре-релизные версии
   3. Запустите проект из команды 
   ```bash
   python3 bot.py 
   ```


### Как делать и регистрировать хэндлеры:
Создаете модуль `you_name.py 'в папке 'handlers'.

Создаете роутер в `you_name.py`.
```python
from aiogram import Router
user_router = Router()
```
Можно делать несколько роутеров в одном модуле, и на каждый из них навешивать хэндлеры.
Можно регистрировать хэндлеры декораторами:
```python
@user_router.message(commands=["start"])
async def user_start(message):
    await message.reply("Поздравляю, обычный пользователь!")
```

Заходим в файл `bot.py ' и добавляем все роутеры в него:
```python
from tgbot.handlers.admin import admin_router
from tgbot.handlers.echo import echo_router
from tgbot.handlers.user import user_router

...

async def main():
   
   ...

    for router in [
        admin_router,
        user_router,
        ...,
        echo_router,

    ]:
        dp.include_router(router)
```

## Настройка на сервере
### Загрузка вашего приложения на сервер
Теперь загрузите исходный код вашего приложения на сервер. Вы можете использовать такие инструменты, как scp, rsync или git для копирования кода на сервер

```bash
git clone https://github.com/yourusername/yourapp.git
cd yourapp
```

### Установка виртуального окружения
Создайте виртуальное окружение для вашего приложения. Это позволит изолировать зависимости вашего приложения от системных библиотек.

```bash
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей
Теперь установите зависимости вашего приложения с помощью pip.
```bash
pip install -r requirements.txt
```

### Автозагрузка .py скрипта на Linux
Как вариант, если у Вас есть systemd
```bash
sudo vim /etc/systemd/system/<your_bot_name>.service
```
```
[Unit]
Description=Telegram bot 'BOT'
After=syslog.target
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/bots/<bot_directory>
ExecStart=/usr/bin/python3 /root/bots/<bot_directory>/bot.py
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```
Затем
```
sudo systemctl daemon-reload
sudo systemctl start <your_bot_name>.service
sudo systemctl status <your_bot_name>.service
# если все норм и юнит запустился...
sudo systemctl enable <your_bot_name>.service
```

### Туториалы с aiogram v3
Видосов пока нет, но @Groosha уже начал делать [свой учебник](https://mastergroosha.github.io/aiogram-3-guide).
