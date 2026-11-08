"""Finite exact enumerator of signed one-hole coordinate frames.
Run: python check_sparse_frames.py
The general theorem uses a combinatorial argument, not finite enumeration.
"""
from itertools import permutations, product
from math import factorial
from collections import deque


def enumerate_graph(n):
    r = n - 1
    vertices = [(rows, signs) for rows in permutations(range(n), r)
                for signs in product((-1, 1), repeat=r)]
    ix = {v: k for k, v in enumerate(vertices)}
    assert len(vertices) == 2**r * factorial(n)
    degree_sum = 0
    visited = {0}
    q = deque([0])
    while q:
        i = q.popleft()
        rows, signs = vertices[i]
        empty, = set(range(n)) - set(rows)
        seen_neighbors = set()
        for col in range(r):
            for new_sign in (-1, 1):
                rr = list(rows)
                ss = list(signs)
                rr[col] = empty
                ss[col] = new_sign
                j = ix[(tuple(rr), tuple(ss))]
                assert j != i
                seen_neighbors.add(j)
                if j not in visited:
                    visited.add(j)
                    q.append(j)
        assert len(seen_neighbors) == 2*r
        degree_sum += len(seen_neighbors)
    assert len(visited) == len(vertices)
    assert degree_sum == 2*r*len(vertices)
    edges = degree_sum // 2
    cycles = edges - len(vertices) + 1
    assert cycles == (n-2)*2**(n-1)*factorial(n)+1
    return len(vertices), edges, cycles

if __name__ == '__main__':
    for n in range(2, 7):
        V, E, C = enumerate_graph(n)
        print('n=%d V=%d E=%d b1=%d' % (n, V, E, C))
    print('SPARSE_REAL_FRAME_GRAPH_EXACT_OK')
