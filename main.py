import time
import local as lc

vvod = int(input(lc.VVOD))
list = []
a = 0
c = vvod
for i in range(vvod):
    list.append(int(input(lc.LIST)))
list.sort()
number = int(input(lc.NUMBER))

def iterat():
    s = -1
    mid = -1
    b = vvod
    while b > s + 1:
        mid = (s + b) // 2
        if list[mid] >= number:
            b = mid
        else:
            s = mid
    print(b)


def time1():
    now = time.time()
    iterat()
    print(lc.TIME1, time.time() - now)


def rec(list, a, c):
    m = (c + a) // 2
    if number == list[m]:
        return m
    elif number <= list[m]:
        return rec(list, a, m)
    else:
        return rec(list, m, c)


def time2():
    now = time.time()
    print(rec(list, a, c))
    print(lc.TIME2, time.time() - now)


if number <= list[vvod - 1]:
    time1()
    time2()
else:
    print(lc.ERROR1)


