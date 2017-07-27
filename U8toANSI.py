#Implement a Script to convert UTF-8 to ANSI for .c or .h files from one dir to another dir
#For other types file just do copy

import sys 
import os
import codecs
import shutil

def handle(srcpath,dstpath):
	files = os.listdir(srcpath)
	for file in files:
		filenew = srcpath + "\\" + file
		if os.path.isfile(filenew):
			type = os.path.splitext(file)[1] 
			if type == ".c" or type == ".h":
				f = codecs.open(filenew,"r",encoding="utf-8")
				content = f.read()
				f.close()
				
				out = codecs.open(dstpath + "\\" + file, "w",encoding="ANSI",errors="ignore")

				out.write(content)
				out.close()	
				print("1")
			else:
				shutil.copyfile(filenew,dstpath + "\\" + file)
		else：#os.path.isdir(filenew):
			newsrcpath = srcpath + "\\" + file
			newdstpath = dstpath + "\\" + file
			os.mkdir(newdstpath)
			handle(newsrcpath,newdstpath)

path = "E:\\redis-3.0-annotated-unstable\\redis-3.0-annotated-unstable"
outpath = "F:\\redis-3.0"

handle(path,outpath)