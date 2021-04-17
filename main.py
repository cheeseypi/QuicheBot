from Core.connector import QuicheBotCore
from TwitchConnector import TwitchConnector

if __name__ == '__main__':
    core = QuicheBotCore()
    twitchcon = TwitchConnector()

    core.attach(twitchcon)