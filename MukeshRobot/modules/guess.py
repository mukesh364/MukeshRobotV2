import random
from PIL import Image
from MukeshRobot import telethn as pbot
from telethon import events
@pbot.on(events.NewMessage(pattern="/guess ?(.*)"))
async def wish(e):

 if e.is_reply:
         mm = random.randint(1,100)
         lol = await e.get_reply_message()
         fire = "https://telegra.ph/file/3fe0f7dedb81528a57313.jpg"
         await pbot.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your Guess is {mm}%__**\n\n__Correct!!!", reply_to=lol)
 if not e.is_reply:
         mm = random.randint(1,100)
         fire = "https://telegra.ph/file/3fe0f7dedb81528a57313.jpg"
         await pbot.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your Guess is {mm}%__**\n\n__Correct!!!", reply_to=fire)
