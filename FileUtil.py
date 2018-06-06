import os

def write(filename,model,list):
	filepath = filename[:filename.rfind("\\")]
	if not os.path.exists(filepath):
		os.makedirs(filepath)
	with open(filename,model) as f:
		for item in list:
			f.write(item+"\n")
