import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn = [[InlineKeyboardButton('🇮🇳 Updates Channel', url=f'https://t.me/Opleech')]]
STARTER = InlineKeyboardMarkup(btn)

BOTBY = "@Bullet_350cc"

def forceMe(id):
    url = f""
    res = requests.get(url).json()
    return res


def notJoin(c,m):
    button = [[InlineKeyboardButton('🇮🇳 Updates Channel', url=f'https://t.me/Opleech')]]
    markup = InlineKeyboardMarkup(button)
    return c.send_message(chat_id=m.chat.id, text="""Hi Broh 👋 \n👉<i> You need to join</i> <b>@WD_Contact_Bot</b> \n<i>Do /start after joining the channel</i>""", reply_markup=markup)

