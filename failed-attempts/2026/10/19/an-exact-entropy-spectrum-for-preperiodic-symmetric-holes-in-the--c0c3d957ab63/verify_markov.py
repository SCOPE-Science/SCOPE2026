"""Exact finite consistency checks for symmetric negative-doubling survivor partitions.

Run: python3 verify_markov.py (Python 3 standard library only).
All rational computations and polynomial coefficients are exact.
The unbounded parameter theorem requires the accompanying mathematical proof.
"""
from fractions import Fraction as F
from math import log


def polytimes(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][h] * b[h][j] for h in range(n))
             for j in range(n)] for i in range(n)]


def charpoly(a):
    """Faddeev-LeVerrier, exact integer output for an integer matrix."""
    n = len(a)
    v = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    ac = [[F(x) for x in row] for row in a]
    coeff = [1]
    for k in range(1, n + 1):
        w = matmul(ac, v)
        c = -sum(w[i][i] for i in range(n)) / k
        assert c.denominator == 1
        coeff.append(int(c))
        for i in range(n):
            w[i][i] += c
        v = w
    return coeff


def build(m):
    z = [F(1, 3 * 2 ** j) for j in range(m + 1)]
    a = F(1, 2) - F(1, 3 * 2 ** (m + 1))
    left = [(F(0), z[m])]
    left += [(z[m - i + 1], z[m - i]) for i in range(1, m + 1)]
    left += [(z[0], a)]
    right = [(1 - hi, 1 - lo) for lo, hi in left]
    ints = left + right
    k = m + 2
    for lo, hi in ints:
        assert lo < hi
        assert hi <= a or lo >= 1 - a
    A = [[0] * (2 * k) for _ in range(2 * k)]
    for i, (lo, hi) in enumerate(ints):
        image = (1 - 2 * hi, 1 - 2 * lo) if hi < F(1, 2) else (2 - 2 * hi, 2 - 2 * lo)
        assert image[0] < image[1]
        for j, (sl, sr) in enumerate(ints):
            overlap = min(image[1], sr) - max(image[0], sl)
            if overlap > 0:
                assert image[0] <= sl and sr <= image[1], (m, i, j, image, (sl, sr))
                A[i][j] = 1
    assert all(A[i][j] == A[i + k][j + k] and A[i][j + k] == A[i + k][j]
               for i in range(k) for j in range(k))
    B = [[A[i][j] + A[i][j + k] for j in range(k)] for i in range(k)]
    E = [[0] * k for _ in range(k)]
    E[0][0] = E[0][1] = 1
    for i in range(1, m):
        E[i][i + 1] = 1
    E[m][m + 1] = 2
    for j in range(1, m + 1):
        E[m + 1][j] = 1
    assert B == E, (m, B, E)
    return A, B


def main():
    for m in range(1, 13):
        A, B = build(m)
        if m <= 7:
            p = [1, 0] + [-2] * m
            assert charpoly(B) == polytimes([1, -1], p)
        if m <= 4:
            # The antisymmetric block contributes t^(m+1)(t+1).
            anti = [1, 1] + [0] * (m + 1)
            expected = polytimes(polytimes([1, -1], [1, 0] + [-2] * m), anti)
            assert charpoly(A) == expected, (m, charpoly(A), expected)
    lam_prev = 1.0
    for m in range(1, 25):
        def pval(t):
            return t ** (m + 1) - 2 * sum(t ** j for j in range(m))
        lo, hi = 1.0, 2.0
        for _ in range(75):
            mid = (lo + hi) / 2
            if pval(mid) < 0:
                lo = mid
            else:
                hi = mid
        lam = (lo + hi) / 2
        assert lam > lam_prev
        assert abs((2 - lam) * (lam + 1) * lam ** m - 2) < 1e-6
        if m == 1:
            assert abs(log(lam) / log(2) - .5) < 1e-13
        lam_prev = lam
    print('VERIFY_OK: exact partition images m=1..12; quotient polynomials m=1..7; full spectra m=1..4; numerical roots m=1..24')


if __name__ == '__main__':
    main()
