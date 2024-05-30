import os
import time

import discord
import configparser

intents = discord.Intents.default()
bot = discord.Client(intents=intents)


def create_config():
    id_chat = "0000000000000000000"
    config = configparser.ConfigParser()

    config.add_section('Login')

    config.set('Login', 'token', '')

    with open('config.cfg', 'w') as configfile:
        config.write(configfile)


def read_config():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    config = {
        "token": config.get('Login', 'token'),
    }
    return config


if __name__ == '__main__':
    if not os.path.exists('config.cfg'):
        create_config()
        time.sleep(5)
        cfg = read_config()
    else:
        cfg = read_config()

    token = cfg["token"]




bot.run(token)