import random
import asyncio
from pyrogram import filters
from MukeshRobot import pbot as MukeshRobot




wish_STRINGS = [
                     'Happy Rakshabandhan Day',
                     "Thanks for always being my pillar of strength. I am very blessed to have a brother like you. Happy Raksha Bandhan!",
                     "A very big thank you for being my companion, my protector and being equally weird with me. You are the best brother in this world. Happy Raksha Bandhan!",
                     "Happy Raksha Bandhan to my childhood leg-puller, my lovely brother, my guardian and the only person who knows me inside-out. \nThanks for always being there. Happy Raksha Bandhan bro!",
                     "I pray for your happiness, prosperity, and long life, sweetest brother. Sending loads of love and best wishes. Happy Raksha Bandhan.",
                     "You are the only person who supports me in my hard times; you are the one who shakes a leg with me in my happiness. There was no single day in my life when you weren't there. I really love you my big brother.",
                     "You supported me while I was in distress; you protected me when I was scared and all other things you did to make me happy. Thanks are just insufficient to express my gratitude. Happy Raksha Bandhan to you Brother!",
                     "Dearest sister, this Raksha Bandhan, I promise to always be your savior and will always be by your side no matter what. Sending loads of blessings and gifts just for you!",
                     "This holy thread you tie on my wrist will strengthen our bond more and fills my heart with more love for you.\n You are the best sis in the world!",
                     "Happy Raksha Bandhan!",
                     "May god bless my angelic sister with loads of happiness, health and success. Happy Raksha Bandhan.",
                     "I wait for the day throughout the year to see you tie a Rakhi so religiously on my wrist and pray to God for my well-being. Sweetest Sis, I wish our bond grows stronger day by day...",
                     "To have an affectionate relationship with a sister is not just to have a friend or a confidant -- it is to have a companion for life.",
                     "Dont wish to @itz_mst_boi .\n I already have my best sis (Swathi).",
                   ]


@MukeshRobot.on_message(filters.command("wish"))
async def lel(bot, message):
    ran = random.choice(wish_STRINGS)
    await bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)

__mod_name__ = "ʀᴀᴋʜɪ"

__help__ = """

ᴡɪsʜ ʟɪɴᴇ ʙᴀʙʏ
❍ /wish *:* ᴡɪsʜ ᴏɴ ғᴇsᴛɪᴠᴀʟ

 """
