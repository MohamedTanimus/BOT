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

sudo_id = "5384214726" #id

ch = '@Freeintrn' #cannel user
#user channel
tok = "5593144986:AAEYxTWwPUoCp4bzpO6yl49nbNlY3KW-Ay8"
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=["start"])
def start(message):
	frt=message.chat.first_name
	idd = message.from_user.id
	url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={ch}&user_id={idd}"
	req = requests.get(url)
	if idd == sudo_id or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
		star = types.InlineKeyboardButton(text='START🍁',callback_data='st')
		star1 = types.InlineKeyboardButton(text='PROGRAM 🧑‍💻',url='https://t.me/Freeintrn')
		button1 = types.InlineKeyboardMarkup()
		button1.row_width = 2
		button1.add(star,star1)
		bot.send_message(message.chat.id,text='''<strong> Welcome To Bot</strong>''',parse_mode="html",reply_markup=button1)
	else:
			star1 = types.InlineKeyboardButton(text='PROGRAM 🧑‍💻',url='https://t.me/Freeintrn')
			button12 = types.InlineKeyboardMarkup()
			button12.row_width = 2
			button12.add(star1)
			bot.send_message(message.chat.id,text=f'''<strong>Wellcome •{message.from_user.first_name}•
	🚸| sorry dear
🔰| You have to subscribe to the bot channel to be able to use it

- Channel ID: {ch}

‼️| Subscribe then send /start</strong>''',parse_mode="html",reply_markup=button12)
			
@bot.callback_query_handler(func=lambda call: True)

def qwrey_cal(call):
	if call.data =="st":
		start1(call.message)
	if call.data =="bot1":
		start2(call.message)
	if call.data =="bot2":
		start3(call.message)
def start1(message):
	buot1 = types.InlineKeyboardButton(text='SCRPIT PYTHON',callback_data='bot1')
	buot2 = types.InlineKeyboardButton(text='SCRPIT PHP',callback_data='bot2')
	can = types.InlineKeyboardMarkup()
	can.row_width = 1
	can.add(buot1,buot2)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>PLEASE CHOOSE LANGUAG SCRIPT</strong>  ",parse_mode="html",reply_markup=can)
#2
def start2(message):
	buot1 = types.InlineKeyboardButton(text='رشق نقاط أنستا اب',callback_data='bot1')
	buot2 = types.InlineKeyboardButton(text='فحص نقاط ',callback_data='bot2')
	can = types.InlineKeyboardMarkup()
	can.row_width = 1
	can.add(buot1,buot2)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong> PYTHONأختر الاسكربت الذي تريده</strong>  ",parse_mode="html",reply_markup=can)
#3
def start3(message):
	buot1 = types.InlineKeyboardButton(text='انشاء حسابات INSTAGRAM',callback_data='bot1')
	buot2 = types.InlineKeyboardButton(text='تجميع نقاط TepFollowers',callback_data='bot2')
	can = types.InlineKeyboardMarkup()
	can.row_width = 1
	can.add(buot1,buot2)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>أختر الاسكربت PHP</strong>  ",parse_mode="html",reply_markup=can)

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
