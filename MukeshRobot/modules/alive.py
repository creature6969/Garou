import random
import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

MISHI = [
    "https://telegra.ph/file/a6eb2b23be4c3cef35c11.jpg",
    "https://telegra.ph/file/3702165c22d86a82c7a48.jpg",
    "https://telegra.ph/file/da4d6b57323c9422e7e57.jpg",
    "https://telegra.ph/file/5d89804de9cb9c2d255e4.jpg",
    "https://telegra.ph/file/d306bf2bf0dfd62dd4c55.jpg",
    "https://telegra.ph/file/c537865e47c371727d3f4.jpg",
    "https://telegra.ph/file/f6a0674f2d4881c92a706.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/garou_updates"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("❤️‍🔥")
    await asyncio.sleep(0.2)
    await accha.edit("🧪")
    await asyncio.sleep(0.1)
    await accha.edit("☠")
    await asyncio.sleep(0.1)
    await accha.edit("🔥")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAx0CfsWUawACRr1l7DNUKm1rxM2BcEkwmNphj0zkMAACTQsAAvc0UFcWmsYXLSnwlDQE"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        random.choice(MISHI),
        caption=f"""** ✦ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}](f"t.me/{BOT_USERNAME}") ✦**\n\n❍ **ʟɪʙʀᴀʀʏ ➛** `{lver}`\n❍ **ᴛᴇʟᴇᴛʜᴏɴ ➛** `{tver}`\n❍ **ᴘʏʀᴏɢʀᴀᴍ ➛** `{pver}`\n❍ **ᴘʏᴛʜᴏɴ ➛** `{pyver()}`\n\n❍ **ᴍᴀᴅᴇ ʙʏ ➛** [ɢᴀʀᴏᴜ-sᴜᴘᴘᴏʀᴛ](https://t.me/Garou_Support_Chat)""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
    
__mod_name__ = "ᴀʟɪᴠᴇ"
__help__ = """
 ❍ /alive ➛ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ sᴛᴀᴛᴜs.
 ❍ /ping ➛ ᴄʜᴋ ᴘɪɴɢ sᴛᴀᴛᴜs.
 ❍ /pingall ➛ ᴄʜᴋ ᴘɪɴɢ sᴛᴀᴛᴜs ᴏғ ᴀʟʟ ᴍᴏᴅᴜʟᴇs.
 """
    
