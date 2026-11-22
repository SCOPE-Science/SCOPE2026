#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic checks for a finite Fejer quadratic form.

The proof of the all-degree statement is in RESULT.md. This script checks
finite cases only and does not replace the proof.
"""
import cmath
import math
import random
from fractions import Fraction


def gram(n):
    return [[Fraction(1) - Fraction(2 * abs(j-k), n)
             for k in range(n+1)] for j in range(n+1)]


def modes(n):
    basis = [([1.0 if j in (0, n) else 0.0 for j in range(n+1)], 0.0, 'null')]
    for ell in range(1, n//2+1):
        angle = (2*ell-1)*math.pi/n
        vec = [math.cos(angle*(j-n/2)) for j in range(n+1)]
        lam = 1/(n*math.sin(angle/2)**2)
        basis.append((vec, lam, 'symmetric'))
    for ell in range(1, (n+1)//2+1):
        angle = (2*ell-1)*math.pi/(n+1)
        vec = [math.sin(angle*(j-n/2)) for j in range(n+1)]
        lam = 1/(n*math.sin(angle/2)**2)
        basis.append((vec, lam, 'antisymmetric'))
    return basis


def gamma(n):
    d = n if n % 2 == 0 else n+1
    return 1/(n*math.cos(math.pi/(2*d))**2)


def close(a, b, multiplier=1):
    if abs(a-b) > 2e-9 * max(1.0, abs(a), abs(b))*multiplier:
        raise AssertionError((a, b))


def check():
    count = 0
    for n in range(1, 71):
        h = gram(n)
        for j in range(n+1):
            assert h[j][0]+h[j][n] == 0
            for k in range(n+1):
                assert h[j][k] == h[k][j]
                count += 1
        for j in range(1, n):
            for k in range(n+1):
                assert h[j-1][k]-2*h[j][k]+h[j+1][k] == (-Fraction(4,n) if j == k else 0)
                count += 1
        basis = modes(n)
        assert len(basis) == n+1
        for v,lam,kind in basis:
            for j in range(n+1):
                close(sum(float(h[j][k])*v[k] for k in range(n+1)), lam*v[j], 3)
                count += 1
        for a,(va,_,_) in enumerate(basis):
            for vb,_,_ in basis[:a]:
                close(sum(x*y for x,y in zip(va,vb)), 0, 3)
                count += 1
        smallest = min(lam for _,lam,_ in basis if lam > 0)
        close(smallest, gamma(n))
        soft = min((t for t in basis if t[1] > 0),key=lambda t:t[1])[0]
        null = basis[0][0]
        for factor in (0., 0.37, -1.2):
            v = [soft[j]+factor*null[j] for j in range(n+1)]
            norm_sq = sum(abs(z)**2 for z in v) - abs(v[0]+v[n])**2 / 2
            deficit = sum(v[j]*float(h[j][k])*v[k] for j in range(n+1) for k in range(n+1))
            close(deficit, gamma(n)*norm_sq, 3)
            count += 1
    rng = random.Random(22027)
    for n in range(1, 35):
        h = gram(n)
        for _ in range(15):
            b = [complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(n+1)]
            total = sum(b)
            partial = 0j
            squares = 0.0
            for m in range(n):
                partial += b[m]
                squares += abs(total-2*partial)**2/n
            form = sum((b[j].conjugate()*b[k]*float(h[j][k])).real
                       for j in range(n+1) for k in range(n+1))
            close(form, squares)
            dist_sq = sum(abs(z)**2 for z in b) - abs(b[0]+b[n])**2/2
            assert form >= (gamma(n)*dist_sq-1e-8)
            count += 2
    print(f'PASS: {count} finite exact/spectral/identity assertions; n=1..70 spectral modes; n=1..34 complex tests')


if __name__ == '__main__':
    check()
