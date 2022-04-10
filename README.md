# About Me Telegram Bot

## 🔗 About this project
![Demo](https://telegra.ph/file/5b295909d59a7a5d51219.jpg)

Telegram bot to describe yourself. Using Python and based on Pyogram.

## ⚡️ How to setup?
Very easy. Can deploy using Heroku, Replit or install locally.

### 🚀 Using Replit
Video tutorial? Coming soon.
> Note: The video tutorial above is just an illustration, for more details, please read below.
1. Create a [Replit](https://replit.com) account first.
2. [Duplicate this repository to Replit](https://replit.com/github/galihpujiirianto/AboutMe-tgbot), then wait for it to finish.
3. For mobile users:
    - In the navigation menu at the bottom, select "Console", then type the command `python3 main.py`.
    - Back again in the bottom navigation menu, select "Code", then in the upper right corner there is a file button, open the `msg_config.py` file, then edit as needed.
    > The writing guide is already in the file.
    - Back again in the bottom navigation menu, select the "Commands" menu, then select "Secret". Then enter the required variables.
    - When done, press the play button in the lower right corner.
4. For PC users:
    - On the right, there is Console, type the command `python3 main.py`.
    - On the left, select `msg_config.py`, then edit as needed.
    > The writing guide is already in the file.
    - In the left navigation menu, select the lock icon, then enter the required variables.
    - When done, click the play icon in the top center.

### 💻 Local installation
1. Before running, install Git and Python first.
2. Clone this repository and go to the folder - `git clone https://github.com/galihpujiirianto/AboutMe-tgbot.git && cd AboutMe-tgbot`
3. Install required packages - `python3 main.py`
4. Fill in the variables as in Vars - `nano .env`
> After filling in the variables correctly, press `CTRL + S` and `CTRL + X` to save.
5. Edit the string in [msg_config.py](./msg_config.py) - `nano msg_config.py`
> After filling in the string correctly, press `CTRL + S` and `CTRL + X` to save.
6. Run the bot - `bash run`

## 📎 Vars
After cloning the repository and install the package, create an `env` file and fill in the following variables:
```
API_ID = get it from https://my.telegram.org/apps
API_HASH = get it from https://my.telegram.org/apps
TOKEN = Create a new bot on Telegram using https://t.me/BotFather
OWNER_ID = Start https://t.me/ChitandaEruRobot then type the /id command
```

## 📃 String Editing
Open the [msg_config.py](./msg_config.py) file, and change the string as needed.
> Instructions for filling in the strings have been provided in the file, please pay close attention to the filling sentences.

## ✍🏻 Support, Credits, License, etc
Reach out your problem to the maintainer at [Telegram Group Support](https://t.me/GalonSupport).

If you want this repository to stay active, please help us with:
- Add a [GitHub Star](https://github.com/galihpujiirianto/AboutMe-tgbot) to this project,
- Fork this repo :)
- Write interesting articles about the project on [Dev.to](dev.to), [Medium](medium.com) or your personal blog,
- or you can donate through [Saweria](https://saweria.co/galihpujiirianto).

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place 
to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

This project is licensed under the GNU General Public License v2. See [LICENSE](./LICENSE) for more information.

Thank you for:
- [Me](https://github.com/galihpujiirianto) for created this manually,
- [Dion](https://github.com/SeorangDion) for correcting an existing error,
- [Pyrogram](https://github.com/pyrogram/pyrogram) for this code to work.

And thanks to all the code samples that are on the Internet.
