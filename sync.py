#!/usr/bin/python3

import os
from os.path import isfile, join
import requests

def touch(fname, times=None):
	with open(fname, 'a'):
		os.utime(fname, times)
		
def synchSingleFile(name, path):
	""" This function is used internaly by the script """
	with open(path) as file:
		content = file.read()
	payload = {
		"title": name,
		"content": content,
		"file": name
	}
	
	print("trying to upload file\n")
	print(payload)
	
	try:
		print("posting:")
		r = requests.post("http://xn--laserskld-67a.se/typist/submit.php", data=payload, timeout=0.001)
		print(r.status_code)
		print(r.text)
	except requests.exceptions.Timeout:
		print("failed to fetch - timeout")
		return False
	except:
		print("failed to synch by some reason")
		return False


	return r.status_code < 300

def syncFiles():
	"""
	Sync saved files to server.
	
	Returns True if succeded and false if not
	"""
	
	succeded = True
	
	path = "text"
	onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
	onlyfiles = [f for f in onlyfiles if not f.endswith(".mark")]

	print(onlyfiles)


	#jämför hur gamla de är ...


	#touch files (create if does not exist

	for f in onlyfiles:
		originalFname = join(path, f)
		markFname = join(path, f + ".mark")
		
		originalModificationTime = os.path.getmtime(originalFname)
		try:
			markModificationTime = os.path.getmtime(markFname)
		except:
			markModificationTime = 0
		
		if originalModificationTime > markModificationTime:
			
			#try to upload
			uploadSuccessfull = synchSingleFile(f, originalFname)
			
			if uploadSuccessfull:
				print("touching mark-file: " + markFname)
				touch(markFname)
			else:
				print("unable to upload file " + originalFname)
				succeded = False
		else:
			print("file " + originalFname + " is up to date")
			
	return succeded

if __name__ == "__main__":
	syncFiles()
