#!/usr/bin/env python3
"""Direct checks of nilpotent multiplication ranks in graph face algebras.

No third-party modules are needed.  Field order four uses F2[t]/(t^2+t+1).
"""
from collections import Counter
from itertools import combinations, product


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def neg(a, q):
    return a if q == 4 else (-a) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return out


def inv(a, q):
    assert a
    return next(b for b in range(1, q) if mul(a, b, q) == 1)


def rank(rows, q):
    a = [row[:] for row in rows]
    if not a:
        return 0
    m, n, k = len(a), len(a[0]), 0
    for j in range(n):
        i = next((h for h in range(k, m) if a[h][j]), None)
        if i is None:
            continue
        a[k], a[i] = a[i], a[k]
        u = inv(a[k][j], q)
        a[k] = [mul(u, t, q) for t in a[k]]
        for h in range(k + 1, m):
            if a[h][j]:
                t = a[h][j]
                a[h] = [add(v, neg(mul(t, w, q), q), q) for v, w in zip(a[h], a[k])]
        k += 1
        if k == m:
            break
    return k


def graph_edges(n, bits):
    return [edge for i, edge in enumerate(combinations(range(n), 2)) if (bits >> i) & 1]


def predicted(n, edges, q, refined=False):
    m = len(edges)
    key = (lambda r, s, t: (r, s, t)) if refined else (lambda r, s, t: (r, s))
    ans = Counter({key(0, 0, 0): 1})
    ans[key(1, 0, 0)] += q**m - 1
    for mask in range(1, 1 << n):
        support = {i for i in range(n) if (mask >> i) & 1}
        free = sum(all((min(v, s), max(v, s)) not in edges for s in support)
                   for v in range(n) if v not in support)
        visited, components = set(), 0
        for x in support:
            if x in visited:
                continue
            colors = {x: 0}
            todo, bipartite = [x], True
            while todo:
                u = todo.pop()
                for v in support:
                    if u == v or (min(u, v), max(u, v)) not in edges:
                        continue
                    if v not in colors:
                        colors[v] = 1 - colors[u]
                        todo.append(v)
                    elif colors[v] == colors[u]:
                        bipartite = False
            visited.update(colors)
            if q % 2 == 0 or bipartite:
                components += 1
        r = 1 + n - free - components
        s = int(q % 2 != 0 and any(i in support and j in support for i, j in edges))
        ans[key(r, s, len(support))] += q**m * (q - 1)**len(support)
    return +ans


def operator(n, edges, q, a, b):
    d = 1 + n + len(edges)
    L = [[0] * d for _ in range(d)]
    for i, x in enumerate(a):
        L[1 + i][0] = x
    for e, val in enumerate(b):
        L[1 + n + e][0] = val
    for e, (i, j) in enumerate(edges):
        L[1 + n + e][1 + i] = a[j]
        L[1 + n + e][1 + j] = a[i]
    LL = [[0] * d for _ in range(d)]
    for i in range(d):
        for k in range(d):
            if L[i][k]:
                for j in range(d):
                    LL[i][j] = add(LL[i][j], mul(L[i][k], L[k][j], q), q)
    return rank(L, q), rank(LL, q)


def full_check(n, edges, q):
    actual = Counter()
    refined = Counter()
    for a in product(range(q), repeat=n):
        for b in product(range(q), repeat=len(edges)):
            r, s = operator(n, edges, q, a, b)
            actual[(r, s)] += 1
            refined[(r, s, sum(bool(t) for t in a))] += 1
    theory = predicted(n, edges, q)
    assert actual == theory, (n, edges, q, actual, theory)
    assert refined == predicted(n, edges, q, refined=True), (n, edges, q, refined)
    assert sum(actual.values()) == q**(n + len(edges))
    return len(actual)


def support_check(n, edges, q):
    m = len(edges)
    counter = Counter()
    for a in product(range(q), repeat=n):
        got = operator(n, edges, q, a, (0,)*m)
        if any(a):
            counter[got] += q**m
        else:
            counter[(0, 0)] += 1
            counter[(1, 0)] += q**m-1
    assert counter == predicted(n, edges, q), (n, edges, q, counter, predicted(n, edges, q))


def main():
    complete = 0
    for q, largest in ((2, 4), (3, 3), (4, 3)):
        for n in range(1, largest + 1):
            for bits in range(1 << (n * (n - 1) // 2)):
                full_check(n, graph_edges(n, bits), q)
                complete += 1
    paw = [(0,1), (0,2), (0,3), (1,2)]
    cycle = [(0,2), (0,3), (1,2), (1,3)]
    for es in (paw, cycle):
        full_check(4, es, 3)
        complete += 1
    sampled = 0
    for q in (3, 5):
        for bits in range(1 << 6):
            support_check(4, graph_edges(4, bits), q)
            sampled += 1
    print('ALL_GRAPH_FACE_JORDAN_CHECKS_PASSED', complete, 'full configurations,', sampled, 'support configurations')
    print('PAW_F2', sorted(predicted(4, paw, 2).items()))
    print('C4_F2', sorted(predicted(4, cycle, 2).items()))
    print('PAW_F3', sorted(predicted(4, paw, 3).items()))
    print('C4_F3', sorted(predicted(4, cycle, 3).items()))

if __name__ == '__main__':
    main()
