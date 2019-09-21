import requests
import json

def get_currency():
	URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
	data = requests.get(URL)
	return data.json()

def convertaciya():	
	data = get_currency()
	Rub = data['Valute']['KZT']['Value']
	Rub_prev = data['Valute']['KZT']['Previous']

	Usd = data['Valute']['USD']['Value']
	Usd_prev = data['Valute']['USD']['Value']

	curs = {'RUB_segodnya': 100/Rub,
   			'RUB_vchera': 100/Rub_prev,
   			'USD_segodnya': Usd * 100/Rub,
   			'USD_vchera': Usd_prev * 100/Rub}

	return curs
	

if __name__ == '__main__':
	# print(get_currency())
	print(convertaciya())
	# d = get_currency()
	# with open('kurs.json', 'w') as file:
	# 	json.dump(d, file, indent=2, ensure_ascii=False)
