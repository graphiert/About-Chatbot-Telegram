# @galihpujiirianto https://github.com/galihpujiirianto/About-Chatbot-Telegram

from pyrogram import filters
from utils import chatbot
from config import OWNER_ID
from main import bot

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
