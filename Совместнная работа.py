a = input('Введите время в мин. и растояние в км.').split()
b = int(a[0])*60
c = int(a[1])*1000
print(c/b)