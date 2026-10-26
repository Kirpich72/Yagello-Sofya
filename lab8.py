print('вариант заданий: 2')
print('Task 1')
a = list(map(float, eval(input('введите список: '))))
d = float(input('введите d: '))
count = 0
SrArifm = (sum(a))/(len(a))
for i in a:
    if abs((SrArifm - i)) <= abs(d):
        count += 1
print('ответ', count)


print('Task 2')
n = int(input('введите n: '))
matr = []
count = 0
print('впишите по одной строке: ')
for i in range(2*n+1):
    matr.append(list(map(float, eval(input()))))
for i in range(1, n-1, 2):
    print(i)
