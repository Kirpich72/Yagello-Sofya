import math
print('вариант заданий: 22')
ssum = 0
for n in range(1, 51):
    ssum += ((1.9**(2*n + 1))/((n**n)+2 ))*math.sin(n)
print(f'сумма = {ssum}')

proizv = 1
for n in range(1,21):
    proizv *= (n**2 + (math.sin(n**3))**3 +1)/(n**2 + (math.cos(n**2))**2 + math.sin(n))
print(f'произведение = {proizv}')
