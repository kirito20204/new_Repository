a = [2, 1, 3, 4, 5]
s='hello'
a.sort(reverse=True)
print(' '.join(map(str, a)))
def list_sort(lst):
    lst.sort(key=lambda a: abs(a), reverse=True)
    return lst

def get_abs(x):
    return abs(x)

def all_eq(lst):
    return 0
s = 'Hello'
s1 = s.rjust(6, '+')
print(f'{s1}')

b = [i**2 for i in range(100) if i%2==1 and i<50 ]
print(b)