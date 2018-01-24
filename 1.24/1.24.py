f=open(r'd:\python\1.txt','w')
f.write('xhh')
f.close()
with open(r'd:\python\1.txt','w') as fileWriter:
    fileWriter.write('xhh is the best')
import os
print os.getcwd()
print os.listdir('D:\\python')
# os.mkdir('test')
