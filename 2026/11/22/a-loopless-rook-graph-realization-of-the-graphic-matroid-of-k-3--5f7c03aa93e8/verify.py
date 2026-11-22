"""Exact finite independent comparison of skew forcing with graphic closure.
Run: python verify.py
No third-party modules needed.
"""
from itertools import combinations

Q = range(3)
CELLS = [(i, j) for i in Q for j in Q]
N = len(CELLS)
ALL = (1 << N) - 1
EDGE = {i * 3 + j: ((i+j) % 3, (i-j) % 3) for i, j in CELLS}
assert len(set(EDGE.values())) == 9


def rook_neighborhood(k):
    i, j = divmod(k, 3)
    return sum(1 << (a * 3 + b)
               for a, b in CELLS if (a == i) != (b == j))

NEIGH = [rook_neighborhood(k) for k in range(N)]


def skew_closure(start):
    blue = start
    while True:
        add = 0
        for neighborhood in NEIGH:
            white_neighbors = neighborhood & ~blue
            if white_neighbors and white_neighbors & (white_neighbors - 1) == 0:
                add |= white_neighbors
        if not add:
            return blue
        blue |= add


def graphic_closure(start):
    parent = list(range(6))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    def join(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[x] = y
    for k, (a, b) in EDGE.items():
        if (start >> k) & 1:
            join(a, b + 3)
    return sum(1 << k for k, (a, b) in EDGE.items() if find(a) == find(b+3))


def is_connected_original_3by3(start):
    return graphic_closure(start) == ALL


def endpoints():
    count = 0
    for s in range(1 << N):
        assert skew_closure(s) == graphic_closure(s), (s, skew_closure(s), graphic_closure(s))
        count += 1
    bases = [s for s in range(1 << N) if s.bit_count() == 5 and skew_closure(s) == ALL]
    assert len(bases) == 81
    assert not any(skew_closure(s) == ALL for s in range(1 << N) if s.bit_count() < 5)
    for i in Q:
        for j in Q:
            center = i*3+j
            neighbor_edges = {EDGE[k] for k in range(N) if NEIGH[center] >> k & 1}
            u, v = EDGE[center]
            expected = {(a, b) for a in Q if a != u for b in Q if b != v}
            assert neighbor_edges == expected
    return count, len(bases)

if __name__ == '__main__':
    checks, minimum = endpoints()
    print('AFFINE_RECTANGLE_NEIGHBORHOODS_PASS 9')
    print('EXHAUSTIVE_CLOSURE_MATCH_PASS subsets=', checks)
    print('GRAPHIC_SPANNING_TREE_BASES_PASS count=', minimum)
    print('VERIFY_OK')
