import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def  message(message):
    bot.send_message(message.chat.id,f"Hello , Send URL Of Video To download Him\n\nBy : @trprogram")

@bot.message_handler(func=lambda message: True)
def trakos(message):
    msg = message.text 
    url = f'https://hamod.ga/api/tiktokWithoutWaterMark.php?u={msg}'
    re = requests.get(url).json()
    d = re['link']
    bot.send_video(message.chat.id,d)
trakos()
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://botgiel10k.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
