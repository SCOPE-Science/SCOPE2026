"""Finite checks for the skew-derivation spectrum of crown incidence algebras.

Uses the defining multiplication and skew Leibniz identity independently
of the combinatorial cochain formula. Only prime fields are enumerated.
"""
from itertools import product


def matrix_rank(rows, p):
    pivots = {}
    for raw in rows:
        row = {j: v % p for j, v in raw.items() if v % p}
        while row:
            j = min(row)
            if j not in pivots:
                inv = pow(row[j], -1, p)
                pivots[j] = {k: (v * inv) % p for k, v in row.items()}
                break
            c = row[j]
            for k, v in pivots[j].items():
                w = (row.get(k, 0) - c * v) % p
                if w:
                    row[k] = w
                else:
                    row.pop(k, None)
    return len(pivots)


def map_poset(m, mode, k):
    low = lambda i: ((i + k) if mode == "rotation" else (k - i)) % m
    high = lambda i: ((i + k) if mode == "rotation" else (k - i - 1)) % m
    return low, high


def cochain_dimensions(m, p, mode, k, weights):
    low, high = map_poset(m, mode, k)
    edges = [(i, j) for i in range(m) for j in (i, (i - 1) % m)]
    allowed = [(i, j) for i, j in edges
               if j in (low(i), (low(i) - 1) % m)]
    fixed = [("a", i) for i in range(m) if low(i) == i] + [
        ("b", j) for j in range(m) if high(j) == j]
    # Coboundary: epsilon(a_i) - sigma(lambda(a_i), lambda(b_j))*epsilon(b_j).
    rows = []
    for i, j in allowed:
        row = {}
        for col, (side, v) in enumerate(fixed):
            w = (int(v == i) if side == "a"
                 else -weights.get((low(i), high(j)), 1) * int(v == j)) % p
            if w:
                row[col] = w
        rows.append(row)
    return len(allowed), matrix_rank(rows, p), len(allowed) - matrix_rank(rows, p)


def predicted(m, p, mode, k, weights):
    if mode == "reflection":
        return 2
    if k % m in (1, m-1):
        return m
    if k % m:
        return 0
    numerator = 1
    denominator = 1
    for i in range(m):
        numerator = numerator * weights.get((i, i), 1) % p
        denominator = denominator * weights.get((i, (i-1) % m), 1) % p
    return int(numerator == denominator)


def direct_dimensions(m, p, mode, k, weights):
    """Solve all skew-Leibniz equations D(xy)=D(x)y+phi(x)D(y)."""
    edges = [(i, j) for i in range(m) for j in (i, (i-1) % m)]
    edge_id = {e: 2*m+t for t, e in enumerate(edges)}
    N = 4*m
    low, high = map_poset(m, mode, k)

    def times(i, j):
        if i < 2*m and j < 2*m:
            return i if i == j else -1
        if i < 2*m <= j:
            return j if i == edges[j-2*m][0] else -1
        if j < 2*m <= i:
            return i if j == m + edges[i-2*m][1] else -1
        return -1

    def phi(i):
        if i < m:
            return low(i), 1
        if i < 2*m:
            return m+high(i-m), 1
        a, b = edges[i-2*m]
        out_edge = (low(a), high(b))
        return edge_id[out_edge], weights.get(out_edge, 1)

    def equations():
        for a in range(N):
            ph_a, coeff = phi(a)
            for b in range(N):
                ab = times(a, b)
                for z in range(N):
                    row = {}
                    if ab >= 0:
                        row[z*N+ab] = 1
                    for v in range(N):
                        if times(v, b) == z:
                            t = v*N+a
                            row[t] = (row.get(t, 0)-1) % p
                        if times(ph_a, v) == z:
                            t = v*N+b
                            row[t] = (row.get(t, 0)-coeff) % p
                    if any(v % p for v in row.values()):
                        yield row

    def inner_equations():
        # u -> (a -> ua - phi(a)u), regarded as a matrix N^2 by N.
        for z in range(N):
            for a in range(N):
                ph_a, coeff = phi(a)
                row = {}
                for u in range(N):
                    w = (int(times(u, a) == z) -
                         coeff * int(times(ph_a, u) == z)) % p
                    if w:
                        row[u] = w
                if row:
                    yield row

    derivation_dim = N*N - matrix_rank(equations(), p)
    inner_dim = matrix_rank(inner_equations(), p)
    return derivation_dim, inner_dim, derivation_dim - inner_dim


def verify():
    cochain_cases = 0
    direct_cases = 0
    for m in range(3, 13):
        for p in (2, 3, 5):
            for mode in ("rotation", "reflection"):
                for k in range(m):
                    for weights in ({}, {(0, 0): 2} if p > 2 else {}):
                        z, b, h = cochain_dimensions(m, p, mode, k, weights)
                        want = predicted(m, p, mode, k, weights)
                        assert h == want, (m, p, mode, k, weights, z, b, h, want)
                        cochain_cases += 1
                        if m <= 5 and p in (2, 3, 5):
                            d, i, actual = direct_dimensions(m, p, mode, k, weights)
                            assert d >= i and actual == want, (
                                m, p, mode, k, weights, d, i, actual, want)
                            direct_cases += 1
    for m in range(3, 20):
        for p in (2, 3, 5):
            # Uniform over Aut(A): each poset symmetry has p-1 outer multiplier classes.
            distribution = {0: 0, 1: 0, 2: 0, m: 0}
            for mode in ("rotation", "reflection"):
                for k in range(m):
                    for t in range(1, p):
                        weights = {(0, 0): t}
                        distribution[predicted(m, p, mode, k, weights)] += 1
            den = 2*m*(p-1)
            assert distribution.get(m) == 2*(p-1)
            assert distribution.get(2) == m*(p-1)
            assert distribution.get(1) == 1
            first = sum(d*n for d, n in distribution.items())
            second = sum(d*d*n for d, n in distribution.items())
            assert first == 4*m*(p-1)+1
            assert second == (2*m*m+4*m)*(p-1)+1
    print('COCHAIN_CASES', cochain_cases)
    print('DIRECT_SKEW_LEIBNIZ_CASES', direct_cases)
    print('PROBABILITY_MOMENT_CASES', 17*3)
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
