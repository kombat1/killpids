#!/bin/python

import sys

try:
	sys.argv[1]
except:
	print "Usage: python killpid.py pids.txt"
	sys.exit()	

kill_lis = open(sys.argv[1],"r").read()

b = kill_lis.split("\n")
a = []
c = []
for i in  range(len(b)-1):
	c.append(b[i].split(" "))
	h = c[i][0]+c[i][1] 
	lists = h.split(":")
	spl = lists[1].replace("?","")
	a.append(spl.replace("pts/0",""))

for i in range(len(a)):
	result = a[i]+"\x0a"
print " ".join(a)