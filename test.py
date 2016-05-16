# coding: UTF-8
import re
import requests

def write(page):
    r = requests.get("http://www.0597zp.com/more.php?page="+str(page))
    result = re.findall('target=_blank>(.*?)</A>',r.content)
    if(len(result)>0):
        tempfile = open("mobile.txt",'a')
        for i in result:
            print (i + ";")
            tempfile.write(i + ";")
        tempfile.write("\n")
        tempfile.close()
        # print ("共"+str(len(result))+"条数据写入文件")

for i in range(15,26):
    write(i)