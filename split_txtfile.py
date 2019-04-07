file = open('ipgb20190101.xml','r')
lines = file.readlines()
list=[] #首行加<root>
j=0
for lines in lines:
   if 'xml version="1.0" encoding="UTF-8"' in lines:
     #print(lines)
     j=j+1
     print("第"+str(j)+"个")
     list=['<?xml version="1.0" encoding="UTF-8"?>\n']
     if j==1000:
         break

   else:
       list.append(lines)
       file = open(r'./splitfiles/ipgb20190101_'+str(j)+'.xml', 'a')
       for i in list:
           file.write(i)
           list=[]

file.close()
