s = []
for i in range(2, int(input()) + 1):
    for j in range(2, int(i ** 0.5 // 1 + 1)):
        if i % j == 0:
            break
    else:
        s.append(i)

print(*s)