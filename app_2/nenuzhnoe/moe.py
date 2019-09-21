import io
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode
import rsa
import base64

input_file = open("77.JPG", "rb")
input_data = input_file.read()
input_file.close()

key = Random.new().read(AES.block_size)
print(key)
print(str(key))
#a = key.decode('utf8')
a = str(base64.b64encode(key),'utf-8')
print(a)


b = base64.b64decode(a)
print(b)
iv = Random.new().read(AES.block_size)
print(iv)

"""
cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
enc_data = cfb_cipher.encrypt(input_data)

enc_file = open("encrypted.enc", "wb")
enc_file.write(enc_data)
enc_file.close()


input_data = bytearray(input_data)
key = 48
for index , value in enumerate(input_data):
	input_data[index] = value^key
fo = open("enc.jpg" , "wb")
fo.write(input_data)
fo.close()
 ####


enc_file2 = open("encrypted.enc", "rb")
enc_data2 = enc_file2.read()
enc_file2.close()
key = b"\x14u=\x11\xbb'\x08S\x153\xf1\\\x97|3I"
iv = b'\x18\x9f\xd3|\xa2\xc3\xe5\x9a\xaa\xa8\xdc\xcf\xbaC\x02\xd8'
key=str(key)
iv=str(iv)
cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
plain_data = cfb_decipher.decrypt(enc_data2.encode("utf8"))

output_file = open("output.jpg", "wb")
output_file.write(plain_data)
output_file.close()
"""




