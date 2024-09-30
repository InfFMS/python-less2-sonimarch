a, b, c, d = map(int, input().split())
if abs(a - c) == abs(b - d) or abs(a - c) == 0 or abs(b - d) == 0:
    print('Yes')
else:
    print('No')