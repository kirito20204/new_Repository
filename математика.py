import math

'''a = int(input('Ведите 1 число'))
b = int(input('Ведите 2 число'))
result1 = a//b
result2 = a%b
print('Если пользователь ввёл ', a, 'и', b, 'целая часть от деления =', result1, 'остаток от деления = ', result2)'''

'''a = float(input('введите число'))
b = a * 2
print(round(b, 2))'''

'''a = int(input('Ввести целое число больше 500'))
b = math.sqrt(a)
print(round(b, 2))'''

'''a = int(input('Введите 1 число'))
b = int(input('Введите 2 число'))
с = int(input('Введите 3 число'))
x=a**2+2*a*b+с
print(x)'''

'''a = int(input('Введите катет а'))
b = int(input('Введите катет б'))
S = 1/2*a*b
C = math.sqrt(a**2+b**2)
print('Вели катет', a, 'вели катет', b, 'Площадь', S, 'a гипотенузы =', C)'''

'''a = int(input('Введите рост человека.'))
print('Идеальный вес =', a, '-100=', a-100, 'кг')'''

'''a = int(input('Введите 1 число'))
b = int(input('Введите 2 число'))
a, b = b, a
print(a, b)'''

s = 1000000
for i in range(1, 4):
    s = (s * 115)/100
    print('год', i, 'сумма =', s)