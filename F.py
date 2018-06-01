#! usr/bin/python3
import threading
import time
import requests
import xlrd
import re
import os
import pathlib
import ExcelUtil
# from ExcelUtil import getColDate
# from Demo import MyThread2

dict={\
'20180520':[\
'tar\\a\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-20.log',\
'tar\\b\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-20.log'],\
'20180524':[\
'tar\\a\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-24.log',\
'tar\\b\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-24.log'],\
'20180525':[\
'tar\\a\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-25.log',\
'tar\\b\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-25.log',\
'tar\\c\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-25.log',\
'tar\\d\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-25.log',\
'tar\\e\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-25.log',\
'tar\\f\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-25.log'],\
'20180526':[\
'tar\\a\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-26.log',\
'tar\\b\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-26.log',\
'tar\\c\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-26.log',\
'tar\\d\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-26.log',\
'tar\\f\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-26.log',\
'tar\\e\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-26.log'],\
'20180527':[\
'tar\\a\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-27.log',\
'tar\\b\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-27.log',\
'tar\\c\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-27.log',\
'tar\\d\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-27.log',\
'tar\\f\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-27.log',\
'tar\\e\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-27.log'],\
'20180528':[\
'tar\\a\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-28.log',\
'tar\\d\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-28.log',\
'tar\\f\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-28.log',\
'tar\\e\\za-telecom-business-ss_regular_app_business_lt_info-2018-05-28.log']
}

class MyThread2(threading.Thread):
	def __init__(self,keys):
		threading.Thread.__init__(self)
		self.keys = keys
		
	def run(self):
		for key in self.keys :
			print(key)
			fileflag = self.getFileFlag(key)
			for file in dict[fileflag]:
				if self.doSth(fileflag,file,key) :
					break
	
	def getFileFlag(self,key):
		name = "20"+key[17:23]
		# print(name)
		return name
		
	def doSth(self,fileflag,file,key):
		self.mkdir(fileflag)
		with open(fileflag+"/result"+fileflag+".txt",'a+') as w:
			with open(file, 'r', encoding='UTF-8') as f:
				for line in f:
					if (key in line) & ("翼支付（直销银行）请求参数，req=" in line):
						result = line[line.index("翼支付（直销银行）请求参数，req=")+18:]
						w.write(key+"\t"+str(result))
						print(str(result))
						return True
				return False
	def mkdir(self,path):  
		folder = os.path.exists(path)  
		if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹  
			os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径  
			print("---  new folder...  ---")  
			print("---  OK  ---")
		else:  
			print("---  There is this folder!  ---")

def splitKeys(begin,end,keys):
	temp = []
	# print("begin:"+str(begin)+"end:"+str(end))
	if begin >len(keys):
		return True,temp
	if end > len(keys):
		temp = keys[begin:]
	else :
		temp = keys[begin:end]
	return False,temp


def go(keys):
	begin = 0
	end = 17
	while True :
		flag,temp = splitKeys(begin,end,keys)
		if flag :
			break
		t1 = MyThread2(temp)
		t1.start()
		begin=end
		end=end+17
		

def handelKeys(keys):
	dictkey = {'20180520':[],'20180524':[],'20180525':[],'20180526':[],'20180527':[],'20180528':[]}
	for key in keys :
		templist = dictkey["20"+key[17:23]]
		templist.append(key)
	for i in dictkey:
		t1 = MyThread2(dictkey[i])
		t1.start()
	
keys = ExcelUtil.getColDate(r"C:\Users\zhaoyiwei\Desktop\超时还款记录1.xlsx")
handelKeys(keys)

	
