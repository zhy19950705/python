from hs import my_abs
# print(my_abs('a'))
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)

def quadratic(a,b,c):
   x=(-b+math.sqrt(b*b-4*a*c))/2
   y=(-b-math.sqrt(b*b-4*a*c))/2
   return x,y
x,y=quadratic(1,4,4)
print(x,y)