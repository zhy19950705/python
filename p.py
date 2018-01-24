f=open(r'd:\python\1.txt')
print(f.read())
with open(r'd:\python\1.txt','r') as fileReader:
    # print(fileReader.read())
    for line in fileReader.readlines():
     print(line.strip())