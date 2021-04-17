from Core.connector import QuicheBotCore
from TwitchConnector import TwitchConnector
from DiscordConnector import DiscordConnector

if __name__ == '__main__':
    core = QuicheBotCore()
    twitchcon = TwitchConnector()
    discordcon = DiscordConnector()

    core.attach(twitchcon)
    core.attach(discordcon)