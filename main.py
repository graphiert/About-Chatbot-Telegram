# @galihpujiirianto https://github.com/galihpujiirianto/AboutMe-tgbot
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
import os
from dotenv import load_dotenv
from msg_config import *
from buttons import *

load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)

def send(message, photo, text, reply_markup):
    def edit(message, text, reply_markup):
        message.edit_message_text(
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    if IMG_START:
        try:
            message.reply_photo(
                photo=photo,
                caption=text,
                reply_markup=reply_markup
            )
        except AttributeError:
            edit(message, text, reply_markup)
    elif IMG_START == None:
        try:
            message.reply_text(
                text=text,
                reply_markup=reply_markup,
                disable_web_page_preview=True
            )
        except AttributeError:
            edit(message, text, reply_markup)

@bot.on_message(filters.command("start") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"back"))
def start(bot, message):
    photo=IMG_START
    text=MSG_START.format(message.from_user.mention)
    reply_markup=InlineKeyboardMarkup(KEYBOARD_HOME)
    send(message, photo, text, reply_markup)

@bot.on_message(filters.command("about") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"about"))
def about(bot, message):
    photo=IMG_START
    text=ABOUT_MSG
    reply_markup=InlineKeyboardMarkup(KEYBOARD_ABOUT)
    send(message, photo, text, reply_markup)

@bot.on_message(filters.command("projects") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"projects"))
def projects(bot, message):
    photo=IMG_START
    text=PROJECTS_MSG
    reply_markup=InlineKeyboardMarkup(KEYBOARD_PROJECTS)
    send(message, photo, text, reply_markup)

@bot.on_message(filters.command("socmed") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"socmed"))
def socmed(bot, message):
    photo=IMG_START
    text=SOCMED_MSG
    reply_markup=InlineKeyboardMarkup(KEYBOARD_SOCMED)
    send(message, photo, text, reply_markup)

print_txt = 'System started! Developed and Maintaned by Galih\n'
print_txt += 'https://github.com/galihpujiirianto | https://t.me/puffypawsy\n'
print_txt += 'Any questions? Say it at https://t.me/GalonSupport\n'
print(print_txt)
bot.run()
