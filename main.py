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
        channel1 = client.get_channel(865462494583980032)
        await channel1.send("-p https://www.youtube.com/watch?v=FfWoHZFci0g")
        await channel1.send("-loop")
    if message.content.startswith("$inspire"):
        quote = get_quote()
        channel2 = client.get_channel(865425426465816630)
        await channel2.send(quote)


client.run(os.getenv("TOKEN"))
