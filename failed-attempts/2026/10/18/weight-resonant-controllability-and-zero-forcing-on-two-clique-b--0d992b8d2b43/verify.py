"""Finite reproducibility checks for weighted two-clique bridge networks.

Run with Python 3.9+; no nonstandard dependencies.
Finite checks corroborate, but do not establish, the all-orders theorem.
"""
from collections import Counter
from itertools import combinations


def rank_mod(rows, prime=1000000007):
    rows = [[int(y) % prime for y in row] for row in rows]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    pivot = 0
    for col in range(n):
        index = next((i for i in range(pivot, m) if rows[i][col]), None)
        if index is None:
            continue
        rows[pivot], rows[index] = rows[index], rows[pivot]
        factor = pow(rows[pivot][col], prime - 2, prime)
        rows[pivot] = [(v * factor) % prime for v in rows[pivot]]
        for i in range(m):
            if i != pivot and rows[i][col]:
                multiplier = rows[i][col]
                rows[i] = [(rows[i][j] - multiplier * rows[pivot][j]) % prime
                           for j in range(n)]
        pivot += 1
        if pivot == m:
            break
    return pivot


def laplacian(p, q, a, b, c):
    n = p + q
    L = [[0] * n for _ in range(n)]
    for start, size, weight in [(0, p, a), (p, q, b)]:
        for i in range(start, start + size):
            for j in range(i + 1, start + size):
                L[i][i] += weight
                L[j][j] += weight
                L[i][j] -= weight
                L[j][i] -= weight
    L[0][0] += c
    L[p][p] += c
    L[0][p] -= c
    L[p][0] -= c
    return L


def reachability_rank(L, selected):
    """Exact rank modulo a prime of the complete Kalman matrix."""
    n = len(L)
    cols = []
    for j in selected:
        v = [int(i == j) for i in range(n)]
        for _ in range(n):
            cols.append(v)
            v = [sum(L[i][k] * v[k] for k in range(n)) for i in range(n)]
    return rank_mod([[column[i] for column in cols] for i in range(n)])


def criterion(p, q, a, b, selected):
    S = set(selected)
    left = sum(i in S for i in range(1, p))
    right = sum(i in S for i in range(p + 1, p + q))
    return (left >= p - 2 and right >= q - 2
            and (a * p != b * q or len(S) >= p + q - 3))


def zero_forcing(p, q, selected):
    n = p + q
    blue = set(selected)
    adj = [set() for _ in range(n)]
    for start, size in [(0, p), (p, q)]:
        for i in range(start, start + size):
            adj[i].update(range(start, start + size))
            adj[i].remove(i)
    adj[0].add(p)
    adj[p].add(0)
    while True:
        if len(blue) == n:
            return True
        forced = set()
        for i in blue:
            white = adj[i] - blue
            if len(white) == 1:
                forced.update(white)
        if not forced:
            return False
        blue.update(forced)


def expected_poly(p, q, resonance):
    """Coefficients of the analytically predicted controllability polynomial."""
    poly = Counter({p + q - 4: (p - 1) * (q - 1),
                    p + q - 3: p + q - 2,
                    p + q - 2: 1})
    for _ in range(2):
        next_poly = Counter()
        for degree, coefficient in poly.items():
            next_poly[degree] += coefficient
            next_poly[degree + 1] += coefficient
        poly = next_poly
    if resonance:
        poly[p + q - 4] -= (p - 1) * (q - 1)
    return +poly


def run():
    checks = 0
    cases = 0
    for p in range(3, 6):
        for q in range(3, 6):
            for a, b, c in sorted({(1, 1, 1), (1, 2, 1),
                                    (2, 1, 3), (q, p, 2)}):
                n = p + q
                L = laplacian(p, q, a, b, c)
                counts = Counter()
                resonance = (a * p == b * q)
                for size in range(n + 1):
                    for subset in combinations(range(n), size):
                        predicted = criterion(p, q, a, b, subset)
                        rank = reachability_rank(L, subset)
                        assert (rank == n) == predicted, (p, q, a, b, c, subset, rank)
                        checks += 1
                        zf = zero_forcing(p, q, subset)
                        zf_predicted = criterion(p, q, q, p, subset)
                        assert zf == zf_predicted, (p, q, subset)
                        assert zf <= predicted, (p, q, a, b, c, subset)
                        checks += 2
                        if predicted:
                            counts[size] += 1
                assert counts == expected_poly(p, q, resonance), (p, q, a, b, c, counts)
                checks += 1
                minimum = min(counts)
                assert minimum == (p + q - 3 if resonance else p + q - 4)
                checks += 1
                cases += 1
    print('VERIFY_OK', checks, 'finite assertions across', cases,
          'weighted cases (3<=p,q<=5), using exact prime-field ranks')

if __name__ == '__main__':
    run()
