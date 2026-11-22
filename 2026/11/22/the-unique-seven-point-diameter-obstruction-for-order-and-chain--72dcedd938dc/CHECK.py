"""Exhaustive integer certificate for the minimal order/chain-diameter split.

Run: python3 CHECK.py
No third-party dependencies. The mathematical edge criteria are those quoted
in Jon Lee, arXiv:2610.07413, Theorem 1.5.
"""
from collections import deque
from itertools import combinations, permutations


def closure(n, code):
    """Strict transitive closure of the upward-labelled generating relation."""
    rows = [0] * n
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (code >> k) & 1:
                rows[i] |= 1 << j
            k += 1
    for j in range(n - 1, -1, -1):
        for i in range(j):
            if rows[i] & (1 << j):
                rows[i] |= rows[j]
    return tuple(rows)


def contains_X(rows):
    """The 5-element induced two-low/one-middle/two-high poset."""
    n = len(rows)
    for c in range(n):
        lows = [a for a in range(c) if rows[a] & (1 << c)]
        highs = [a for a in range(c + 1, n) if rows[c] & (1 << a)]
        for a, b in combinations(lows, 2):
            if rows[a] & (1 << b):
                continue
            for g, h in combinations(highs, 2):
                if not rows[g] & (1 << h):
                    return True
    return False


def connected(mask, comparability):
    """Connectivity in the undirected comparability graph restricted to mask."""
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        index = bit.bit_length() - 1
        fresh = comparability[index] & mask & ~reached
        reached |= fresh
        frontier |= fresh
    return mask != 0 and reached == mask


def diameter(vertices, comparability, need_containment):
    m = len(vertices)
    adj = [[] for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            x, y = vertices[i], vertices[j]
            if need_containment and ((x & y) != x) and ((x & y) != y):
                continue
            if connected(x ^ y, comparability):
                adj[i].append(j)
                adj[j].append(i)
    answer = 0
    for root in range(m):
        distance = [-1] * m
        distance[root] = 0
        q = deque([root])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if distance[w] == -1:
                    distance[w] = distance[v] + 1
                    q.append(w)
        assert -1 not in distance, 'polytope graph cannot disconnect'
        answer = max(answer, max(distance))
    return answer


def order_and_chain_diameters(rows):
    n = len(rows)
    below = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if rows[i] & (1 << j):
                below[j] |= 1 << i
    comparability = [rows[i] | below[i] for i in range(n)]
    ideals = []
    antichains = []
    for s in range(1 << n):
        if all(not(s & (1 << i)) or ((s & below[i]) == below[i])
               for i in range(n)):
            ideals.append(s)
        if all(not(s & (1 << i)) or (s & comparability[i]) == 0
               for i in range(n)):
            antichains.append(s)
    assert len(ideals) == len(antichains)
    return (diameter(ideals, comparability, True),
            diameter(antichains, comparability, False))


def canonical(rows):
    """Isomorphism-free code over all simultaneous relabellings."""
    n = len(rows)
    optimum = None
    for permutation in permutations(range(n)):
        code = 0
        for i in range(n):
            for j in range(n):
                if rows[permutation[i]] & (1 << permutation[j]):
                    code |= 1 << (n * i + j)
        if optimum is None or code < optimum:
            optimum = code
    return optimum


def dual(rows):
    n = len(rows)
    return tuple(sum(1 << j for j in range(n) if rows[j] & (1 << i))
                 for i in range(n))


def enumerate_posets(n):
    """Exhaust all orders by fixing an arbitrary linear extension."""
    seen = set()
    for code in range(1 << (n * (n - 1) // 2)):
        relation = closure(n, code)
        if relation not in seen:
            seen.add(relation)
            yield relation


def main():
    totals = {}
    exceptional = []
    for n in (4, 5, 6, 7):
        all_count = x_count = bad_count = 0
        for rows in enumerate_posets(n):
            all_count += 1
            if not contains_X(rows):
                continue  # X-free pairs are unimodularly equivalent.
            x_count += 1
            d_o, d_c = order_and_chain_diameters(rows)
            if d_o != d_c:
                bad_count += 1
                if n == 7:
                    exceptional.append((rows, d_o, d_c))
        totals[n] = (all_count, x_count, bad_count)
        print(n, all_count, x_count, bad_count)
    assert totals == {4:(40,0,0), 5:(357,1,0),
                      6:(4824,66,0), 7:(96428,3705,46)}
    assert len(exceptional) == 46
    assert {(a, b) for _,a,b in exceptional} == {(2, 3)}
    groups = {}
    for rows, a, b in exceptional:
        key = canonical(rows)
        groups.setdefault(key, []).append(rows)
    assert sorted(map(len, groups.values())) == [23, 23]
    keys = sorted(groups)
    assert keys == [8658630260, 8725738108]
    assert canonical(dual(groups[keys[0]][0])) == keys[1]
    # P1 of Lee's Proposition 4.41(i), with order a,b,c,p,q,g,h.
    p1 = (124, 100, 96, 32, 64, 0, 0)
    assert canonical(p1) in keys
    assert order_and_chain_diameters(p1) == (2, 3)
    print('Two isomorphism types, exchanged by duality; Lee P1 representative.')
    print('PASS')

if __name__ == '__main__':
    main()
