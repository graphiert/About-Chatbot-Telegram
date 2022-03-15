# @galihpujiirianto https://github.com/galihpujiirianto/AboutMe-tgbot

from pyrogram.types import InlineKeyboardButton
from msg_config import (
    ABOUT_BTN, PROJECTS_BTN,
    SOCMED_BTN, BCK_BTN
)

KEYBOARD_HOME = [
            [
                InlineKeyboardButton(text=ABOUT_BTN, callback_data=f"about"),
                InlineKeyboardButton(text=PROJECTS_BTN, callback_data=f"projects")
            ],
            [
                InlineKeyboardButton(text=SOCMED_BTN, callback_data=f"socmed")
            ]
]
KEYBOARD_ABOUT = [
            [
                InlineKeyboardButton(text=PROJECTS_BTN, callback_data=f"projects"),
                InlineKeyboardButton(text=SOCMED_BTN, callback_data=f"socmed")
            ],
            [
                InlineKeyboardButton(text=BCK_BTN, callback_data=f"back")
            ]
]
KEYBOARD_PROJECTS = [
            [
                InlineKeyboardButton(text=ABOUT_BTN, callback_data=f"about"),
                InlineKeyboardButton(text=SOCMED_BTN, callback_data=f"socmed")
            ],
            [
                InlineKeyboardButton(text=BCK_BTN, callback_data=f"back")
            ]
]
KEYBOARD_SOCMED = [
            [
                InlineKeyboardButton(text=ABOUT_BTN, callback_data=f"about"),
                InlineKeyboardButton(text=PROJECTS_BTN, callback_data=f"projects")
            ],
            [
                InlineKeyboardButton(text=BCK_BTN, callback_data=f"back")
            ]
]