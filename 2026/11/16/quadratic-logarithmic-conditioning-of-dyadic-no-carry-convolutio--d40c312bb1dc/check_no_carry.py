"""Exact combinatorial enumeration and numerical cross-checks for dyadic no-carry Fourier spectra.

Run: python3 check_no_carry.py.  This checker corroborates finite cases; the theorem's
all-length proof is analytic and does not rely on floating-point calculations.
"""
import cmath
import math
import itertools


def direct(n, u, v):
    N = 1 << n
    omega = cmath.exp(2j * math.pi / N)
    total = 0j
    for a in range(N):
        for b in range(N):
            if not (a & b):
                total += omega ** ((u * a + v * b) % N)
    return total


def factors(n, u, v):
    N = 1 << n
    ans = 1+0j
    for j in range(n):
        ans *= (1 + cmath.exp(2j * math.pi * ((u << j) % N) / N)
                   + cmath.exp(2j * math.pi * ((v << j) % N) / N))
    return ans


def witness(n):
    N = 1 << n
    u = (N - (-1)**n) // 3
    return u, N-u


def test():
    count = 0
    for n in range(1, 6):
        N = 1 << n
        lo = 2**(-n*(n+1)/2)
        hi = (4*math.pi/3)**n * lo
        absolute_min = 1e99
        for u in range(N):
            for v in range(N):
                F = factors(n,u,v)
                D = direct(n,u,v)
                assert abs(D-F) < 3e-10 * max(1,3**n), (n,u,v,D,F)
                assert abs(F) >= lo*(1-1e-8), (n,u,v,F,lo)
                absolute_min = min(absolute_min, abs(F))
                count += 1
        u,v = witness(n)
        assert abs(factors(n,u,v)) <= hi*(1+1e-8), (n,u,v)
        print('N',N,'minimum',format(absolute_min,'.14g'),'witness',witness(n),
              'witness absolute',format(abs(factors(n,u,v)),'.14g'))
    for n in range(6, 11):
        N = 1 << n
        lo = 2**(-n*(n+1)/2)
        hi = (4*math.pi/3)**n * lo
        u,v = witness(n)
        W=abs(factors(n,u,v))
        assert lo*(1-1e-7) <= W <= hi*(1+1e-7), (n,W,lo,hi)
    print('NO_CARRY_FOURIER_BOUNDS_PASS', 'direct_coefficients', count)


if __name__ == '__main__':
    test()
