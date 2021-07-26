import os
import discord
import requests
import json
import datetime
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


def weeks_until(year, month, day):
    start_date = datetime.date.today()
    end_date = datetime.date(year, month, day)

    weeks = ((end_date - start_date).days // 7)

    return weeks


def semester_weeks():
    week_number = 13 - weeks_until(2021, 10, 24)

    return "This week is Week " + str(week_number) + ". Check the assessments page to what due dates are coming up " \
                                                     "and organise weekly to-do list!! "


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$earrape"):
        payload1 = {
            'content': "-clear"
        }
        payload2 = {
            'content': "-p https://www.youtube.com/watch?v=FfWoHZFci0g"
        }
        payload3 = {
            'content': "-loop"
        }
        header = {
            'authorization': os.getenv('AUTH')
        }

        r = requests.post("https://discord.com/api/v9/channels/750273754067763291/messages", data=payload1,
                          headers=header)
        r = requests.post("https://discord.com/api/v9/channels/750273754067763291/messages", data=payload2,
                          headers=header)
        r = requests.post("https://discord.com/api/v9/channels/750273754067763291/messages", data=payload3,
                          headers=header)

        # channel1 = client.get_channel(750273754067763291)
        # await channel1.send("-p https://www.youtube.com/watch?v=FfWoHZFci0g")
        # await channel1.send("-loop")
    if message.content.startswith("$inspire"):
        quote = get_quote()
        channel2 = client.get_channel(852750656501710870)
        await channel2.send(quote)
    if message.content.startswith("$insult"):
        insult = get_insult()
        await message.channel.send(insult)
    if message.content.startswith("$week"):
        week = semester_weeks()
        await message.channel.send(week)


client.run(os.getenv("TOKEN"))
