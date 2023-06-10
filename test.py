from copy import deepcopy
a, b = [], []
for i in range(5):
    a.append(input())
    b.append(deepcopy(a))
    a.clear()
print(b)