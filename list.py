classmates=['zjc','xww']
print(classmates)
print(len(classmates))

print(classmates[-1])#获取最后一个元素
print(classmates[-2])

classmates.append('xhh')#追加到末尾
print(classmates)

classmates.insert(1,'jack')
print(classmates)

classmates.pop()#删除末尾
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1]='ll'
print(classmates)

L=['apple',1,True]
s=['python','java',['asp','php'],'scheme']
print(len(s))

classmates=('jj','dd')#tuple不可变，代码更安全
t=(1,)#只有一个元素时

t=('a','b',['A','B'])
print(t)
t[2][0]='X'
t[2][1]='Y'
print(t)
