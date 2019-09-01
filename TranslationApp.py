"""Full Translation App"""

from os import getenv
from pyrogram import Client, Filters
from translate import Translator
translator= Translator(to_lang="en", from_lang='zh')
postScript= "\n\n\n TranslatorBot via pyrogram"

RecieveCh = "me"
# RecieveCh = -1001173826177 # For Real HK Channel
SendCh = "me"
# SendCh = -324271754

api_id = getenv('API_ID')
api_id_hash = getenv('API_ID_HASH')
app = Client("my_account", api_id, api_id_hash)


@app.on_message(Filters.chat(RecieveCh) & Filters.photo & Filters.caption)
def echoPT(client, message):
    translation = translator.translate(message.caption) + postScript
    app.send_photo(SendCh,message.photo.file_id, translation)
    return

@app.on_message(Filters.chat(RecieveCh) & Filters.photo & ~Filters.caption)
def echoP(client, message):
    app.send_photo(SendCh,message.photo.file_id)
    return

@app.on_message(Filters.chat(RecieveCh) & Filters.text & ~Filters.photo)
def echoT(client, message):
    translation = translator.translate(message.text) + postScript
    app.send_message(SendCh, translation)
    return




app.run()  # Automatically start() and idle()