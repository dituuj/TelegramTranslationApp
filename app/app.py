from pyrogram import Client, Filters

post_script = "\n\n\n TranslatorBot via pyrogram"

class TranslationApp:
    def __init__(self, telegram_client, chat_to_translate):
        self.telegram_client = telegram_client
        self.chat_id = chat_to_translate
        self.consumers = []
        self.translators = []

    def add_consumers(self, *args):
        self.consumers.extend(args)

    def add_translators(self, *args):
        self.translators.extend(args)

    def translate(self, text):
        for t in self.translators:
            result = t.translate(text)
            if result:
                return result + post_script
        # TODO(walt): publish or alert this error message somewhere other than console
        print('Error: all translators have failed!')
        return None

    def send_text(self, text):
        for consumer in self.consumers:
            consumer.send_text(text)

    def send_photo(self, file_id, caption=None):
        for consumer in self.consumers:
            consumer.send_photo(file_id, caption)

    def run(self):
        @self.telegram_client.on_message(Filters.chat(self.chat_id) & Filters.photo & Filters.caption)
        def echoPT(client, message):
            translation = self.translate(message.caption)
            self.send_photo(message.photo.file_id, translation)

        @self.telegram_client.on_message(Filters.chat(self.chat_id) & Filters.photo & ~Filters.caption)
        def echoP(client, message):
            self.send_photo(message.photo.file_id)

        @self.telegram_client.on_message(Filters.chat(self.chat_id) & Filters.text & ~Filters.photo)
        def echoT(client, message):
            translation = self.translate(message.text)
            if translation:
                self.send_text(translation)

        self.telegram_client.run()
