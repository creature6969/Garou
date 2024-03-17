import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from MukeshRobot import pbot, dispatcher, telethn
from pyrogram import filters

JOKE_API_ENDPOINT = 'https://v2.jokeapi.dev/joke/Dark?format=txt&amount=1'

def get_joke():
    response = requests.get(JOKE_API_ENDPOINT)
    return response.text

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke_text = get_joke()
    await update.message.reply_text(joke_text)

JOKE_HANDLER = CommandHandler("joke", joke, block=False)
telethn.add_handler(JOKE_HANDLER)
