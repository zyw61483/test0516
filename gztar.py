#! usr/bin/python3
import gzip
import os
def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    #获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    #创建gzip对象
    open("tar\\"+f_name, "w+").write(g_file.read().decode())
    #gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
	
un_gz("20180527.tar.gz")
