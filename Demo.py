#! usr/bin/python3
import threading
import time

class MyThread(threading.Thread):
	def run(self):
		self.doSth()	
	def doSth(self):
		for i in range(10):
			time.sleep(1)
			print("Hello")
		
t = MyThread()
t.start()		