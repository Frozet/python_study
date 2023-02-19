from collections import Counter

with open('data2.txt') as f:
    data = f.read().splitlines()
    N = int(data[0])
    edges = []
    islands = [0 for _ in range(N)]
    island_count = 0

    for i in range(1, len(data)):
        u, v = map(int, data[i].split())
        edges.append((u, v))

        if islands[u - 1] == 0 and islands[v - 1] == 0:
            island_count += 1
            islands[u - 1] = islands[v - 1] = island_count

        elif islands[u - 1] == 0:
            islands[u - 1] = islands[v - 1]

        elif islands[v - 1] == 0:
            islands[v - 1] = islands[u - 1]

        elif islands[u - 1] != islands[v - 1]:
            old_island = islands[v - 1]
            new_island = islands[u - 1]

            for i in range(N):
                if islands[i] == old_island:
                    islands[i] = new_island

for i in range(N):
    if islands[i] == 0:
        island_count += 1
        islands[i] = island_count

print(len(Counter(islands)) - 1)
