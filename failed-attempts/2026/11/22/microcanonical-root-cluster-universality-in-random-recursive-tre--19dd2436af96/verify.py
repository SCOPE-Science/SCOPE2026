"""Finite exact checks for root-cluster moments under fixed-size edge deletion.

Run: python3 verify.py
Only Python standard library is needed.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial


def rising(x, r):
    v = 1
    for k in range(r):
        v *= x + k
    return v


def elementary(values):
    e = [Q(1)] + [Q(0)] * len(values)
    for i, a in enumerate(values, 1):
        for j in range(i, 0, -1):
            e[j] += a * e[j - 1]
    return e


def formula(n, h, r):
    N = n - 1
    e = elementary([Q(j, j+r) for j in range(1, n)])
    return Q(factorial(r)*comb(N+r, r), comb(N, h)) * e[h]


def enumerate_moments(n, max_r):
    """Enumerate each recursive parent sequence and each deletion set."""
    N = n - 1
    mass = [[0] * (max_r + 1) for _ in range(N + 1)]
    for choices in product(*(range(j) for j in range(1, n))):
        parent = [0] * (n + 1)
        for v, p0 in enumerate(choices, 2):
            parent[v] = p0 + 1
        for mask in range(1 << N):
            connected = [False] * (n + 1)
            connected[1] = True
            size = 1
            for v in range(2, n+1):
                if not (mask >> (v-2)) & 1 and connected[parent[v]]:
                    connected[v] = True
                    size += 1
            h = mask.bit_count()
            for r in range(1, max_r + 1):
                mass[h][r] += rising(size, r)
    return [[Q(mass[h][r], factorial(N)*comb(N,h)) for r in range(max_r+1)]
            for h in range(N+1)]


def run():
    tests = 0
    for n in range(2, 8):
        moments = enumerate_moments(n, 5)
        for h in range(n):
            for r in range(1, 6):
                assert moments[h][r] == formula(n, h, r), (n, h, r, moments[h][r], formula(n,h,r))
                tests += 1
        # endpoints, no deletions => n members; all deleted => one member
        for r in range(1, 6):
            assert moments[0][r] == rising(n, r)
            assert moments[n-1][r] == rising(1, r)
            tests += 2
    # A second, separate check of the exact polynomial coefficient transformation:
    # [z^h] product_j (p + r*p/j + (1-p)*z) / (C(N,h)*p^(N-h)*(1-p)^h)
    # equals the elementary symmetric formula (using rational p).
    for n in range(2, 23):
        N = n-1
        for r in (1, 2, 4):
            for p in (Q(1, 3), Q(3, 5)):
                coeff = [Q(factorial(r))]
                for j in range(1,n):
                    nxt = [Q(0)]*(len(coeff)+1)
                    for k,x in enumerate(coeff):
                        nxt[k] += x*(p+Q(r)*p/j)
                        nxt[k+1] += x*(1-p)
                    coeff=nxt
                for h in range(n):
                    direct = coeff[h]/(comb(N,h)*p**(N-h)*(1-p)**h)
                    assert direct == formula(n,h,r)
                    tests += 1
    # Strict log-concavity of the microcanonical mean as h varies is a diagnostic.
    for n in range(4,60):
        mu = [formula(n,h,1) for h in range(n)]
        for h in range(1,n-1):
            assert mu[h]**2 > mu[h-1]*mu[h+1]
            tests += 1
    print('PASS:',tests,'exact rational assertions, all finite.')

if __name__ == '__main__':
    run()
