import math
x=int(input("Введіть x="))
y=((((7*x+math.cos(x)+math.sqrt(x)))**3*x-1)//math.e**1.5*x)-math.log(abs(x))
print("y=",y)