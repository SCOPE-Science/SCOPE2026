"""Independent finite checks for isolation/degree-parity covariance in G(n,p).

Uses only the Python standard library. Finite checks support, but do not replace,
the proof for all n and p.
"""
from fractions import Fraction
from itertools import combinations
from math import log, exp


def predicted(n, p):
    return -Fraction(n, 2) * (1 - p)**(n - 1) * (
        1 + (1 - 2*p)**(n - 2) * (2*n*p - 1))


def brute_moments(n):
    edges = list(combinations(range(n), 2))
    counts = len(edges)
    # Each list index k collects all labeled graphs having k edges.
    a, b, ab = [[0] * (counts + 1) for _ in range(3)]
    for mask in range(1 << counts):
        d = [0]*n
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                d[u] += 1
                d[v] += 1
        x = sum(t == 0 for t in d)
        y = sum(t % 2 for t in d)
        k = mask.bit_count()
        a[k] += x
        b[k] += y
        ab[k] += x*y
    return counts, a, b, ab


def check_exact():
    checked = 0
    for n in range(2, 7):
        E, a, b, ab = brute_moments(n)
        for p in (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2),
                  Fraction(4, 5), Fraction(9, 10)):
            w = [p**k * (1-p)**(E-k) for k in range(E+1)]
            x = sum(t*z for t,z in zip(a,w))
            y = sum(t*z for t,z in zip(b,w))
            xy = sum(t*z for t,z in zip(ab,w))
            assert xy-x*y == predicted(n,p), (n,p)
            checked += 1
    return checked


def crossover(n):
    assert n >= 3 and n % 2 == 1
    lo,hi=.5,1.
    def f(p):
        return (2*p-1)**(n-2) * (2*n*p-1) - 1
    for _ in range(90):
        mid = (lo + hi)/2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def check_window():
    count=0
    for n in (101, 501, 2001, 10001):
        threshold=crossover(n)
        relative=2*n*(1-threshold)-log(2*n)
        assert abs(relative) < 0.12, (n,relative)
        for s in (-2., -1., 1., 2.):
            p=1-(log(2*n)+s)/(2*n)
            t=(1-2*p)
            # The normalized covariance is used to avoid underflow.
            norm=-(1+t**(n-2)*(2*n*p-1))
            assert abs(norm-(exp(-s)-1)) < (20*log(n)**2/n)*exp(abs(s))
            count+=1
    return count


if __name__=='__main__':
    e=check_exact()
    w=check_window()
    print(f'PASS: {e} independently enumerated exact graph-law cases; '
          f'{w} numerical critical-window checks.')
