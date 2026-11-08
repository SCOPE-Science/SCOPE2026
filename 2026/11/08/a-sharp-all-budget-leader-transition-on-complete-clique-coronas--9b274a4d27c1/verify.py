"""Exact-rational verification of the all-budget complete-clique corona theorem.

Run: python3 verify.py
Only Python standard library is required. This is finite corroboration, not the proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def laplacian(n):
    a = [[0] * (2 * n) for _ in range(2 * n)]
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    edges += [(i, n + i) for i in range(n)]
    for i, j in edges:
        a[i][i] += 1
        a[j][j] += 1
        a[i][j] -= 1
        a[j][i] -= 1
    return a


def invtrace(mat):
    sz = len(mat)
    if not sz:
        return F(0)
    a = [[F(x) for x in row] + [F(i == j) for j in range(sz)]
         for i, row in enumerate(mat)]
    for j in range(sz):
        piv = next(i for i in range(j, sz) if a[i][j])
        a[piv], a[j] = a[j], a[piv]
        z = a[j][j]
        a[j] = [v / z for v in a[j]]
        for i in range(sz):
            if i == j:
                continue
            z = a[i][j]
            if z:
                a[i] = [x - z * y for x, y in zip(a[i], a[j])]
    return sum((a[i][sz + i] for i in range(sz)), F(0))


def objective(n, leaders):
    lead = set(leaders)
    follow = [j for j in range(2 * n) if j not in lead]
    lap = laplacian(n)
    return invtrace([[lap[i][j] for j in follow] for i in follow])


def profile(n, leaders):
    s = set(leaders)
    B = C = L = N = 0
    for i in range(n):
        x, y = i in s, n + i in s
        if x and y: B += 1
        elif x: C += 1
        elif y: L += 1
        else: N += 1
    return (B, C, L, N)


def profile_objective(n, prof):
    B, C, L, N = prof
    if not L + N:
        return F(C)
    h = F(1) - F(N, n) - F(L, n + 1)
    return (F(C + N) + F(L, n + 1) + F(2 * N, n)
            + (F(L, (n + 1) ** 2) + F(2 * N, n ** 2)) / h)


def expected_profiles(n, k):
    if k >= n:
        return {(k - n, 0, 2 * n - k, 0)}
    t = n * k * k + (2 * n * n + 3 * n + 2) * k - 2 * n * (n + 1) ** 2
    result = set()
    if t <= 0:
        result.add((0, 1, k - 1, n - k))
    if t >= 0:
        result.add((0, 0, k, n - k))
    return result


def run():
    full = 0
    for n in range(2, 6):
        opt = {k: (None, set(), 0) for k in range(1, 2 * n + 1)}
        for k in range(1, 2 * n + 1):
            best = None
            best_profiles = set()
            nopts = 0
            for sel in combinations(range(2 * n), k):
                got = objective(n, sel)
                formula = profile_objective(n, profile(n, sel))
                assert got == formula, ('formula', n, k, sel, got, formula)
                full += 1
                if best is None or got < best:
                    best, best_profiles, nopts = got, {profile(n, sel)}, 1
                elif got == best:
                    best_profiles.add(profile(n, sel))
                    nopts += 1
            target = expected_profiles(n, k)
            assert best_profiles == target, ('opt', n, k, best_profiles, target)
            if k < n:
                t = n * k*k + (2*n*n+3*n+2)*k - 2*n*(n+1)**2
                count = (n * comb(n - 1, k - 1) if t <= 0 else 0) + (comb(n, k) if t >= 0 else 0)
            else:
                count = comb(n, k - n)
            assert count == nopts, ('count', n, k, count, nopts)
    profiles = 0
    for n in range(2, 61):
        for k in range(1, 2 * n + 1):
            eligible = []
            for B in range(n + 1):
                for C in range(n - B + 1):
                    for L in range(n - B - C + 1):
                        N = n - B - C - L
                        if 2 * B + C + L == k:
                            eligible.append((profile_objective(n, (B, C, L, N)), (B, C, L, N)))
                            profiles += 1
            optimal = min(v for v, _ in eligible)
            winners = {p for v, p in eligible if v == optimal}
            assert winners == expected_profiles(n, k), ('profiles', n, k, winners, expected_profiles(n, k))
    print(f'PASS: {full} exhaustive exact grounded-matrix calculations on n=2..5; '
          f'{profiles} exact occupancy comparisons on n=2..60.')


if __name__ == '__main__':
    run()
