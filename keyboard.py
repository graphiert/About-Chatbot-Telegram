from pyrogram.types import InlineKeyboardButton

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