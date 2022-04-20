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


@bot.message_handler(commands=['start'])
def start(message):
	while True:
		try:
			request = requests.get('https://Vf10.moahmedsalah.repl.co?num=01022196853&pas=AnA@AnA1').json()
			getcard = request['card']
			getunits = request['units']
			getamoubt = request['amount']
			if '0'  in getcard[0]:
				pass
				time.sleep(35)
			else:
				if '0'  in getcard[0]:
					pass
					time.sleep(35)
				else:
					tele = (f"""عدد الوحدات: {getunits}\nالكارت: {getcard}\nقمية الكارت: {getamoubt}""")
					bot.send_message(message.chat.id,f"<strong>{tele}</strong>",parse_mode="html") 
					print(tele)
					time.sleep(35)
		except:print('Error Request Vodafone')
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://mdkkdkdkdkdkjd.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
