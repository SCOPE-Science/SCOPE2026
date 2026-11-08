"""Finite exact and direct-numerical checks for the stated trispectrum sampling theorem.

Standard Python 3; use: python3 CHECK.py
"""
import cmath
import itertools
import math
from fractions import Fraction

checks = 0


def check(cond, message):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(message)


def determinant(mat):
    """Exact determinant by fraction-free integer elimination."""
    a = [list(map(int, row)) for row in mat]
    n = len(a)
    if not n:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = a[i][j] * pivot - a[i][k] * a[k][j]
                check(v % prev == 0, 'Bareiss non-exact division')
                a[i][j] = v // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def row(n, a):
    m = n // 4
    mid = n // 2
    out = [0] * m
    for b in (a, 1, 1, -a - 2):
        b %= n
        check(b % 2 == 1, 'Even frequency in selected trispectrum')
        if b < mid:
            out[(b - 1) // 2] += 1
        elif b > mid:
            out[(n - b - 1) // 2] -= 1
        else:
            check(mid % 2 == 1, 'Unexpected self-conjugate frequency')
    return out


for n in range(4, 202, 2):
    m = n // 4
    A = [row(n, 2 * j + 1) for j in range(m)]
    d = abs(determinant(A))
    check(d == (n if n % 4 == 0 else n // 2), ('relation determinant', n, d))

# Independently enumerate discretized Fourier phase fibers. Each coordinate
# is an N-th root of unity; the Nyquist coefficient, when present, is real.
for n in range(4, 14, 2):
    m = n // 4
    mid = n // 2
    sols = 0
    shifts = set()
    for s in range(n):
        pos = tuple((s * (2 * j + 1)) % n for j in range(m))
        nyq = (-1) ** s if mid % 2 else 1
        shifts.add((pos, nyq))
    for pos in itertools.product(range(n), repeat=m):
        for nyq in ((-1, 1) if mid % 2 else (1,)):
            h = {2 * j + 1: cmath.exp(2j * math.pi * pos[j] / n)
                 for j in range(m)}
            if mid % 2:
                h[mid] = complex(nyq)
            for b in range(1, n, 2):
                if b not in h:
                    h[b] = h[n-b].conjugate()
            if all(abs(h[a] * h[1] ** 2 * h[(-a - 2) % n] - 1) < 1e-8
                   for a in range(1, 2 * m, 2)):
                sols += 1
                check((pos, nyq) in shifts, ('nontranslation solution', n, pos, nyq))
    check(sols == n, ('translation fiber size', n, sols))

# Direct time-domain check of fourth autocorrelation and its Fourier
# transform, using independent DFT/inverse-DFT constructions.
for n in (4, 6, 8, 10, 12):
    F = [0j] * n
    for a in range(1, n, 2):
        F[a] = complex(1 + ((3*a) % 7) / 5, 0)
    for a in range(1, n, 2):
        if a < n-a:
            val = cmath.rect(abs(F[a]), (a*a + 2*a) / 7)
            F[a] = val
            F[n-a] = val.conjugate()
    f = [sum(F[a] * cmath.exp(2j*math.pi*a*x/n)
             for a in range(n)) / n for x in range(n)]
    for x in range(n):
        check(abs(f[x].imag)<1e-9, ('real time signal', n, x))
        check(abs(f[x+n//2] + f[x])<1e-9 if x<n//2 else True,
              ('antiperiodic',n,x))
    for a in range(1, 2*(n//4), 2):
        s = 0j
        for t1 in range(n):
            for t2 in range(n):
                for t3 in range(n):
                    rho = sum(f[x]*f[(x+t1)%n]*f[(x+t2)%n]*f[(x+t3)%n]
                              for x in range(n))
                    s += rho * cmath.exp(-2j*math.pi*(a*t1+t2+t3)/n)
        theory = F[a]*F[1]**2*F[(-a-2)%n]
        check(abs(s-theory)<2e-7*n, ('direct trispectrum', n, a, s, theory))

print('CHECK_OK exact_and_direct_assertions=' + str(checks))
