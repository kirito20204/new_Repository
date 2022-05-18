queue=[]
command=input().split()
while command[0]!='exit':
    if command[0]=='push':
        queue.append(command[1])
        print('ok')
    elif command[0]=='pop':
        print(queue.pop(0))
    elif command[0]=='front':
        print(queue[0])
    elif command[0]=='clear':
        queue.clear()
        print('ok')
    elif command[0]=='size':
        print(len(queue))
    command=input().split()
print('bye')
