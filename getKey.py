#! usr/bin/python3
import ExcelUtil
# from ExcelUtil import getColDate

xlsfile = r"C:\Users\zhaoyiwei\Desktop\超时还款记录1.xlsx"
list = ExcelUtil.getColDateBySICI(xlsfile,1,0)
mobile = []
with open("mobile.txt",'r') as r:
	for line in r:
		mobile.append(line)
	
for key in list:
	flag = False
	for temp in mobile :
		print(key.strip('\n')+"==="+temp.strip('\n'))
		if key.strip('\n') == temp.strip('\n'):
			flag = True
	if not flag :
		with open("keyNot.txt",'a+') as w:
			w.write(key+"\n")
		