a = 10027
s = []
while a <= 99999:
    if a % 133 == 125:
        s.append(a)
    a += 134

print(*s)