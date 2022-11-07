# @galihpujiirianto https://github.com/galihpujiirianto/About-Chatbot-Telegram

import os
from pyrogram import Client, filters, idle
from pyrogram.types import (
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.errors import BadRequest

def started():
    try:
        open("print_txt.py", "r")
    except FileNotFoundError:
        os.system("wget https://bit.ly/3Ksaa7N -O print_txt.py")
    print()
    from print_txt import print_txt
    return print(print_txt)

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
TOKEN = os.environ.get("TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")
MSG_START = str(os.environ.get("MSG_START"))
IMG_START = os.environ.get("IMG_START")
ABOUT_MSG = str(os.environ.get("ABOUT_MSG"))
PROJECTS_MSG = str(os.environ.get("PROJECTS_MSG"))
SOCMED_MSG = str(os.environ.get("SOCMED_MSG"))

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)

if not OWNER_ID:
    raise ValueError("""Please enter your OWNER_ID! The bot will be disabled.
Please reactivate it when you have entered the OWNER_ID!""")

try:
    OWNER_ID = int(OWNER_ID)
except TypeError:
    raise ValueError("Please enter your OWNER_ID only numbers!")

chatbot = {}

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
    if photo:
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
def start(_, message):
    photo=IMG_START
    text=MSG_START.format(message.from_user.mention) + "\n\npsst, you can chat me via this bot UwU"
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
    send(message, photo, text, reply_markup)# @galihpujiirianto https://github.com/galihpujiirianto/About-Chatbot-Telegram

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
        if message.reply_to_message:
            sender = message.reply_to_message.forward_sender_name
            try:
                message.copy(chatbot.get(message.reply_to_message.forward_sender_name))
            except TypeError:
                message.reply("This message couldn't be sent because the sender hasn't sent his last message here.")
            except BadRequest:
                message.reply("The sender has blocked you.")
    else:
        if bot.get_me().id == user_id:
            return
        chatbot.update({message.from_user.first_name: message.from_user.id})
        message.forward(OWNER_ID)

started()
bot.start()
idle()
