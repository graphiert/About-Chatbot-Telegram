# @galihpujiirianto https://github.com/galihpujiirianto/AboutMe-tgbot

from pyrogram.types import InlineKeyboardButton

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
