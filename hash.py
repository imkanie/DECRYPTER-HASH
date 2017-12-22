#!/usr/bin/python
#coding: utf-8

import requests #pip install requests
import sys
import re

url = 'http://hashtoolkit.com/reverse-hash/?hash='
try:
	hasH = sys.argv[1]
except:
	print("Use: python "+sys.argv[0]+" hash")
	sys.exit()
http = requests.get(url+hasH)
content = http.content
cracked = re.findall("<span title=\"decrypted (md5|sha1|sha256|sha384|sha512) hash\">(.*)</span>", content)
print ("\n\tHash: "+cracked[0][0])
print ("\tSenha Encontrada: "+cracked[0][1])