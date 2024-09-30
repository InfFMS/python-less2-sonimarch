a, b, c, d = map(int, input().split())
if (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2):
    print('Yes')
else:
    print("No")