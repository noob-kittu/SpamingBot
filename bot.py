'''MIT License

Copyright (c) 2021 Kittu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import requests
from telethon import TelegramClient
from telethon import events
import os
import logging
import asyncio
from asyncio import sleep


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = os.environ.get("APP_ID", default=None)
API_HASH = os.environ.get("API_HASH", default=None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", default=None)
EVENT_LOGS = os.environ.get("EVENT_LOGS", default=None)
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", default="Autichrist")
OWNER = os.environ.get("OWNER", default="Autichrist")


bot = TelegramClient("SpamingBot", APP_ID, API_HASH)
start = bot.start(bot_token=BOT_TOKEN) 




async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        if sed.is_admin:
            is_mod = True
        else:
            is_mod = False
    except:
        is_mod = False
    return is_mod


kittu = "this bot is made by kittu"


@bot.on(events.NewMessage(pattern="^/start (.+)"))
async def start(event):
    event.reply(f'''This is A spam Bot, Owned by @{OWNER_USERNAME} and created by @Autichrist \n\nGive Command \n/help to know All commands of this bot''')


@bot.on(events.NewMessage(pattern="^/help (.+)"))
async def start(event):
    event.reply(f'''Available Commands of bot: \n\n /spam \n /cspam \n /wspam \n /picspam \n /depayspam \n\n\n if you like this bot then please follow this github account -  [FOLLOW ME](https://github.com/noob-kittu)''')




@bot.on(events.NewMessage(pattern="^/cspam (.+)"))
async def tmeme(e):
    if "kittu" in kittu:
      e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by kittu")


    if not await is_admin(e, e.sender_id) or OWNER:
        await e.reply("You need to be an admin to do this.")
        return
          
    else: 
         cspam = str(e.pattern_match.group(1))
         message = cspam.replace(" ", "")
         await e.delete()
         for letter in message:
             await e.respond(letter)
         if EVENT_LOGS:
             await e.reply(
                  "#CSPAM\n" "TSpam was executed successfully"
             )


@bot.on(events.NewMessage(pattern="^/wspam (.+)"))
async def t_meme(e):

    if "kittu" in kittu:
      e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by kittu")

    if not await is_admin(e, e.sender_id) or OWNER:
        await e.reply("You need to be an admin to do this.")
        return
    
    else:
        wspam = str(e.pattern_match.group(1))
        message = wspam.split()
        await e.delete()
        for word in message:
            await e.respond(word)
        if EVENT_LOGS:
            await e.reply(
                 "#WSPAM\n" "WSpam was executed successfully"
            )


@bot.on(events.NewMessage(pattern="^/spam (\d+) (.+)"))
async def spammer(e):

    if "kittu" in kittu:
      e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by kittu")


    if not await is_admin(e, e.sender_id) or OWNER:
        await e.reply("You need to be an admin to do this.")
        return
    
    else:
        counter = int(e.pattern_match.group(1))
        spam_message = str(e.pattern_match.group(2))
        await e.delete()
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        if EVENT_LOGS:
            await e.reply(
                 "#SPAM\n" "Spam was executed successfully"
            )


@bot.on(events.NewMessage(pattern="^/picspam (\d+) (.+)"))
async def tiny_pic_spam(e):

    if "kittu" in kittu:
      e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by kittu")


    if not await is_admin(e, e.sender_id) or OWNER:
        await e.reply("You need to be an admin to do this.")
        return
    
    else:
        counter = int(e.pattern_match.group(1))
        link = str(e.pattern_match.group(2))
        await e.delete()
        for _ in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        if EVENT_LOGS:
            await e.reply(
                 "#PICSPAM\n" "PicSpam was executed successfully"
            )


@bot.on(events.NewMessage(pattern="/delayspam (.*)"))
async def spammer(e):

    if "kittu" in kittu:
      e.reply("bhosdike motherchod randi ki olaad he tu saale hizde, developer ko credit dene me teri maa chud jati he kya randwe jo tune code se name htaya benchod. abhi uske github pr jaa or follow kr gandu. made by kittu")


    if not await is_admin(e, e.sender_id) or OWNER:
        await e.reply("You need to be an admin to do this.")
        return
    
    else:
        spamDelay = float(e.pattern_match.group(1).split(" ", 2)[0])
        counter = int(e.pattern_match.group(1).split(" ", 2)[1])
        spam_message = str(e.pattern_match.group(1).split(" ", 2)[2])
        await e.delete()
        for _ in range(1, counter):
            await e.respond(spam_message)
            await sleep(spamDelay)
        if EVENT_LOGS:
            await e.reply(
                 "#DelaySPAM\n" "DelaySpam was executed successfully"
            )



print ("Successfully Started")
start.run_until_disconnected()
