'''
import re

list = []
matchPattern = re.compile(r'INVALID PARAMETER')
file = open('movies.xml','r')
while 1:
    line = file.readline()
    if not line:
        print("error")
        break
    elif matchPattern.search(line):
        pass
    else:
        list.append(line)
file.close()
file = open(r'target.xml', 'w')
for i in list:
    file.write(i)
file.close()
'''
file = open('ipgb20190101.xml','r')
lines = file.readlines()
list=['<?xml version="1.0" encoding="UTF-8"?>','<root>'] #首行加<root>
for lines in lines:
   if "xml" in lines:
     print(lines)
   elif "DOCTYPE" in lines:
        print(lines)
   else:
       list.append(lines)
file.close()
#最后一行加</root>
list.append('</root>')
file = open(r'target.xml', 'w')
for i in list:
    file.write(i)
file.close()
