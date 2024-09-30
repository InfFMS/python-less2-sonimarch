a, b, c, d = map(int, input().split())
if abs(a - c) == 1 and abs(b - d) == 1:
    print('Yes')
else:
    print('No')