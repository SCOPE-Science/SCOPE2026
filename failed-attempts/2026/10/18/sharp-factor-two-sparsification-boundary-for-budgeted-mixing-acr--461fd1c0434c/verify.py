"""Exact-rational replay of the two-hub bridge spectral identities.
Run with Python 3.9+ (standard library only): python verify.py.
The finite checks support, but do not replace, the universal argument.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def add(x, y):
    z = [F(0)] * max(len(x), len(y))
    for i, v in enumerate(x): z[i] += v
    for i, v in enumerate(y): z[i] += v
    return z


def mul(x, y):
    z = [F(0)] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y): z[i + j] += a * b
    return z


def characteristic(A):
    d = len(A)
    out = [F(0)] * (d + 1)
    for perm in permutations(range(d)):
        parity = sum(perm[i] > perm[j] for i in range(d) for j in range(i + 1, d))
        prod = [F(1)]
        for i in range(d):
            j = perm[i]
            prod = mul(prod, [(-A[i][j]), F(1)] if i == j else [-A[i][j]])
        out = add(out, [(-v if parity % 2 else v) for v in prod])
    return out


def spectrum_check(p, q):
    N = p + q
    a, b, c = F(3*q, N), F(3*p, N), F(3*p*q, N) - 1
    assert a > 0 and b > 0 and c > 0
    quotient = [
        [a, -a, F(0), F(0)],
        [-(p-1)*a, (p-1)*a+c, -c, F(0)],
        [F(0), -c, (q-1)*b+c, -(q-1)*b],
        [F(0), F(0), -b, b],
    ]
    actual = characteristic(quotient)
    claimed = [F(1)]
    for root in [F(0), F(1), F(3*p*q, N), F(9*p*q, N)-3]:
        claimed = mul(claimed, [-root, F(1)])
    assert actual == claimed, (p, q, actual, claimed)
    assert F(3*p*q, N) > 1
    assert F(9*p*q, N)-3 > 1
    variance = F(9*p*q, N)-4
    assert variance > 0
    assert (p-1)*a+(q-1)*b+c == variance
    # The explicit universal test vector must have this variance.
    z = [F(2)]*(p-1) + [F(1), F(0)] + [F(-1)]*(q-1)
    avg = sum(z)/N
    assert sum((v-avg)**2 for v in z) == variance
    # Exact eigenvector equation in the full weighted graph.
    edges = [(i,p-1,a) for i in range(p-1)]
    edges += [(p+j,p,b) for j in range(1,q)]
    edges += [(p-1,p,c)]
    Lz = [F(0) for _ in range(N)]
    for i,j,w in edges:
        Lz[i] += w*(z[i]-z[j]); Lz[j] += w*(z[j]-z[i])
    assert Lz == [v-avg for v in z]
    assert all(w > 0 for _,_,w in edges)
    # Fourier/orbit transverse modes create the sharp ratio test.
    is_sharp = 2*p >= q and 2*q >= p
    candidate_is_gap = (p == 2 or a >= 1) and (q == 2 or b >= 1)
    assert candidate_is_gap == is_sharp
    return 1


def main():
    total = sum(spectrum_check(p,q) for p in range(2,25) for q in range(2,25))
    assert total == 529
    print(f'EXACT_CHECKS_OK p,q=2..24 ({total} parameter pairs): quotient characteristic polynomial,')
    print('budget, variances, eigenvector equations, and factor-two threshold')

if __name__ == '__main__':
    main()
