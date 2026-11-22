"""Independent finite checks for minimum-domination slides on cycles.
Uses only Python's standard library; no data files or network required.
"""
from itertools import combinations
from collections import deque, Counter


def dominating(S, n):
    return all(any((v + h) % n in S for h in (-1, 0, 1)) for v in range(n))


def excess_pair(S, n):
    excess = [v for v in range(n) if sum((v + h) % n in S for h in (-1, 0, 1)) == 2]
    assert len(excess) == 2
    assert all(sum((v + h) % n in S for h in (-1, 0, 1)) <= 2 for v in range(n))
    inverse3 = pow(3, -1, n)
    return frozenset((v * inverse3) % n for v in excess)


def target_pairs(n, d):
    return {frozenset((a, b)) for a in range(n) for b in range(a + 1, n)
            if min(b - a, n - (b - a)) >= d}


def slides(S, n):
    for x in S:
        for step in (-1, 1):
            y = (x + step) % n
            if y not in S:
                yield frozenset((S - {x}) | {y})


def token_slides(P, n, allowed):
    return set(Q for Q in slides(P, n) if Q in allowed)


def mobius_distance(P, Q, n):
    a, b = sorted(P)
    c, e = sorted(Q)
    copies = ((c, e), (e, c + n), (e - n, c), (c + n, e + n), (c - n, e - n))
    return min(abs(a - u) + abs(b - v) for u, v in copies)


def bfs(source, adj):
    ds = {source: 0}
    dq = deque([source])
    while dq:
        x = dq.popleft()
        for y in adj[x]:
            if y not in ds:
                ds[y] = ds[x] + 1
                dq.append(y)
    return ds


def check(n):
    m = (n + 2) // 3
    d = m - 1
    states = [frozenset(c) for c in combinations(range(n), m)
              if dominating(frozenset(c), n)]
    state_set = set(states)
    assert len(states) == n * (m + 1) // 2
    pairs = target_pairs(n, d)
    phi = {S: excess_pair(S, n) for S in states}
    assert set(phi.values()) == pairs
    assert len(phi) == len(pairs)
    g = {S: set(T for T in slides(S, n) if T in state_set) for S in states}
    h = {P: token_slides(P, n, pairs) for P in pairs}
    assert all(set(map(phi.get, g[S])) == h[phi[S]] for S in states)
    degree_hist = Counter(map(len, g.values()))
    assert degree_hist == Counter({2: n, 4: n * (m - 1) // 2})
    assert sum(map(len, g.values())) // 2 == n * m
    diam = (n // 2)
    examined = 0
    for S in states:
        ds = bfs(S, g)
        assert len(ds) == len(states)
        assert max(ds.values()) == diam
        for T, distance in ds.items():
            assert distance == mobius_distance(phi[S], phi[T], n), (n, S, T, distance)
            examined += 1
    return n, len(states), examined


if __name__ == '__main__':
    pairs_checked = 0
    for n in (4, 7, 10, 13, 16, 19):
        n, states, ordered_pairs = check(n)
        pairs_checked += ordered_pairs
        print(f'PASS n={n}, states={states}, ordered_pairs={ordered_pairs}')
    print(f'ALL_VERIFY_OK: {pairs_checked} ordered source-target pairs; exact graph-to-strip isomorphism')
