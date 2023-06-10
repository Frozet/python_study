from datetime import datetime
from copy import deepcopy

ls, dc = [], []
with open('diary.txt') as f:
    for line in f.readlines():
        try:
            ln = datetime.strptime(line.rstrip(), '%d.%m.%Y; %H:%M')
            ls.append(ln)
        except:
            ln = line
            ls.append(ln)
        if ln == '\n':
            dc.append(deepcopy(ls))
            ls.clear()
    ls[-1] += '\n'
    ls.append('\n')
    dc.append(deepcopy(ls))
for i in sorted(dc, key=lambda x: x[0]):
    for j in i:
        if type(j) == datetime:
            print(j.strftime('%d.%m.%Y; %H:%M'))
        else:
            print(j, end='')





