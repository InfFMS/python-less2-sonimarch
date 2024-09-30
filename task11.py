a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if b1 > a2 or a1 > b2:
    print('пустое множество')
elif b1 == a2 and a1 == b2:
    print(b1)
else:
    print(a2, b1)