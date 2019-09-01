from pyrogram import Client, Filters
from translate import Translator

translator= Translator(to_lang="en", from_lang='zh')
post_script = "\n\n\n TranslatorBot via pyrogram"

class TranslationApp:
    def __init__(self, telegram_client, chat_id):
        self.telegram_client = telegram_client
        self.chat_id = chat_id
        self.consumers = []

    def add_consumers(self, *args):
        self.consumers.extend(*args)

    def send_text(self, text):
        for consumer in self.consumers:
            consumer.send_text(text)

    def send_photo(self, file_id, caption=None):
        for consumer in self.consumers:
            consumer.send_photo(file_id, caption)

    def run(self):
        @self.telegram_client.on_message(Filters.chat(self.chat_id) & Filters.photo & Filters.caption)
        def echoPT(client, message):
            translation = translator.translate(message.caption) + post_script
            self.send_photo(message.photo.file_id, translation)

        @self.telegram_client.on_message(Filters.chat(self.chat_id) & Filters.photo & ~Filters.caption)
        def echoP(client, message):
            self.send_photo(message.photo.file_id)

        @self.telegram_client.on_message(Filters.chat(self.chat_id) & Filters.text & ~Filters.photo)
        def echoT(client, message):
            translation = translator.translate(message.text) + post_script
            self.send_text(translation)

        self.telegram_client.run()
