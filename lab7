# variant 22

# Task 1. на вход строка, на выходе список
a = eval(input())
spisok = []
for i in a:
    if type(i) == list:
        for j in i:
            spisok.append(j)
    else:
        spisok.append(i)
print(spisok)

# Task 2
b = input('введите строку/список: ')
matr = [[0 for j in range(len(b))] for i in range(len(b))]
for i in range(len(b)-1, -1, -1):
    matr[i][i] = 1
    for j in range(i+1,len(b)):
        if b[i] == b[j]:
            matr[i][j] = matr[i+1][j-1] + 2
        else:
            matr[i][j] = max(matr[i+1][j], matr[i][j-1])
# (Для наглядности, на ход решения не влияет, можно убрать) таблица кол-ва макс знаков в палиндроме с i по j индексы 
print('cтроки = i, столбцы = j')
s = '   '
for i in range(len(b)):
    if i <= 10:
        s += '  ' + str(i)
    else:
        s += ' ' + str(i)
print(s)
for i in range(len(matr)):
    print(i, ' ', matr[i])
# конец блока с матрицей
i = 0
j = len(b) - 1
LeftPart = []
RightPart = []
while i <= j:
    if i == j:
        LeftPart.append(b[i])
        break
    elif b[i] == b[j]:
        LeftPart.append(b[i])
        RightPart.append(b[j])
        i += 1
        j -= 1
    elif matr[i+1][j] > matr[i][j-1]:
        i += 1
    else:
        j -=1
LeftPart += RightPart[::-1]
print(f'{b} -> {matr[0][-1]} ({''.join(LeftPart)})')
