#!/usr/bin/env python3
"""Integer-only check of the row-mirror perfect-matching-complex transfer identity.
No external packages or files are needed. Run: python3 CHECK.py
"""
from collections import deque
from functools import lru_cache

ALPHABET = ((0, 1), (5, -1), (2, -1), (7, 1))

def tiling_edges():
    return {a: {b for b in range(8) if not (a & b)
                and (7 ^ a ^ b) in (0, 3, 6)} for a in range(8)}

def transfer():
    rel = tiling_edges()
    start = frozenset((0,))
    states = [start]
    index = {start: 0}
    pending = deque([start])
    transitions = {}
    while pending:
        state = pending.popleft()
        i = index[state]
        transitions[i] = []
        for mandatory, weight in ALPHABET:
            nxt = frozenset(b for a in state for b in rel[a]
                            if (b & mandatory) == mandatory)
            if nxt not in index:
                index[nxt] = len(states)
                states.append(nxt)
                pending.append(nxt)
            transitions[i].append((index[nxt], weight))
    size = len(states)
    mat = [[0] * size for _ in range(size)]
    for i, row in transitions.items():
        for j, wt in row:
            mat[i][j] += wt
    finish = [int(any(0 in rel[a] for a in state)) for state in states]
    return states, mat, finish

def mul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def power(a, exponent):
    b = eye(len(a))
    while exponent:
        if exponent & 1:
            b = mul(b, a)
        a = mul(a, a)
        exponent //= 2
    return b

def w(n, mat, finish):
    p = power(mat, 2*n - 1)
    return sum(p[0][i] * v for i, v in enumerate(finish))

def brute(n):
    """Independent full-perfect-matching enumeration, not transfer-state reuse."""
    L = 2*n
    vertices = 3*L
    adjacent = [set() for _ in range(vertices)]
    for r in range(3):
        for c in range(L):
            u = r*L+c
            if c+1 < L:
                v = u+1
                adjacent[u].add(v)
                adjacent[v].add(u)
            if r+1 < 3:
                v = u+L
                adjacent[u].add(v)
                adjacent[v].add(u)
    edges = sorted((u, v) for u in range(vertices)
                   for v in adjacent[u] if u < v)
    edge_id = {edge: i for i, edge in enumerate(edges)}
    @lru_cache(None)
    def perfect(available):
        if not available:
            return ((),)
        lowest = (available & -available).bit_length()-1
        result = []
        for other in adjacent[lowest]:
            if available & (1 << other):
                identifier = edge_id[min(lowest, other), max(lowest, other)]
                for rest in perfect(available ^ (1 << lowest) ^ (1 << other)):
                    result.append((identifier,) + rest)
        return tuple(result)
    matchings = perfect((1 << vertices)-1)
    involution = []
    for u, v in edges:
        ru = (2-u//L)*L + u%L
        rv = (2-v//L)*L + v%L
        involution.append(edge_id[min(ru, rv), max(ru, rv)])
    orbits = []
    seen = set()
    for i in range(len(edges)):
        if i not in seen:
            orb = frozenset((i, involution[i]))
            orbits.append(orb)
            seen.update(orb)
    invariant_faces = {0}
    for m in matchings:
        contained = set(m)
        eligible = [j for j, orb in enumerate(orbits) if orb <= contained]
        for subset in range(1 << len(eligible)):
            mask = 0
            for k, j in enumerate(eligible):
                if subset & (1 << k):
                    mask |= 1 << j
            invariant_faces.add(mask)
    # Every selected orbit, whether of size 1 or 2, contributes -1 to
    # (-1)^(face cardinality) times its internal orientation sign.
    return sum((-1)**bin(mask).count("1") for mask in invariant_faces), len(matchings)

def main():
    states, M, finish = transfer()
    expected_states = [
        frozenset((0,)), frozenset((1,4,7)), frozenset((7,)),
        frozenset((0,3,6)), frozenset(), frozenset((3,6)),
        frozenset((1,4)),
    ]
    assert states == expected_states, states
    assert finish == [0,1,1,0,0,0,1]
    assert len(M) == 7
    assert power(M,8) == power(M,2), 'Exact matrix identity failed'
    for n in range(1,50):
        expect = {0:1,1:0,2:-1}[n % 3]
        assert w(n,M,finish) == expect, (n,w(n,M,finish),expect)
    # Direct face enumeration, including non-extendable matching exclusions.
    for n in range(1,7):
        face_sum, match_count = brute(n)
        assert face_sum == w(n,M,finish), (n,face_sum,w(n,M,finish))
        print('half_width',n,'perfect_matchings',match_count,
              'fixed_face_signed_sum',face_sum,
              'homology_trace',(-1)**n*face_sum)
    print('ROW_MIRROR_SEVEN_STATE_TRANSFER_AND_INDEPENDENT_FACES_OK')

if __name__ == '__main__':
    main()
