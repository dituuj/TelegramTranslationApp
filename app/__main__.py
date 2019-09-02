"""Full Translation App"""

from os import getenv
from pyrogram import Client
from consumers import TelegramConsumer
from app import TranslationApp

api_id = getenv('API_ID')
api_id_hash = getenv('API_ID_HASH')
# TODO(walt): consider whether to move this construction into app.py, and if so how
client = Client("my_account", api_id, api_id_hash)

app = TranslationApp(client, 'me') # Replace 'me' with -1001173826177 for real HK channel

app.add_consumers([
    # TelegramConsumer(app, -324271754), # HK Translation Chat
    TelegramConsumer(client, 'me'), # self, for testing
])

app.run()  # Automatically start() and idle()
