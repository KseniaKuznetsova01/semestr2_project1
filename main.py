vvod = int(input('Введите кол-во объектов в массиве'))
list=[]
for i in range(vvod):
    list.append(int(input()))
list.sort()
print(list)
т
start = int(input('''Какой способ вы хотите использовать для поиска?
1-Итеративный
2-Рекурсивный'''))
if start == 1:




    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] > key:
            right = middle
        else:
            left = middle


elif start == 2:
    print('')
else:
    print('ERROR')