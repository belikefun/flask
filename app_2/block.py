import json
import os, random
import hashlib
import rsa
from main import *
import bot
import pyAesCrypt
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
from base64 import b64encode
import base64
import codecs
import Starter
blockchain_dir = os.curdir + '/blockchain/'
i = 0

def privatnui_kluch_useru(priv):
	global i
	if i==0:
		priv_key = priv
		i = i+1
	if priv!=0:
		return (priv_key)

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
def aes_encrypt(filename,razshirenie):
	#file=filee
	#password="abat"
	#bufferSize = 64*1024*1024
	#return (pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize))
	"""
	key = Random.new().read(AES.block_size)
	iv = Random.new().read(AES.block_size)
	image_dir = os.curdir + '/images/' + filee
	input_file = open(image_dir)
	input_data = input_file.read()
	input_file.close()

	cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
	enc_data = cfb_cipher.encrypt(input_data)

	enc_file = open("encrypted.enc", "w")
	enc_file.write(enc_data)
	enc_file.close()
	"""
	"""
	key = Random.new().read(AES.block_size)
	image_dir = os.curdir + '/images/'
	chunk_size = 64*1024
	output_file = filename+".enc"
	file_size = str(os.path.getsize(image_dir + filename)).zfill(16)
	IV = ''
	for i in range(16):
		IV += chr(random.randint(0, 0xFF))
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	with open(image_dir + filename, 'rb') as inputfile:
		with open(image_dir + output_file, 'wb') as outf:
			outf.write(file_size)
			outf.write(IV)
			while True:
				chunk = inputfile.read(chunk_size)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' '*(16 - len(chunk)%16)
				outf.write(encryptor.encrypt(chunk))
	"""
	image_dir = os.curdir + '/images/'
	input_file = open(image_dir + filename, "rb")
	input_data = input_file.read()
	input_file.close()

	key = Random.new().read(AES.block_size)
	#iv = Random.new().read(AES.block_size)
	iv = b'\x83|E\xf8\x0e\xdb\xd9\x9e\xdd-*\xbe\xba\xe4\xfe\xaf'
	#String encodedKey = Base64.getEncoder().encodeToString(key.getEncoded())
	#String encodediv = Base64.getEncoder().encodeToString(iv.getEncoded())
	encoded_key = str(base64.b64encode(key),'utf-8')
	
	
	cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
	enc_data = cfb_cipher.encrypt(input_data)


	files = get_files2() 
	prev_file = files[-2]
	filename1 = str(prev_file + 1)
	prev_hash = get_hash2(str(prev_file))
	bot.kluch("decryptЛ" + encoded_key + "Л" + filename1 + "Л" + str(razshirenie))
	with open(image_dir + filename, 'w') as file:
		file.write(str(base64.b64encode(enc_data), 'utf-8'))
		file.write("&")
		file.write(prev_hash)

	#google drive
	Starter.uploadFile(filename1,image_dir + filename1,'image/jpeg')




#	enc_file = open(image_dir + filename, "wb")
#	enc_file.write(enc_data)
#	enc_file.close()

def aes_decrypt(key,filename,razshirenie):
	"""
	image_dir = os.curdir + '/images/' + filee + "encrypted.enc"
	enc_file2 = open(image_dir)
	enc_data2 = enc_file2.read()
	enc_file2.close()

	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(enc_data2)

	output_file = open("output.jpg", "w")
	output_file.write(plain_data)
	output_file.close()
	"""
	image_dir = os.curdir + '/images/'
	key = base64.b64decode(key)
	iv = b'\x83|E\xf8\x0e\xdb\xd9\x9e\xdd-*\xbe\xba\xe4\xfe\xaf'
	#key = base64.b64decode(key)
	#iv = base64.b64decode(iv)
	
	#key = key.encode('utf-8')
	#iv = iv.encode('utf-8')
	

	enc_file2 = open(image_dir + filename, "r")
	enc_data2 = enc_file2.read()
	enc_file2.close()
	#key = b'\x82\xea\xb0\xa4\x89\xa7\xaai\x1e16\xd7\x1e9\xc8\xde'
	#iv = b'\x08N\x1e\x1e\xdf4\xcf\xe4\x91\xab[a\xbd\x05\xd3-'
	posle_chteniya = enc_data2.split("&")
	informaciya = base64.b64decode(posle_chteniya[0])
	hashFunk = posle_chteniya[1]

	cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
	plain_data = cfb_decipher.decrypt(informaciya)
	#plain_data = cfb_decipher.decrypt(enc_data2)
	#output_file = open(image_dir + "output.jpg", "wb")
	output_file = open(os.curdir + '/outputs/output.' + razshirenie, "wb")
	output_file.write(plain_data)
	output_file.close()
	#bot.send_image(image_dir + "output.jpg")


def rsa_encrypt(clean):
	(pubkey,priv) = rsa.newkeys(512)


	a = str(pubkey)
	a = a.split("(")						#vitaskivayu tolko kluch is classa rsa public key
	a = a[1].split(",")
	d = " "
	d = a[0]								# "d" ato u nas chistui kluch, bez 65537 vkonce
	pub_key = int(d)

	message = clean.encode("utf8")

	crypto=rsa.encrypt(message,rsa.PublicKey(pub_key, 65537))
	#crypto = rsa.encrypt(message, pubkey)

	#b = str(priv)
	#b = b.split("(")						#vitaskivayu tolko kluch is classa rsa private key
	#b = b[1].split(")")
	#c = " "
	#c = b[0]								# "c" ato u nas chistui kluch private
	#privatnui_kluch_useru(str(priv))
	bot.kluch(priv)
	return crypto
	
def rsa_decrypt(block_number,private):
	block_number = str(block_number)
	with open(blockchain_dir + block_number,"rb") as r:
		"""
		mylist = list(r)
			#read=mylist.split('\r\n')
		print("\n")
		print (mylist[0])
		h = privatnui_kluch_useru(0)
		print("\n")
		print("a")
		print("\n")
		print (h)
		"""

		b = str(private)
		b = b.split("(")						#vitaskivayu tolko kluch is classa rsa private key
		b = b[1].split(")")
		c = " "
		c = b[0]								# "c" ato u nas chistui kluch private
		print("\n")
		print (c)

		d=c.split(",")
		key = [0,0,0,0,0,0,0]
		key[0]=int(d[0])
		f=d[1].split(" ")
		key[1]=f[1]
		f=d[2].split(" ")						# razdelil kluch. Key ato massig a e g f kluchei
		key[2]=f[1]
		f=d[3].split(" ")
		key[3]=f[1]
		f=d[4].split(" ")
		key[4]=f[1]

		#message=rsa.decrypt(mylist[0], rsa.h)
		#return (str(message.decode("utf8")))
		
		read=r.readlines() #read[0] ato shifrovannui text
		
		

		message=rsa.decrypt(read[0],rsa.PrivateKey(int(key[0]), int(key[1]), int(key[2]), int(key[3]), int(key[4])))
		return (str(message.decode("utf8")))
	





def get_hash(filename):
	blockchain_dir = os.curdir + '/blockchain/'
	file = open(blockchain_dir + filename, 'rb').read()

	return hashlib.md5(file).hexdigest()
def get_hash2(filename):
	image_dir = os.curdir + '/images/'
	file = open(image_dir + filename, 'rb').read()

	return hashlib.md5(file).hexdigest()


def get_files():
	files = os.listdir(blockchain_dir)
	return sorted([int(i) for i in files])
def get_files2():
	image_dir = os.curdir + '/images/'
	files = os.listdir(image_dir)
	return sorted([int(i) for i in files])

def check_integrity():
	# schitat pred block
	# vichislit pred block
	# sravnit
	image_dir = os.curdir + '/images/'
	#blockchain_dir = os.curdir + '/blockchain/'
	
	files = get_files2()

	results = []

	for file in files[1:]:
		f = open(image_dir + str(file), 'r')
		chtenie = f.read()
		h = chtenie.split("&")
		informaciya = h[0]
		hashFunk = h[1]


		#print (h[1])
		#	h = json.load(f)['hash']

		prev_file = str(file - 1)
		actual_hash = get_hash2(prev_file)


		if h[1] == actual_hash:
			res = 'OK'
		else:
			res = 'Corrupted'
		#print('block {} is: {}'.format(prev_file, res))
		results.append({'block': prev_file, 'result': res})

	return results

def write_block(name, prev_hash=''):
	
	blockchain_dir = os.curdir + '/blockchain/'
	files = get_files()
	 
	
	prev_file = files[-1]

	filename = str(prev_file + 1)

	prev_hash = get_hash(str(prev_file))
	print(name)
	#data = str(rsa_encrypt(name))   rsa
	data = aes_encrypt(name)

	with open(blockchain_dir + filename, 'w') as file:
		file.write(data + "\n")
		file.write(prev_hash)


def main():
	#write_block(data1='katja')
	#rsa_decrypt("92",1)
	#print(check_integrity())
	#print(rsa_decrypt("59",priv_key))
	print("Hi")

if __name__ == '__main__':
	main()