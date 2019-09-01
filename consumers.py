class Consumer:
    def send_photo(self, file_id, caption=None):
        pass

    def send_text(self, text):
        pass


class TelegramConsumer:
    def __init__(self, client, chat_id):
        self.client = client
        self.chat_id = chat_id

    def send_photo(self, file_id, caption=None):
        self.client.send_photo(self.chat_id, file_id, caption)

    def send_text(self, text):
        self.client.send_message(self.chat_id, text)


