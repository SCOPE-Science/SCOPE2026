"""Exact low-degree Fourier checks for transitive-tournament comparison vectors.
Run: python3 verify.py . No third-party dependencies.
"""
from itertools import combinations, permutations
from math import comb, factorial


def signed_subset_dp(n, edges):
    hi = [0] * n
    for u, v in edges:
        if u > v: u, v = v, u
        hi[u] |= 1 << v
    dp = [0] * (1 << n)
    dp[0] = 1
    for mask in range(1, 1 << n):
        z = mask
        total = 0
        while z:
            bit = z & -z
            z -= bit
            v = bit.bit_length() - 1
            remaining = mask ^ bit
            parity = (hi[v] & remaining).bit_count() % 2
            total += (-1 if parity else 1) * dp[remaining]
        dp[mask] = total
    return dp[-1]


def expected_abs(n, edges):
    m = len(edges)
    if m == 0: return factorial(n)
    if m in (1, 3): return 0
    vertices = set(v for e in edges for v in e)
    adj = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    components = []
    todo = set(vertices)
    while todo:
        v = todo.pop()
        comp = {v}
        frontier = [v]
        while frontier:
            u = frontier.pop()
            for w in adj[u]:
                if w not in comp:
                    comp.add(w)
                    todo.discard(w)
                    frontier.append(w)
        components.append(comp)
    if m == 2:
        return factorial(n) // 3 if len(components)==1 else 0
    if len(components) == 2 and sorted(map(len, components)) == [3,3]:
        return factorial(n) // 9
    if len(components) != 1:
        return 0
    d = sorted((len(adj[v]) for v in vertices), reverse=True)
    if d == [2,2,2,2]: return factorial(n) // 3
    if d == [4,1,1,1,1]: return factorial(n) // 5
    if d == [3,2,1,1,1]: return factorial(n) // 15
    if d == [2,2,2,1,1]: return (2 * factorial(n)) // 15
    return 0


def direct_sums(n):
    edges = list(combinations(range(n), 2))
    masks = []
    for pi in permutations(range(n)):
        positions = [0]*n
        for i, v in enumerate(pi): positions[v] = i
        mask = sum(1 << j for j,(u,v) in enumerate(edges)
                   if positions[u] > positions[v])
        masks.append(mask)
    counts = [0]*5
    for m in range(5):
        for idxs in combinations(range(len(edges)),m):
            mask = sum(1 << j for j in idxs)
            actual = sum(1 if (p & mask).bit_count() % 2 == 0 else -1
                         for p in masks)
            want = expected_abs(n,[edges[i] for i in idxs])
            assert abs(actual) == want, (n,idxs,actual,want)
            if want: counts[m] += 1
    return counts


def formula(n):
    return (1 + 3*comb(n,3) + 3*comb(n,4) + 125*comb(n,5)
            + 90*comb(n,6))

if __name__ == '__main__':
    for n in (4,5,6):
        counts = direct_sums(n)
        assert sum(counts)==formula(n)
        assert counts[1]==counts[3]==0
        print('direct',n,counts, 'rank',sum(counts))
    motifs = [
        (3,[(0,1),(0,2)],2),
        (4,[(0,1),(2,3)],0),
        (4,[(0,1),(1,2),(2,3),(3,0)],8),
        (4,[(0,1),(1,2),(2,0),(2,3)],0),
        (5,[(0,1),(0,2),(0,3),(0,4)],24),
        (5,[(0,1),(0,2),(0,3),(1,4)],8),
        (5,[(0,1),(1,2),(2,3),(3,4)],16),
        (6,[(0,1),(0,2),(3,4),(3,5)],80),
    ]
    for k,e,w in motifs:
        x=signed_subset_dp(k,e)
        assert abs(x)==w, (k,e,x,w)
    print('subset dynamic program: all 8 motif checks passed')
    print('all assertions passed')
