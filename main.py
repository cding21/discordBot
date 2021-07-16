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


def get_insult():
    request = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    json_data = request.json()
    insult = json_data["insult"]
    return insult


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$earrape"):
        channel1 = client.get_channel(750273754067763291)
        await channel1.send("-p https://www.youtube.com/watch?v=FfWoHZFci0g")
        await channel1.send("-loop")
    if message.content.startswith("$inspire"):
        quote = get_quote()
        channel2 = client.get_channel(852750656501710870)
        await channel2.send(quote)
    if message.content.startswith("$insult"):
        insult = get_insult()
        await message.channel.send(insult)


client.run(os.getenv("TOKEN"))
