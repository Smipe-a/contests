# Python 3.9 (PyPy 7.3.16)
from typing import List, Tuple
from collections import defaultdict, deque

def problem_b(experience: List[int], levels: List[Tuple[int, int]]):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for u, v in levels:
        graph[u].append(v)
        in_degree[v] += 1

    walkthrough = deque([1])
    dp = experience[:]
    
    max_experience = 0
    while walkthrough:
        level = walkthrough.popleft()
        for next_level in graph[level]:
            dp[next_level] = max(dp[next_level], dp[level] + experience[next_level])
            
            in_degree[next_level] -= 1
            if in_degree[next_level] == 0:
                walkthrough.append(next_level)
        
        max_experience = max(max_experience, dp[level])

    print(max_experience)


if __name__ == '__main__':
    n, m = map(int, input().split())
    experience = [0] + list(map(int, input().split()))
    levels = [tuple(map(int, input().split())) for _ in range(m)]

    problem_b(experience, levels)
