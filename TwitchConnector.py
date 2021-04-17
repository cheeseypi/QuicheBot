import twitch
from Core.connector import QuicheBotConnector
from Core.message import Message
from Core.user import User
from Core.settings import load_setting


class TwitchConnector(QuicheBotConnector):
    connector_name = "Twitch"

    def __init__(self):
        super().__init__()
        self.helix = None
        self.chat = None
        settings = load_setting('twitch')
        self.enabled = settings['enable']
        self.client_id = settings['client-id']
        self.client_secret = settings['client-secret']
        self.oauth = settings['oauth']
        self.channel = settings['channel']
        self.nick = settings['nickname']

    def assign_core(self, core):
        if not self.enabled:
            return False
        super().assign_core(core)
        self.helix = twitch.Helix(
            'jqqxdo6tewc80vot6w66mkzfnso558', '7tsxcnw9efuxbjk3q2r8ebdx54k01c')
        self.chat = twitch.Chat(channel='#cheeseypi', nickname='cheeseyquichebot',
                                oauth='oauth:948piogkdqxbti42c8pwu0grd5zily', helix=self.helix)
        self.chat.subscribe((lambda message: self.receivedMessage(message)))
        return True

    def receivedMessage(self, message: twitch.chat.Message):
        user = User(message.user.login, message.user.id,
                    message.user.display_name, message.user)
        msg_obj = Message(message.text, user, self.connector_name)
        if(msg_obj.is_command):
            self.core.ping_command(msg_obj)

    def send_message(self, text, sent_object):
        self.chat.send(text)
