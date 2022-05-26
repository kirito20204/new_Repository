task = input('Введите время в мин. и растояние в км.').split()
time = int(task[0])*60
distance = int(task[1])*1000
print(distance/time)