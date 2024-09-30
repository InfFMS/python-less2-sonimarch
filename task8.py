a, b, c, d = map(int, input().split())
if abs(a - c) == abs(b - d):
    print('Yes')
else:
    print('No')