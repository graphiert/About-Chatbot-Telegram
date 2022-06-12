from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle
)
from keyboard import *
from utils import *
from config import (
    MSG_START, IMG_START, ONWER_ID,
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

@bot.on_inline_query(filters.user(OWNER_ID))
def inline_query(_, inline_query):
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
def notowner(_, inline_query):
   inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="You're not allowed!",
                description="This can only work by bot owner.",
                input_message_content=InputTextMessageContent("No. You aren't allowed to accessed this bot using inline.")
            )
        ]
    )

@bot.on_message(filters.private & ~filters.edited)
def incoming_private(_, message):
    user_id = message.from_user.id
    if user_id == OWNER_ID:
        sender = message.reply_to_message.forward_sender_name
        for name, rep_uid in chatbot.items():
            if name == sender:
                message.forward(rep_uid, is_copy=True)
    else:
        if bot.get_me() == message.from_user.id:
            return
        name = message.from_user.first_name
        chatbot[name] = message.from_user.id
        message.forward(OWNER_ID)