"""Exact arithmetic checks for spectral allocations on complete split graphs.

Run: python3 verify.py. Python standard library only. Finite checks supplement
rather than replace the proof for all parameters.
"""
from fractions import Fraction as F
from itertools import product


def graph_laplacian(p, q, x, y):
    n = p + q
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            w = y if i < p and j < p else x if (i < p <= j) else F(0)
            if w:
                L[i][i] += w
                L[j][j] += w
                L[i][j] -= w
                L[j][i] -= w
    return L


def matrix_times(L, vector):
    return [sum(L[i][j] * vector[j] for j in range(len(vector)))
            for i in range(len(vector))]


def expected_eigenvectors(p, q):
    n = p + q
    yield [F(1)] * n, F(0)
    for k in range(1, p):
        v = [F(0)] * n
        v[0], v[k] = F(1), F(-1)
        yield v, None  # q*x+p*y
    for k in range(1, q):
        v = [F(0)] * n
        v[p], v[p + k] = F(1), F(-1)
        yield v, None  # p*x
    yield [F(q)] * p + [F(-p)] * q, None  # (p+q)*x


def optimum(p, q, A, C, B):
    if q >= p:
        t = B / (q * A)
        return t, t / p, F(0), 'clique-unused'
    H1 = q * A + F((p - 1) * (p - q), 2 * p) * C
    H2 = p * A
    if H1 < H2:
        t = B / H1
        return t, t / p, t * (p - q) / (p * p), 'clique-used'
    if H2 < H1:
        t = B / H2
        return t, t / q, F(0), 'clique-unused'
    t = B / H1
    return t, t / p, t * (p - q) / (p * p), 'degenerate-interval'


def eigencheck(p, q, x, y):
    L = graph_laplacian(p, q, x, y)
    names = []
    for k, (v, _) in enumerate(expected_eigenvectors(p, q)):
        lam = (F(0) if k == 0 else
               (q * x + p * y if k < p else
               (p * x if k < p + q - 1 else (p + q) * x)))
        assert matrix_times(L, v) == [lam * vv for vv in v]
        names.append(lam)
    assert sorted(names)[0] == 0
    assert sorted(names)[1] == min(p*x, q*x + p*y)
    return 1


def run():
    cases = 0
    for p, q, A, C, B in product(range(2, 8), range(2, 8),
                                  [F(1), F(3, 2)],
                                  [F(1, 5), F(1), F(2), F(4), F(9)],
                                  [F(1), F(7, 3)]):
        t, x, y, phase = optimum(p, q, A, C, B)
        assert x > 0 and y >= 0
        assert p*q*A*x + F(p*(p-1), 2)*C*y == B
        assert min(p*x, q*x + p*y) == t
        assert eigencheck(p, q, x, y)
        # Closed-form bound over 100 equally spaced symmetric test rates.
        for j in range(101):
            xx = B * F(j, 100) / (p*q*A)
            yy = (B - p*q*A*xx) / (F(p*(p-1), 2)*C)
            assert min(p*xx, q*xx+p*yy) <= t
        if q < p and C == F(2*p, p-1)*A:
            for k in range(11):
                x2 = t/p + F(k,10)*(t/q-t/p)
                y2 = (t-q*x2)/p
                assert p*q*A*x2 + F(p*(p-1),2)*C*y2 == B
                assert min(p*x2, q*x2+p*y2) == t
        cases += 1
    print('VERIFY_OK', cases, 'exact matrix and optimum cases;',
          cases*101, 'rational rate bounds')


if __name__ == '__main__':
    run()
