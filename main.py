from Core.connector import QuicheBotCore
from TwitchConnector import TwitchConnector
from DiscordConnector import DiscordConnector
from MinecraftConnector import MinecraftConnector

if __name__ == '__main__':
    core = QuicheBotCore()
    twitchcon = TwitchConnector()
    discordcon = DiscordConnector()
    minecraftcon = MinecraftConnector()

    core.attach(twitchcon)
    core.attach(discordcon)
    core.attach(minecraftcon)