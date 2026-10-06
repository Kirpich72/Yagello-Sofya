#первое задание: 22. максимальную длину строго возрастающего участка последовательности и сумму элементов этого самого длинного участка
n = int(input('введите количество цифр: '))
first = int(input())
count = 1
Fcount = 1
ssum = first
Fssum = first
for i in range(n-1):
    x = int(input())
    if x > first:
        count += 1
        ssum += x
        if count > Fcount:
            Fcount = count
            Fssum = ssum
    else:
        count = 1
        ssum = x
    first = x
print(f'ответ на первое задание: макс. длина = {Fcount}, сумма = {Fssum}')
#второе задание: Вводятся N чисел. Найдите наибольшую сумму подряд идущих элементов, состоящую ровно из 4 чисел, и укажите позицию первого элемента этой группы.
N = int(input('введите количество цифр: '))
summ = 0
Fsum = 0
firstindex = -1
for i in range(N):
    y = int(input())
    if 999 < y < 10000:
        summ += y
        if firstindex == -1:
            firstindex = i
    else:
        firstindex = -1
    if summ > Fsum:
        Fsum = summ
print(f'ответ на второе задание: макс.сумма = {Fsum}, индекс первого элемента = {firstindex} (P.S. нумерация идет с 0)')
