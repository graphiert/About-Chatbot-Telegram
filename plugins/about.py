# @galihpujiirianto https://github.com/galihpujiirianto/About-Chatbot-Telegram

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
from utils import *
from main import bot
from config import (
    MSG_START, IMG_START,
    ABOUT_MSG, PROJECTS_MSG, SOCMED_MSG
)

@bot.on_message(filters.command("start") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"back"))
def start(_, message):
    photo=IMG_START
    text=MSG_START.format(message.from_user.mention) + "\n\n psst, you can chat me via this bot UwU"
    reply_markup=InlineKeyboardMarkup(KEYBOARD_HOME)
    send(message, photo, text, reply_markup)

@bot.on_message(filters.command("about") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"about"))
def about(_, message):
    photo=IMG_START
    text=ABOUT_MSG
    reply_markup=InlineKeyboardMarkup(KEYBOARD_ABOUT)
    send(message, photo, text, reply_markup)

@bot.on_message(filters.command("projects") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"projects"))
def projects(_, message):
    photo=IMG_START
    text=PROJECTS_MSG
    reply_markup=InlineKeyboardMarkup(KEYBOARD_PROJECTS)
    send(message, photo, text, reply_markup)

@bot.on_message(filters.command("socmed") & filters.private)
@bot.on_callback_query(filters.regex(pattern=r"socmed"))
def socmed(_, message):
    photo=IMG_START
    text=SOCMED_MSG
    reply_markup=InlineKeyboardMarkup(KEYBOARD_SOCMED)
    send(message, photo, text, reply_markup)
