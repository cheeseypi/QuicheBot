import threading
import asyncio
import discord
from Core.connector import QuicheBotConnector
from Core.message import Message
from Core.user import User
from Core.settings import load_setting


class DiscordConnector(QuicheBotConnector):
    connector_name = 'Discord'

    def __init__(self):
        super().__init__()
        settings = load_setting('discord')
        self.enabled = settings['enable']
        self.token = settings['token']
        self.client = discord.Client()

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            user = User(message.author.name, message.author.id,
                        None, message.author)
            msg_obj = Message(message.content, user,
                              self.connector_name, message)
            self.core.ping_command(msg_obj)

    def assign_core(self, core):
        if not self.enabled:
            return False
        super().assign_core(core)
        loop = asyncio.get_event_loop()
        loop.create_task(self.client.start(self.token))
        threading.Thread(target=loop.run_forever).start()
        # self.client.run(self.token)
        return True

    def send_message(self, message, sent_object):
        asyncio.run(sent_object.channel.send(message))
