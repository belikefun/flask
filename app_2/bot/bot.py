import requests
import misc
import json
import Kurs
import os

import sys
sys.path.insert(0, 'D:/Diploma/flask/app')

import block

blockchain_dir = 'D:/Diploma/flask/app/blockchain'


token = misc.token
kurs = Kurs.convertaciya()
# https://api.telegram.org/bot875513562:AAGQAocMJ5JeYtk9RlrPS4R94HSGpWWQYe0/sendmessage?chat_id=355479683&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'





def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()





def get_message():
	data = get_updates()

	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']
	
	message = {'chat_id': chat_id,
	           'text': message_text}

	return message


def send_message(chat_id,text='Wait a second, please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
	requests.get(url)


def main():
	# d = get_updates()
		
	# with open('updates.json', 'w') as file:
	# 	json.dump(d, file, indent=2, ensure_ascii=False)
	answer = get_message()
	chat_id = answer['chat_id']
	text = answer['text']

	if 'kurs' in text:
		send_message(chat_id,kurs)
	if 'integrity' in text:
		send_message(chat_id,block.check_integrity())



if __name__ == '__main__':
	main()
