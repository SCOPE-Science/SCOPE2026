"""Explicit directed-neighborhood checks for length-three de Bruijn codes.

All tests use the forward arcs abc -> bcz and distance at most two.
No external dependencies.
"""
from collections import deque
from itertools import product, combinations


def data(q):
    V = list(product(range(q), repeat=3))
    nbr = {x: [(x[1], x[2], z) for z in range(q)] for x in V}
    balls = {}
    for x in V:
        visited = {x}
        frontier = {x}
        for _ in range(2):
            frontier = {y for u in frontier for y in nbr[u]} - visited
            visited.update(frontier)
        balls[x] = visited
    return V, balls


def identifying(V, balls, C):
    signatures = [frozenset(balls[v].intersection(C)) for v in V]
    return all(signatures) and len(set(signatures)) == len(V)


def run():
    for q in range(2, 10):
        V, balls = data(q)
        C = {v for v in V if v[0] != v[2]}
        assert len(C) == q*q*(q-1)
        assert identifying(V, balls, C) == (q >= 3)
        # Each forced word is the only witness separating its pair.
        for a, b, c in V:
            if a != c:
                assert balls[(a,b,c)] ^ balls[(c,b,c)] == {(a,b,c)}
        print(f'q={q}: vertices={len(V)}, canonical={len(C)}, identifying={q>=3}, forcing=PASS')
    V, balls = data(2)
    optima = []
    for k in range(len(V)+1):
        for W in combinations(V, k):
            if identifying(V, balls, set(W)):
                optima.append(set(W))
        if optima:
            assert k == 7
            break
    assert len(optima) == 2
    assert {tuple(V[i] for i in range(8) if V[i] not in C) for C in optima} == {((0,0,0),), ((1,1,1),)}
    print('binary exact minimum=7; two optimizers: omit 000 or 111; PASS')

if __name__ == '__main__':
    run()
