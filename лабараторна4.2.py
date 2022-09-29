import math
def func (x,y,a): 
          Z=5.126*math.log(abs(3.3+x**2))+(x+y**3)**1/6-4*math.tan(a+x)
          return(Z)
x1=int(input("Введіть x="))
y1=int(input("Введіть y="))
a1=int(input("Введіть a="))
f=func(x1,y1,a1)
print (f)
