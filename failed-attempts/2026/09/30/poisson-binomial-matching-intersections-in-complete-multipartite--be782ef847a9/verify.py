#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for tail in partitions(n - x, x):
            yield (x,) + tail


def bareiss_det(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            r = next((r for r in range(k + 1, n) if A[r][k]), None)
            if r is None:
                return 0
            A[k], A[r] = A[r], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
        for j in range(k + 1, n):
            A[k][j] = 0
    return sign * A[-1][-1]


def vertices(parts):
    return [(i, a) for i, n in enumerate(parts) for a in range(n)]


def edges(parts):
    V = vertices(parts)
    return V, [(u, v) for u, v in combinations(range(len(V)), 2)
               if V[u][0] != V[v][0]]


def tau(parts):
    N = sum(parts)
    s = len(parts)
    ans = N ** (s - 2)
    for n in parts:
        ans *= (N - n) ** (n - 1)
    return ans


def predicted_joint(parts, i, j, q):
    N = sum(parts)
    sigma = Fraction(1, N - parts[i]) + Fraction(1, N - parts[j])
    return Fraction(tau(parts)) * Fraction(N - q, N) * sigma ** q


def contracted_count(parts, i, j, q):
    V, E = edges(parts)
    parent = list(range(len(V)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    idx = {v: k for k, v in enumerate(V)}
    for a in range(q):
        union(idx[(i, a)], idx[(j, a)])

    roots = {}
    for v in range(len(V)):
        r = find(v)
        if r not in roots:
            roots[r] = len(roots)

    n = len(roots)
    L = [[0] * n for _ in range(n)]
    for u, v in E:
        a, b = roots[find(u)], roots[find(v)]
        if a == b:
            continue
        L[a][a] += 1
        L[b][b] += 1
        L[a][b] -= 1
        L[b][a] -= 1
    return bareiss_det([row[:-1] for row in L[:-1]])


def is_tree(n, chosen, E):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for ei in chosen:
        u, v = E[ei]
        u, v = find(u), find(v)
        if u == v:
            return False
        parent[v] = u
    return True


def brute_distribution(parts, i, j, m):
    V, E = edges(parts)
    idx = {v: k for k, v in enumerate(V)}
    edge_index = {e: k for k, e in enumerate(E)}
    M = set()
    for a in range(m):
        u, v = idx[(i, a)], idx[(j, a)]
        if u > v:
            u, v = v, u
        M.add(edge_index[(u, v)])
    counts = [0] * (m + 1)
    for chosen in combinations(range(len(E)), len(V) - 1):
        if is_tree(len(V), chosen, E):
            counts[sum(e in M for e in chosen)] += 1
    return counts


def predicted_distribution(parts, i, j, m):
    N = sum(parts)
    sigma = Fraction(1, N - parts[i]) + Fraction(1, N - parts[j])
    beta = sigma * Fraction(N - m, N)
    p = [Fraction(1)]
    for _ in range(m - 1):
        q = [Fraction(0)] * (len(p) + 1)
        for k, x in enumerate(p):
            q[k] += x * (1 - sigma)
            q[k + 1] += x * sigma
        p = q
    q = [Fraction(0)] * (len(p) + 1)
    for k, x in enumerate(p):
        q[k] += x * (1 - beta)
        q[k + 1] += x * beta
    total = tau(parts)
    ans = []
    for x in q:
        y = x * total
        assert y.denominator == 1
        ans.append(y.numerator)
    return ans


types = 0
joint_checks = 0
for N in range(2, 9):
    for parts in partitions(N):
        if len(parts) < 2:
            continue
        types += 1
        for i, j in combinations(range(len(parts)), 2):
            for q in range(1, min(parts[i], parts[j]) + 1):
                got = contracted_count(parts, i, j, q)
                want = predicted_joint(parts, i, j, q)
                assert want.denominator == 1
                assert got == want.numerator, (parts, i, j, q, got, want)
                joint_checks += 1

distribution_checks = 0
for N in range(2, 7):
    for parts in partitions(N):
        if len(parts) < 2:
            continue
        for i, j in combinations(range(len(parts)), 2):
            m = min(parts[i], parts[j])
            got = brute_distribution(parts, i, j, m)
            want = predicted_distribution(parts, i, j, m)
            assert got == want, (parts, i, j, m, got, want)
            distribution_checks += 1

assert types == 58
assert joint_checks == 394
assert distribution_checks == 89
print("VERIFIED 58 complete multipartite types through order 8")
print("JOINT_INCLUSION_CHECKS 394")
print("FULL_DISTRIBUTION_CHECKS 89")
print("VERIFY_OK")
