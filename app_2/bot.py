import requests
import misc
import json
import Kurs
import os
from time import sleep
import base64
from base64 import b64encode

#import sys
#sys.path.insert(0, 'D:/Diploma/flask/app')

import block
import telebot
#blockchain_dir = 'D:/Diploma/flask/app/blockchain'


token = misc.token
kurs = Kurs.convertaciya()
bot = telebot.TeleBot(token)
# https://api.telegram.org/bot875513562:AAGQAocMJ5JeYtk9RlrPS4R94HSGpWWQYe0/sendmessage?chat_id=355479683&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'


global last_update_id
last_update_id = 0


#ipd = bot.get_updates()
#last_ipd = ipd[-1]

#print (last_ipd.message)


def get_updates():
	url = URL + 'getupdates?offset=-1'
	r = requests.get(url)
	return r.json()





def get_message():
	data = get_updates()

	current_update_id = data['result'][-1]['update_id']

	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id

		chat_id = data['result'][-1]['message']['chat']['id']
		message_text = data['result'][-1]['message']['text']
	
		message = {'chat_id': chat_id,
	           'text': message_text}

		return message
	return None

def send_message(chat_id,text='Wait a second, please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
	requests.get(url)


def kluch(key):
	answer1 = get_message()
	chat_id = answer1['chat_id']
	send_message(chat_id,key)
	#main() 																# ne proveril ewe na cicl


def send_image(razshirenie,chat_id):
	
	file = open('D:/Diploma/flask — копия/app_2/outputs/output.' + razshirenie,'rb')	
	if razshirenie == 'JPG' or razshirenie == 'jpg':
		bot.send_chat_action(chat_id, 'upload_photo')
		bot.send_photo(chat_id, file)
		file.close()
	if razshirenie == 'mp4':
		bot.send_chat_action(chat_id, 'upload_video')
		bot.send_video(chat_id, file)
		file.close()
	if razshirenie == 'mp3':
		bot.send_chat_action(chat_id, 'upload_audio')
		bot.send_audio(chat_id, file)
		print("zawel")
		file.close()
	if razshirenie == 'doc' or razshirenie == 'txt':
		bot.send_chat_action(chat_id, 'upload_document')
		bot.send_document(chat_id, file)
		file.close()

def main():
	# d = get_updates()
		
	# with open('updates.json', 'w') as file:
	# 	json.dump(d, file, indent=2, ensure_ascii=False)
	while True:
		answer = get_message()
		print(answer)
		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']

			if 'kurs' in text:
				send_message(chat_id,kurs)
			if 'integrity' in text:
				send_message(chat_id,block.check_integrity())
			if 'decrypt' in text:
				b = text.split("Л")
				#block_number = b[1]
				#private_key = b[2]
				#y=block.rsa_decrypt(b[1],b[2])
				key = b[1]
				safe_number = b[2]
				razshireni = b[3]
				print(key)
				#key = base64.b64decode(key)
				y = block.aes_decrypt(key,safe_number,razshireni)
				#send_message(chat_id,y)
				send_image(razshireni,chat_id)
				

				
		else:
			continue
		sleep(2)


if __name__ == '__main__':
	main()
