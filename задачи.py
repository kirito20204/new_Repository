'''a=input()
b=input()
a=''.join(sorted(a))
b=''.join(sorted(b))
if a==b:
    print('YES')
else:
    print('NO')'''
a = input().strip().split(' ')
a = list(map(int, a))
a.sort(reverse=True)
a = ' '.join(list(map(str, a )))
print(a)