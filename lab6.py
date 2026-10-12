print('вариант заданий: 22')
a = input('введите строку: ')
NewStr = a[0]
counter = 1
for i in range(1, (len(a))):
    if NewStr[-1] == a[i]:
        counter += 1
    else:
        NewStr += str(counter)
        NewStr += a[i]
        counter = 1
NewStr += str(counter)
print(f'{a} -> {NewStr}')
