import functools
from .user import User
from .message import Message

class QuicheBotConnector:
    connector_name = 'GlobalConnector'
    def __init__(self):
        self.core = None

    def assign_core(self, core):
        self.core = core

    def send_message(self, text):
        return

class QuicheBotCore:
    def __init__(self):
        self.connectors = {}

    def attach(self, connector: QuicheBotConnector):
        if connector.assign_core(self):
            self.connectors[connector.connector_name] = connector

    def ping_command(self, message: Message):
        if len(message.command) == 1:
            self.connectors[message.msg_source].send_message('Hello!')
