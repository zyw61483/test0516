#! usr/bin/python3

import sys

if len(sys.argv)==3:
	print(str(float(sys.argv[1]))+" + "+str(float(sys.argv[2]))+" = "+str(float(sys.argv[1])+float(sys.argv[2])))