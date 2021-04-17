from mcipc.rcon.je import Client
from Core import QuicheBotConnector, User, Message, load_setting

class MinecraftConnector(QuicheBotConnector):
    connector_name = "Minecraft"
    def __init__(self):
        super().__init__()
        settings = load_setting('minecraft')
        self.enabled = settings['enable']
        self.ip = settings['ip']
        self.port = settings['port']
        self.secret = settings['secret']

    def assign_core(self, core):
        super().assign_core(core)
        if not self.enabled:
            return False
        return True

    def send_message(self, message, obj):
        with Client(self.ip, self.port, passwd=self.secret) as client:
            return str(client.run(message))