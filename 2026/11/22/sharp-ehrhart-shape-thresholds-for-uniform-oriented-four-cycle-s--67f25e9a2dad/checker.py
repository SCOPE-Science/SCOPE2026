"""Exact, dependency-free checks for the equal-weight directed four-cycle Ehrhart spectrum.

Run: python3 checker.py
All comparisons use integer or rational arithmetic; the infinite proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb


def matrix(w):
    return [[int(i == j) + (w if j == (i + 1) % 4 else 0)
             for j in range(4)] for i in range(4)]


def determinant(A):
    n = len(A)
    s = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        prod = 1
        for i in range(n):
            prod *= A[i][p[i]]
        s += (-1 if inversions % 2 else 1) * prod
    return s


def inverse(A):
    n = len(A)
    T = [[Q(A[i][j]) for j in range(n)] + [Q(int(i == j)) for j in range(n)]
         for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j, n) if T[k][j])
        T[j], T[k] = T[k], T[j]
        factor = T[j][j]
        T[j] = [x / factor for x in T[j]]
        for i in range(n):
            if i != j:
                factor = T[i][j]
                T[i] = [T[i][l] - factor * T[j][l] for l in range(2 * n)]
    return [t[n:] for t in T]


def compositions4(N):
    for a in range(N + 1):
        for b in range(N - a + 1):
            for c in range(N - a - b + 1):
                yield (a, b, c, N - a - b - c)


def ehrhart_h(w):
    a = comb(w, 3) if w >= 3 else 0
    b = (2 * w**3 + w - 6) // 3
    return [1, a, b, a]


def predicted_L(m, h):
    return sum(h[i] * comb(m + 3 - i, 3) for i in range(min(m, 3) + 1))


def disc_cubic(A, B, C, D):
    return 18 * A * B * C * D - 4 * B**3 * D + B**2 * C**2 - 4 * A * C**3 - 27 * A**2 * D**2


def run():
    numcounts = 0
    for w in range(2, 10):
        M = matrix(w)
        assert determinant(M) == 1 - w**4
        J = inverse(M)
        h = ehrhart_h(w)
        assert sum(h) == (w**4 - 1) // (w + 1)
        for m in range(1, 4):
            good = 0
            interior1 = 0
            for x in compositions4(m * (w + 1)):
                y = [sum(J[i][j] * x[j] for j in range(4)) for i in range(4)]
                assert sum(y) == m
                if min(y) >= 0:
                    good += 1
                    if m == 1 and min(y) > 0:
                        interior1 += 1
            assert good == predicted_L(m, h), (w, m, good, predicted_L(m, h))
            if m == 1:
                assert interior1 == h[3]
            numcounts += 1
        a, b = h[1], h[2]
        if w == 2:
            assert a == 0 and b == 4
        elif 3 <= w <= 6:
            assert disc_cubic(a, b, a, 1) < 0
        else:
            assert a > 2 and a*a > 4*b - 8 and b - 2*a + 1 > 0
        assert (a*a >= b) == (w >= 5)
    print('PASS: 8 exact determinants and inverses; 24 complete dilation counts;')
    print('      interior lattice-point counts, Ehrhart h* formula and thresholds.')
    for w in range(2, 10):
        print('w=', w, 'h*=', ehrhart_h(w), 'real-rooted=',w>=7)

if __name__ == '__main__':
    run()
