# @galihpujiirianto https://github.com/galihpujiirianto/AboutMe-tgbot

import os, sys
os.system("pip3 install Pyrogram==1.4.16 TgCrypto Flask")
from pyrogram import Client
from config import (
    API_ID, API_HASH, TOKEN, OWNER_ID
)

if not OWNER_ID:
    raise ValueError("Please enter your OWNER_ID! The bot will be disabled. Please reactivate it when you have entered the OWNER_ID!")

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins={"include"=["plugin"]}
)

os.system("wget https://bit.ly/3Ksaa7N -O print_txt.py")
from keep_alive import keep_alive
from print_txt import print_txt
print(print_txt)
keep_alive()
bot.run()
