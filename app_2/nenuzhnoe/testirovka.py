import os
import rsa


def main():
	blockchain_dir = os.curdir + '/blockchain/'

	with open(blockchain_dir + "67","rb") as r:
		wordlist = [line.split(None, 1)[0] for line in r]
		mylist = list(r)
		#read=mylist.split('\r\n')
		print (wordlist)
		a = str(wordlist)
		b = a.encode("utf8")
		c = "b'\x16\x8a\xc2p-%\x89\xfcY\x9f\xcf5\xae \xafgO\x1f\xc9L-\x95\xb7\xf5\xe9\x14\x96\x14^\xb2J\xae\xed\xd6\xf2.\x90>s\xb2\x12\\\n51\xf6*\x1b\x1e\xd4j\x0b\xfd\x87\xd4\x1a<\xd5\xc1\xae\x9d\xcc\xa9\xec'"
		c = c.encode("utf8")
		message=rsa.decrypt(c,rsa.PrivateKey(11161127976793463098341893290626853111828288796960003059775998828936413339680857526594375117822045490516072178963109459059194792164537057451958871220501073, 65537, 4432979251963529677126500791232692776613063725603382511344267353055752308636977277361548560146607292953090160750601911697562179782865429799325031200460793, 6943954727198207710200782297906596283717643403536093640058132931625306505809978807, 1607315775415031838085208900811651323025093753857089808778693680439926839))
		return str(message.decode("utf8"))





if __name__ == '__main__':
	main()