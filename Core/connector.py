import functools
from .user import User
from .message import Message


class QuicheBotConnector:
    connector_name = 'GlobalConnector'

    def __init__(self):
        self.core = None

    def assign_core(self, core):
        self.core = core

    def send_message(self, text, sent_object):
        return


class QuicheBotCore:
    def __init__(self):
        self.connectors = {}

    def attach(self, connector: QuicheBotConnector):
        if connector.assign_core(self):
            self.connectors[connector.connector_name] = connector
            print("Connected", connector.connector_name)

    def ping_command(self, message: Message):
        if message.is_command and len(message.command) > 0:
            if message.command[0] == 'mcexec':
                response = self.connectors['Minecraft'].send_message(str.join(' ', message.command[1:]), None)
                self.connectors[message.msg_source].send_message(response, message)
            else:
                self.connectors[message.msg_source].send_message('pong', message)
