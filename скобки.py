stack=[]
data=input()
is_ok=True
for i in data:
    if i =='(' or i =='[' or i =='{':
        stack.append(i)
    else:
        if len(stack) > 0:
            a=stack.pop()
            if (i ==')' and a =='(') or (i ==']' and a =='[') or (i =='}' and a =='{'):
                continue
        print('no')
        is_ok=False
        break
if is_ok:
    if len(stack) != 0:
        print('no')
    else:
        print('yes')