
if (n := int(input())):
  if n == 1 or n == 2 or n == 12:
    print('Зима')
  elif 2 < n < 6:
    print('Весна')
  elif 5 < n < 9:
    print('Лето'):
  elif 8 < n < 12:
    print("Осень")
  else:
    print('Неверный номер месяца')