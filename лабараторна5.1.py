import math
x=int(input("Введіть значення x="))
def func1(x1):
        rez=2//x+2.31*math.e**2*x
        return(rez)
def func2(x2):
        rez=math.asin(0.2*x+0.3)
        return(rez)
def func3(x3):
        rez=math.cos(x+0.4*math.log(math.fabs(x+0.2)))
        return(rez)
if (x>=1):
        y=func1(x)
elif (-1<x<1):
        y=func2(x)
elif (x<=-1):
        y=func3(x)
print("y=",y)

