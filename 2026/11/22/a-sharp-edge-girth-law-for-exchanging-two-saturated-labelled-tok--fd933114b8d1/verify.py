#!/usr/bin/env python3
"""Exact finite replay for the saturated-edge exchange distance theorem.

This checker enumerates legal distinguishable-token configurations directly.
Its exhaustive BFS is supplemental to, not a substitute for, the proof for all graphs.
"""
from collections import deque


def edge_cycle_length(n, edges, u, v):
    neighbors = [set() for _ in range(n)]
    for a, b in edges:
        if {a, b} == {u, v}:
            continue
        neighbors[a].add(b)
        neighbors[b].add(a)
    d = [-1] * n
    d[u] = 0
    q = deque([u])
    while q:
        x = q.popleft()
        for y in neighbors[x]:
            if d[y] < 0:
                d[y] = d[x] + 1
                q.append(y)
    return (d[v] + 1) if d[v] >= 0 else None


def exact_distance(n, edges, s, u, v):
    neighbors = [set() for _ in range(n)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    start = (u,) * s + (v,) * s
    target = (v,) * s + (u,) * s
    distance = {start: 0}
    q = deque([start])
    while q:
        x = q.popleft()
        if x == target:
            return distance[x], len(distance)
        cnt = [0] * n
        for p in x:
            cnt[p] += 1
        for i, p in enumerate(x):
            for w in neighbors[p]:
                if cnt[w] == s:
                    continue
                y = x[:i] + (w,) + x[i+1:]
                if y not in distance:
                    distance[y] = distance[x] + 1
                    q.append(y)
    raise AssertionError('Target was unreachable')


def graph_cases():
    def path(n):
        return [(i, i+1) for i in range(n-1)]
    def cycle(n):
        return [(i, (i+1) % n) for i in range(n)]
    def complete(n):
        return [(i, j) for i in range(n) for j in range(i+1, n)]
    cases = []
    for n in range(3, 9):
        cases.append(('cycle'+str(n), n, cycle(n), [2] if n >= 7 else [2,3], [0]))
    for n in range(3, 7):
        cases.append(('path'+str(n), n, path(n), [2,3], [0, n-2]))
    cases.extend([
        ('complete4',4,complete(4),[2,3],[0,3]),
        ('diamond',4,[(0,1),(1,2),(2,3),(3,0),(0,2)],[2,3],[0,4]),
        ('house',5,[(0,1),(1,2),(2,3),(3,0),(1,4),(2,4)],[2],[0,1,4]),
        ('triangle_tail',4,[(0,1),(1,2),(2,0),(2,3)],[2,3],[0,2,3]),
        ('theta',6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,3)],[2],[0,3,6]),
    ])
    return cases


def run():
    cases = 0
    total_visited = 0
    branch_counts = {}
    for name, n, edges, capacities, indices in graph_cases():
        for s in capacities:
            for edge_id in indices:
                u,v = edges[edge_id]
                g = edge_cycle_length(n,edges,u,v)
                expected = 2*s + min(4, g-2 if g is not None else 4)
                actual, visited = exact_distance(n,edges,s,u,v)
                assert actual == expected, (name,s,(u,v),g,expected,actual)
                branch_counts[g if g is not None else 'bridge'] = branch_counts.get(g if g is not None else 'bridge',0)+1
                total_visited += visited
                cases += 1
    print('EXACT_BFS_CASES',cases,'PASS')
    print('CYCLE_LENGTH_BRANCHES',dict(sorted(branch_counts.items(),key=lambda z:str(z[0]))))
    print('TOTAL_VISITED_SOURCE_STATES',total_visited)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
