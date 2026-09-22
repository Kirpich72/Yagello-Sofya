#first task
import math
x = float(input('значение х = '))
y = (((math.e)**(x*x))*math.log(2+(x**(1/x))) + (2**x)*math.log(2-x) - (math.e)**(2/(x**x)))
print(f'ответ на первое задание: {y:.5f}')

#second task
a, b = list(map(float, ((input('значения промежутка (P.S. через пробел): ').split()))))
def partRange(a,b,c):
    while a<b and a+c <= b:
        yield a
        a+=c
for x in partRange(a,b, 0.05):
    y = ((math.acos(x))**2 + (math.asin(x))**2)/((math.sin(1+ (x**2)))**2 - (math.cos(1 - (x**2)))**2)
    print(f'x = {x} -> y = {y}')
