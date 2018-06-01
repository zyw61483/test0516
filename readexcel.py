#! usr/bin/python3
import threading
import time
import requests
import xlrd
import re
import os
import pathlib


class MyThread(threading.Thread):
	def __init__(self,fileName,fileUrl,mycookie):
		threading.Thread.__init__(self)
		self.fileName = fileName
		self.fileUrl = fileUrl
		self.mycookie = mycookie
	def run(self):
		self.doSth()	
	def doSth(self):
		r = requests.get(self.fileUrl,cookies = self.mycookie) 
		with open(self.fileName, "wb") as code:
			code.write(r.content)

def getResultOth(filename,key):
	f = open("tar\\oth\\"+filename, 'r',encoding='UTF-8')
	w = open("result.txt",'a')
	# flag = True
	for line in f:
		if (key in line) & ("翼支付（直销银行）请求参数，req=" in line):
			# print(line)
			result = line[line.index("翼支付（直销银行）请求参数，req=")+18:]
			w.write(key+"\t"+str(result))
			print(str(result))
			# flag = False
			return False
	f.close()
	w.close()		
	return True	
	
def getResult(filename,key):
	# print("fileName:"+filename+" key:"+key)
	f = open(filename, 'r',encoding='UTF-8')
	w = open("result.txt",'a')
	flag = True
	for line in f:
		if (key in line) & ("翼支付（直销银行）请求参数，req=" in line):
			# print(line)
			result = line[line.index("翼支付（直销银行）请求参数，req=")+18:]
			w.write(key+"\t"+str(result))
			print(str(result))
			flag = False
			break
		
	if flag:
		flag = getResultOth(filename[4:],key)	
	
	if flag :
		w.write(key+"\t\n")
		print(key)
	f.close()
	w.close()
				
mycookie = {"session":".eJxNkD1uwzAMhe_C2Sj0T8lT1y49gRbGohsDtR3EEdI6yN1DBW3RhQAfH79H8AZ14zP0Nxjqdnkr0BuVtLKug8InOl9mXp6yiFH_F99pZughV2815uqYhlyTLjrXiLHkGkxUUtGMuSIPDjrgmaZPWdqPtH5PV55e9-O6fNDyMqyzzCcJ0ioo7TtYfvmxoJdqkIRjicW3rDK57krZpIz0J6E0s5ZbtEvJqpa28dcTgN5iaxsdgh9DcI5ToOQw8sGR9Sb56HBMhawY20d-0v8Ohfv9ASpEWKs.DeaRSA.NCwTUPyzSn-Ci9sxHk2zA8FmfzU"}
xlsfile = r"C:\Users\zhaoyiwei\Desktop\超时还款记录.xlsx"
book = xlrd.open_workbook(xlsfile)
sheet0 = book.sheet_by_index(0)
col_data = sheet0.col_values(0)
fileRecord = []
dict = {'20180520.tar.gz':'za-telecom-business-ss_regular_app_business_lt_info-2018-05-20.log',\
'20180525.tar.gz':'za-telecom-business-ss_regular_app_business_lt_info-2018-05-25.log',\
'20180526.tar.gz':'za-telecom-business-ss_regular_app_business_lt_info-2018-05-26.log',\
'20180527.tar.gz':'za-telecom-business-ss_regular_app_business_lt_info-2018-05-27.log',\
'20180528.tar.gz':'za-telecom-business-ss_regular_app_business_lt_info-2018-05-28.log',\
'20180524.tar.gz':'za-telecom-business-ss_regular_app_business_lt_info-2018-05-24.log'}
for i in col_data:
	tarfilename = "20"+i[17:23]+".tar.gz"
	path = pathlib.Path(tarfilename)
			
	if  path.is_file():
		print("存在"+tarfilename)
		getResult("tar\\"+dict.get(tarfilename),i)
	elif tarfilename not in fileRecord:
		fileRecord.append(tarfilename)
		print(i+" 不存在"+tarfilename)
		# url_file1 = 'https://gayway.zhonganonline.com/download/?host=10.139.97.231&path=/home/zhaoyiwei/za-telecom-business/'+tarfilename+'&user=zhaoyiwei&id_rsa=false'
		url_file1 = 'https://gayway.zhonganonline.com/download/?host=10.253.1.105&path=/home/zhaoyiwei/za-telecom-business/'+tarfilename+'&user=zhaoyiwei&id_rsa=false'
		t1 = MyThread(tarfilename,url_file1,mycookie)
		t1.start()	
	
	