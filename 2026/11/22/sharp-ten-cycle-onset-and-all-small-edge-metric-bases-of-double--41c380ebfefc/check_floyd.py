#!/usr/bin/env python3
"""Independent finite certificate: Floyd–Warshall and unique edge-signature sets."""
from itertools import combinations


def counts(n):
    vertices = [(L, i) for L in 'xuvy' for i in range(n)]
    edge_set = set()

    def add(u, v):
        edge_set.add(frozenset((u, v)))

    for i in range(n):
        j = (i+1) % n
        add(('x',i),('x',j)); add(('y',i),('y',j))
        add(('x',i),('u',i)); add(('v',i),('y',i))
        add(('u',i),('v',j)); add(('v',i),('u',j))

    edges = [tuple(e) for e in edge_set]
    assert len(edges) == 6*n
    pos = {p:i for i,p in enumerate(vertices)}
    N = len(vertices)
    distances = [[N+1]*N for _ in vertices]
    for i in range(N): distances[i][i] = 0
    for e in edges:
        u, v = (pos[p] for p in e)
        distances[u][v] = distances[v][u] = 1
    for k in range(N):
        for i in range(N):
            via = distances[i][k]
            for j in range(N):
                candidate = via+distances[k][j]
                if candidate < distances[i][j]:distances[i][j] = candidate

    signatures = [tuple(min(distances[v][pos[a]], distances[v][pos[b]])
                        for a,b in edges) for v in range(N)]
    result = []
    for k in (2,3,4):
        count = 0
        for selected in combinations(range(N), k):
            if len(set(zip(*(signatures[v] for v in selected)))) == len(edges):
                count += 1
        result.append(count)
    return result

if __name__ == '__main__':
    print('n\tvertices\tedges\tpairs\ttriples\tquadruples')
    for n in range(3, 13):
        a,b,c = counts(n)
        print(f'{n}\t{4*n}\t{6*n}\t{a}\t{b}\t{c}')
