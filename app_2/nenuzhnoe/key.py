
import rsa
file=input("Write the filename: ")
with open(file,"rb") as r:
	read=r.read()
	message=rsa.decrypt(read,rsa.PrivateKey(94604863104722737306105372654805597781667023433554416714187857570254400471119334786039205181993190690120946746589392178505292417317436341856410407878686255498813657326044408293735764711233636219243341831840523770545163654085285165314781570676096374993953010209488501581022702770952779109756569982383039121593, 65537, 44136040548497759939182015791395412548247085485770271618113336667997135883614960420573854440078761697216045085630569996456952800089729712258109881290699752771375189512484144933387294786923432518523662070631252062648718546570640215058921177758789035217631297481449395499148172099859080882297574435509515469773, 30441283485347460725515738660275572102576666010670446900856103513474376521955600248434430499541835885679670873131864995746644573828591489610497053536153998698731607, 3107781679122026192356951893840980079859695788172544469420918395757071803951104225184250049548236831298425322995032824915668037910826585906527599))
	print("\n[*] Decrypted text:\n\n[text] << "+str(message.decode("utf8"))+"\n")
