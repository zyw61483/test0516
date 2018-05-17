#! usr/bin/python3
# utf-8
def hello(str):
	print('hello '+str)
#print("hello world")
#print("你好")
#hello("world")
#hello("啦啦")

def printList(str,list):
	print(str)
	for obj in list:
		print(obj)

def unchange(obj):
	obj+=1
	print("unchange:"+str(obj))
	
def change(list,obj):
	list.append(obj)
	
a=1
print("first:"+str(a))
unchange(a)
print("now:"+str(a))

list=[1,2,3]
printList("first List:",list)
change(list,4)
printList("now List:",list)