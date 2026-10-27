print('вариант заданий: 2')
print('Task 1')
a = list(map(float, eval(input('введите список: '))))
d = float(input('введите d: '))
count = 0
SrArifm = (sum(a))/(len(a))
for i in a:
    if abs((SrArifm - i)) <= abs(d):
        count += 1
print('ответ =', count)


print('Task 2')
n = int(input('введите n: '))
matr = []

# генератор таблицы с элементами = индексам в матрице
# for i in range(1, 2*n+2):
#     matr.append([])
#     for j in range(1, 2*n+2):
#         matr[-1].append(int(str(i)+str(j)))

# создание таблицы вручную
print(f'вписывайте по одной строке, числа через пробел (кол-во чисел в одной стр = {n*2+1} ): ')
for i in range(2*n+1):
    matr.append(list(map(float, (input()).split())))
centr = abs(matr[n][n])
AllCount = 0
for i in range(0, n+1, 2):
    start = n - (i//2)
    end = n + (i//2) + 1
    count = sum(abs(element) < centr for string in matr[start:end] for element in string[start:end])
    AllCount += count
    print(f'Порядок = {i+1}: кол-во элементов = {count}')
print(f'Кол-во элеметнов во всей матрице больше центрального = {AllCount}')
