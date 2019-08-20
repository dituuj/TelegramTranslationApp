"""Full Translation App"""

from pyrogram import Client, Filters
from translate import Translator
translator= Translator(to_lang="en", from_lang='zh')
postScript= "\n\n\n TranslatorBot via pyrogram"

#RecieveCh = "me"
RecieveCh = -1001173826177 # For Real HK Channel
SendCh = -324271754
app = Client("my_account")


@app.on_message(Filters.chat(RecieveCh) & Filters.photo & Filters.caption)
def echo(client, message):
    translation = translator.translate(message.caption) + postScript
    app.send_photo(SendCh,message.photo.file_id, translation)
    return

@app.on_message(Filters.chat(RecieveCh) & Filters.photo & ~Filters.caption)
def echo(client, message):
    app.send_photo(SendCh,message.photo.file_id)
    return

@app.on_message(Filters.chat(RecieveCh) & Filters.text)
def echo(client, message):
    translation = translator.translate(message.text) + postScript
    app.send_message(SendCh, translation)
    return

    


app.run()  # Automatically start() and idle()