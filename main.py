import os
import discord
import requests
import json
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "\"" + json_data[0]["q"] + "\" -" + json_data[0]["a"]
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$earrape"):
        await message.channel.send("-p https://www.youtube.com/watch?v=FfWoHZFci0g")
        await message.channel.send("-loop")
    if message.content.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)


client.run(os.getenv("TOKEN"))
