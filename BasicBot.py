# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import json

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Every wanted to kys yourself? Now you can.", command_prefix="-", pm_help=True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,
                                                                               platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Github Link: https://github.com/Habchy/BasicBot')
    print('--------')
    print('Created by TheRedshift#1309')

with open('data.txt') as json_file:
    data = json.load(json_file)


@client.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await client.say(random.choice(choices))


@client.command(pass_context=True)
async def kys(ctx, arg):
    temp = data.get("insults")
    temp = temp[random.randint(0, len(temp))].get("text")
    await client.say('' + arg + '' + str(temp)+''.format(ctx))


@client.command(pass_context=True)
async def addInsult(ctx, arg):
    data['insults'].append({
        'id': str(len(data) + 1),
        'text': arg
    })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


with open('token.txt', "r") as token_file:
    token = str(token_file.readline()).rstrip()
    print(token)


client.run(str(token))


# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.
