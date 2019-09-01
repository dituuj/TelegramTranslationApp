"""Full Translation App"""

from os import getenv
from pyrogram import Client, Filters
from translate import Translator
from consumers import TelegramConsumer
translator= Translator(to_lang="en", from_lang='zh')
postScript= "\n\n\n TranslatorBot via pyrogram"

RecieveCh = "me"
# RecieveCh = -1001173826177 # For Real HK Channel

api_id = getenv('API_ID')
api_id_hash = getenv('API_ID_HASH')
app = Client("my_account", api_id, api_id_hash)

consumers = [
    # TelegramConsumer(app, -324271754), # HK Translation Chat
    TelegramConsumer(app, 'me'), # self, for testing
]

@app.on_message(Filters.chat(RecieveCh) & Filters.photo & Filters.caption)
def echoPT(client, message):
    translation = translator.translate(message.caption) + postScript
    for consumer in consumers:
        consumer.send_photo(message.photo.file_id, translation)
    return

@app.on_message(Filters.chat(RecieveCh) & Filters.photo & ~Filters.caption)
def echoP(client, message):
    for consumer in consumers:
        consumer.send_photo(message.photo.file_id)
    return

@app.on_message(Filters.chat(RecieveCh) & Filters.text & ~Filters.photo)
def echoT(client, message):
    translation = translator.translate(message.text) + postScript
    for consumer in consumers:
        consumer.send_text(translation)
    return




app.run()  # Automatically start() and idle()