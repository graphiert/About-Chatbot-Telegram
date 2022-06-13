# @galihpujiirianto https://github.com/galihpujiirianto/About-Chatbot-Telegram

from pyrogram import filters
from pyrogram.types import (
    InputTextMessageContent,
    InlineQueryResultArticle
)
from main import bot
from config import (
    MSG_START, IMG_START, ONWER_ID,
    ABOUT_MSG, PROJECTS_MSG, SOCMED_MSG
)

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
