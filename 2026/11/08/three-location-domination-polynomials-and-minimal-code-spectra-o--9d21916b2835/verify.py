"""Literal finite neighborhood checks on the prism and its crown complement."""
from collections import Counter
from itertools import combinations
from math import comb


def is_code(C, neighborhoods):
    outsiders = set(range(len(neighborhoods))) - C
    traces = {v: neighborhoods[v] & C for v in outsiders}
    if not all(traces.values()):
        return False, False
    self_locating = all(set.intersection(*(neighborhoods[u] for u in T)) == {v}
                        for v, T in traces.items())
    solid = not any(X <= Y or Y <= X for X, Y in combinations(traces.values(), 2))
    return self_locating, solid


def check(n):
    V = set(range(2*n))
    prism = [{u for u in V if u//n == v//n or u%n == v%n} for v in range(2*n)]
    crown = [(V-N) | {v} for v, N in enumerate(prism)]
    S, joint = set(), set()
    for k in range(2*n+1):
        for vertices in combinations(range(2*n), k):
            C = frozenset(vertices)
            sp, dp = is_code(C, prism)
            sc, dc = is_code(C, crown)
            assert dp == dc
            if sp:
                S.add(C)
                if sc:
                    joint.add(C)
    F = Counter({n+j: comb(n,j)*2**(n-j) for j in range(n+1)})
    F[n] -= 2*(n+1)
    F[n+1] -= 2*n
    J = Counter({n+j: 2*comb(n,j) for j in range(2,n+1)})
    J[2*n] -= 1
    assert Counter(map(len,S)) == F
    assert Counter(map(len,joint)) == J
    assert Counter(len(C) for C in S if all(C-{v} not in S for v in C)) == {n: 2**n-2*n-2}


if __name__ == '__main__':
    for n in (4,5,6):
        check(n)
    print('VERIFY_OK subsets_per_graph=5376')
