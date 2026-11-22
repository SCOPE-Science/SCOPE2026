"""Independent exact-rational checks of Kemeny cycle identities.

Run: python3 verify.py. Only Python standard library is needed.
The symbolic all-size and continuous-parameter proofs are in RESULT.md;
this script checks finite instances, not universal quantified assertions.
"""
from fractions import Fraction as F


def resistance_kemeny(weights):
    ws = [F(x) for x in weights]
    n = len(ws)
    assert n >= 3 and all(x > 0 for x in ws)
    m = sum(ws)
    deg = [ws[(i - 1) % n] + ws[i] for i in range(n)]
    r = [1 / x for x in ws]
    total = sum(r)
    k = F(0)
    for i in range(n):
        partial = F(0)
        for j in range(i + 1, n):
            partial += r[j - 1]
            effective = partial * (total - partial) / total
            k += deg[i] * deg[j] * effective
    return k / (2 * m)


def solve_fraction(a, b):
    a = [[F(x) for x in row] for row in a]
    b = [F(x) for x in b]
    n = len(b)
    for p in range(n):
        q = next(j for j in range(p, n) if a[j][p] != 0)
        a[p], a[q] = a[q], a[p]
        b[p], b[q] = b[q], b[p]
        pivot = a[p][p]
        for k in range(p, n):
            a[p][k] /= pivot
        b[p] /= pivot
        for j in range(n):
            if j == p:
                continue
            factor = a[j][p]
            for k in range(p, n):
                a[j][k] -= factor * a[p][k]
            b[j] -= factor * b[p]
    return b


def hitting_kemeny(weights):
    ws = [F(x) for x in weights]
    n = len(ws)
    deg = [ws[(i - 1) % n] + ws[i] for i in range(n)]
    pi = [di / sum(deg) for di in deg]
    trans = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, w in enumerate(ws):
        j = (i + 1) % n
        trans[i][j] = w / deg[i]
        trans[j][i] = w / deg[j]
    K = F(0)
    for target in range(1, n):
        states = [i for i in range(n) if i != target]
        a = [[F(int(i == j)) - trans[i][j] for j in states] for i in states]
        h = solve_fraction(a, [F(1)] * (n - 1))
        K += pi[target] * h[states.index(0)]
    return K


def defect_formula(n, w):
    m, w = n - 1, F(w)
    return F(m, 6) * ((2 * m * m + 1) * (w * w + 1) + m * (m * m + 5) * w) / ((m + w) * (m * w + 1))


def defect_gap(n, w):
    m, w = n - 1, F(w)
    return F(m * (m - 1) ** 2, 6) * (w - 1) ** 2 / ((m + w) * (m * w + 1))


def five_formula(e):
    e = F(e)
    return F(4) - 2 * e * e / (5 * (5 - e * e))


def main():
    checks = 0
    for n in range(3, 24):
        baseline = F(n * n - 1, 6)
        assert resistance_kemeny([1] * n) == baseline
        checks += 1
        for w in [F(1, 5), F(1, 2), F(2, 3), F(1), F(5, 4), F(2), F(7, 2), F(10)]:
            test = [F(1)] * (n - 1) + [w]
            k = resistance_kemeny(test)
            assert k == defect_formula(n, w)
            assert k - baseline == defect_gap(n, w)
            assert (k == baseline) == (w == 1)
            checks += 3
            if n <= 9:
                assert k == hitting_kemeny(test)
                checks += 1
    for e in [F(-4, 5), F(-3, 4), F(-1, 2), F(-1, 3), F(-1, 5), F(0), F(1, 5), F(1, 3), F(1, 2), F(3, 4), F(4, 5)]:
        ws = [1 + e, 1 + e, F(1), 1 - e, 1 - e]
        k = resistance_kemeny(ws)
        assert k == five_formula(e)
        assert k == hitting_kemeny(ws)
        assert (k < 4) == (e != 0)
        checks += 3
    for ws in [[F(1), F(2), F(3), F(6)], [F(2), F(3), F(6), F(4)], [F(1), F(2), F(3), F(4)], [F(3), F(3), F(3), F(3)]]:
        k = resistance_kemeny(ws)
        assert (k == F(5, 2)) == (ws[0] * ws[2] == ws[1] * ws[3])
        assert k == hitting_kemeny(ws)
        checks += 2
    for ws in [[F(1), F(2), F(3)], [F(1), F(1), F(1)], [F(2), F(3), F(7)]]:
        k = resistance_kemeny(ws)
        assert k >= F(4, 3)
        assert (k == F(4, 3)) == (ws[0] == ws[1] == ws[2])
        assert k == hitting_kemeny(ws)
        checks += 3
    print('PASS:', checks, 'exact rational comparisons')
    print('C5, e=1/2: K=', resistance_kemeny([F(3, 2), F(3, 2), 1, F(1, 2), F(1, 2)]))


if __name__ == '__main__':
    main()
