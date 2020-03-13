import time
import local as lc

vvod = int(input(lc.VVOD))
list = []
a = 0
b = vvod
for i in range(vvod):
    list.append(int(input(lc.LIST)))
list.sort()
number = int(input(lc.NUMBER))
start = int(input(lc.START))

