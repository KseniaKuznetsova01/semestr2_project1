vvod = int(input('Введите кол-во объектов в массиве'))
list=[]
for i in range(vvod):
    list.append(int(input('Введите новое число для добавления в массив')))
list.sort()
print(list)
number = int(input('Введите число для поиска:'))
start = int(input('''Какой способ вы хотите использовать для поиска?
1-Итеративный
2-Рекурсивный'''))
if start == 1:
    s = -1
    m = -1
    b = vvod
    while b > s + 1:
        m = (s + b) // 2
        if list[m] > number:
            b = m
        else:
            s = m
    print(m,list[m])
elif start == 2:
    print('')
else:
    print('ERROR')