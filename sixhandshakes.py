import csv
import operator
import networkx as nx

graph = nx.Graph()
# Открывает файл для чтения, заполняем объект graph списком граней графа
with open('email-Eu-core.txt', 'r') as file:
    next(file)
    for line in file.readlines():
        a, b = map(int, line.strip().split())

        graph.add_edge(a, b)

# Проверяем количество вершин и граней
print(graph)

s = dict()
# В цикле проходимся по всем вершинам и ищем кратчайший путь от каждой к каждой
for i in graph:
    for j in graph:
        try:
            n = nx.shortest_path(graph, i, j)
            a = len(n) - 1

            if a != 0:    # Путь до самим себя не считаем
                if s.get(a):
                    s[a] += 1
                else:
                    s[a] = 1
        except:
            continue

# Так как в цикле проходили путь от вершины к вершине и туда и обратно, то делим полученный результат на 2
for key, val in s.items():
    s[key] = val // 2

# Считаем медиану и моду
path_line = []
for key, val in s.items():
    for i in range(val):
        path_line.append(key)
print('Медиана:', path_line[len(path_line) // 2])
x = max(s.items(), key=operator.itemgetter(1))
print('Мода:', x[0])

# Заполняем csv файл для дальнейшей работы с данными
with open('excel_file.csv', 'w', encoding='utf-8', newline='') as data:
    writer = csv.writer(data)
    writer.writerow(list(s.keys()))
    writer.writerow(list(s.values()))