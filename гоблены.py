from collections import deque

first = deque()
second = deque()

for i in range(int(input())):
    s = input().split()
    if s[0] == '+':
        second.append(s[1])
    elif s[0] == '*':
        second.appendleft(s[1])
    else:
        print(first.popleft())

    if len(second) > len(first):
        x = second.popleft()
        first.append(x)