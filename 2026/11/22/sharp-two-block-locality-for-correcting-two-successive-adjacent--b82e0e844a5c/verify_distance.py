#!/usr/bin/env python3
"""Check the binary adjacent-swap distance identity on all pairs up to length 9."""
from collections import deque
from itertools import product


def prefix_distance(x, y):
    if sum(x) != sum(y):
        return None
    running = 0
    cost = 0
    for a, b in zip(x, y):
        running += a - b
        cost += abs(running)
    return cost


def bfs_distances(start):
    q = deque([start])
    dist = {start: 0}
    while q:
        x = q.popleft()
        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                continue
            y = x[:i] + (x[i + 1], x[i]) + x[i + 2:]
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    return dist


if __name__ == '__main__':
    checked = 0
    for n in range(1, 10):
        for x in product((0, 1), repeat=n):
            reach = bfs_distances(x)
            for y, graph_distance in reach.items():
                assert prefix_distance(x, y) == graph_distance, (x, y)
                checked += 1
        print(f'length={n} ordered_same_weight_pairs={sum(1 for x in product((0,1), repeat=n) for y in product((0,1), repeat=n) if sum(x)==sum(y))}')
    print(f'PASS binary prefix-transport identity, {checked} ordered same-weight pairs')
