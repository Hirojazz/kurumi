import html
import random
import time
import requests

import KURUMIBOT.modules.meme_strings as meme_strings
from KURUMIBOT import dispatcher
from KURUMIBOT.modules.disable import DisableAbleCommandHandler
from KURUMIBOT.modules.helper_funcs.chat_status import is_user_admin
from KURUMIBOT.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async

GIF_ID = "CgACAgQAAx0CSVUvGgAC7KpfWxMrgGyQs-GUUJgt-TSO8cOIDgACaAgAAlZD0VHT3Zynpr5nGxsE"


@run_async
def hugs(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(GIF_ID, caption=f"*hugs {name}*")


@run_async
def hugs(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(random.choice(meme_strings.GIFS), caption=f"*hugs {name}*")
   
   
#plugin by t.me/RCage
@run_async
def meme(update: Update, context: CallbackContext):
    msg = update.effective_message
    meme = requests.get("https://meme-api.herokuapp.com/gimme/Animemes/").json()
    image = meme.get("url")
    caption = meme.get("title")
    if not image:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(
                photo=image, caption=caption)


MEME_HANDLER = DisableAbleCommandHandler("meme", meme)
HUGS_HANDLER = DisableAbleCommandHandler("hugs", hugs)

dispatcher.add_handler(MEME_HANDLER)
dispatcher.add_handler(HUGS_HANDLER)

__command_list__ = [
    "hugs",
    "meme",
]
__handlers__ = [
    HUGS_HANDLER,
    MEME_HANDLER,
]
