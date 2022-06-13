# @galihpujiirianto https://github.com/galihpujiirianto/About-Chatbot-Telegram
import os
# Fill constant variable
#-----------------------
API_ID = os.environ["API_ID"] # Enter API_ID, get it from https://my.telegram.org/apps
API_HASH = os.environ["API_HASH"] # Enter API_HASH, get it from https://my.telegram.org/apps
TOKEN = os.environ["TOKEN"] # Enter TOKEN, get it from https://t.me/BotFather
OWNER_ID = os.environ["OWNER_ID"] # Enter OWNER_ID, start https://t.me/Missrose_bot and type /id

# Message Configuration
#----------------------
# Message to be sent when user clicks /start. Note:
# use {} to mention the user who started the bot.
# Note: Use Markdown Parse Mode to give markdown.
MSG_START = str(os.environ["MSG_START"])

# If you want to use an image, enter the telegraph link
# here. If you don't want to use an image, remove the
# quote character and its contents, then fill it with None.
# Or you can also ignore it.
IMG_START = str(os.environ["IMG_START"])

# Message that will be sent when the user presses the
# about button or when the user sends the /about command.
# Note: Use Markdown Parse Mode to give markdown.
ABOUT_MSG = str(os.environ["ABOUT_MSG"])

# Message that will be sent when the user presses the
# projects button or when the user sends the /projects command.
# Note: Use Markdown Parse Mode to give markdown.
PROJECTS_MSG = str(os.environ["PROJECT_MSG"])

# Message that will be sent when the user presses the
# social media button or when the user sends the /socmed command.
# Note: Use Markdown Parse Mode to give markdown.
SOCMED_MSG = str(os.environ["SOCMED_MSG"])
