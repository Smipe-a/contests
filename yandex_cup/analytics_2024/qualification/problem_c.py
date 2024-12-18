from collections import defaultdict


with open('yandex_cup\\analytics_2024\\qualification\\persons.txt',
          encoding='utf-8') as file:
    # A list of all representatives
    persons = [person.strip() for person in file.readlines()]

with open('yandex_cup\\analytics_2024\\qualification\\pairs.txt',
          encoding='utf-8') as file:
    pairs = [pair.strip().split(' - ') for pair in file.readlines()]
    # A hashmap containing all representatives and their connections through "1 handshake"
    connections = defaultdict(list)
    for pair in pairs:
        connections[pair[0]].append(pair[1])
        connections[pair[1]].append(pair[0])

def dfs(node):
    # O(V + E)
    stack = [node]
    # All possible handshakes are iterated over
    while stack:
        current = stack.pop()
        for neighbor in connections[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

visited, civilizations = set(), 0
for person in persons:
    # As soon as we encounter a representative not in visited
    # it means we've moved to the next civilization
    if person not in visited:
        civilizations += 1
        visited.add(person)
        dfs(person)

print(civilizations)
