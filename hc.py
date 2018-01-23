def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

def enroll(name,gender,age=6,city='hz'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
enroll('xww',1)
enroll('xcc',2,7)
enroll('xhh',3,city='qz')

def add_end(L=[]):
    L.append('end')
    return L

print(add_end([1,2,3]))
print(add_end([1,2,3]))
print(add_end())
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L=[]
    L.append('end')
    return L

def calc(numbers):
    sum =0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc([1,2,3]))

def calc2(*numbers):
    sum =0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc2(1,2,3))
print(calc2())
nums=[1,2,3]
print(calc2(nums[0],nums[1]))
print(calc2(*nums))

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('xww',30)
person('bob',35,city='hz')
person('xcc',45,gender='M',job='eng')

extra={'city:':'bj','job:':'eng'}
person('jack',1,**extra)

def person2(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

person('xcc',1,city='hz',job='eng')
person('xww',2,city='nb',job='qq',zipcod=123)

def person(name,age,*,city='beijing',job):
    print(name,age,city,job)
person('jack',24,city='bj',job='a')
person('jack',25,job='b')

def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=66)
f2(1,2,d=99,ext=None)
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
f2(*args,**kw)

def product(*numbers):
    s=1
    for i in numbers:
        s=s*i
    print(s)
product(5,6.7)
