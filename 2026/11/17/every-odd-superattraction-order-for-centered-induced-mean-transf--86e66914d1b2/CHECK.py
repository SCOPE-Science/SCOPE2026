#!/usr/bin/env python3
"""Finite diagnostics for moment-stratified mean iteration; not an infinite proof."""
from fractions import Fraction as F
from math import factorial
from decimal import Decimal, localcontext


def legendre(n):
    out = {}
    for j in range(n // 2 + 1):
        coeff = F((-1) ** j * factorial(2*n-2*j),
                  2**n * factorial(j) * factorial(n-j) * factorial(n-2*j))
        out[n-2*j] = coeff
    return out


def moment(n, power, eps):
    base = F(1, power+1) if power % 2 == 0 else F(0)
    pert = sum((c / (power+d+1) for d, c in legendre(n).items()
                if (power+d) % 2 == 0), F(0))
    return base + eps*pert


def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


checks = 0
for p in (3, 5, 7, 9):
    eps = F(3, 5)
    for j in range(1, p, 2):
        assert moment(p, j, eps) == 0
        checks += 1
    wanted = eps * F(2**p * factorial(p)**2, factorial(2*p+1))
    assert moment(p, p, eps) == wanted
    checks += 1
    for j in range(p, p+18, 2):
        assert moment(p, j, eps) > 0
        checks += 1
    with localcontext() as ctx:
        ctx.prec = 80
        c = dec(wanted) / (Decimal(2)**(p-1))
        for r_str in ('0.10', '0.20'):
            r = Decimal(r_str)
            z = (r/2).exp()
            u = (z - 1/z)/(z + 1/z)
            hp, hm = Decimal(0), Decimal(0)
            for j in range(80):
                term = dec(moment(p, j, eps)) * u**j
                hp += term
                hm += (-1)**j * term
            rp = hp.ln() - hm.ln()
            assert rp > 0
            assert abs(rp/(c*r**p) - 1) < Decimal('0.02')
            checks += 2
        for j in (0, 1, 2, 3, 4):
            t = F(j, 4)
            value = sum((a*t**d for d, a in legendre(p).items()), F(0))
            assert abs(value) <= 1
            checks += 1
print(f'PASS: {checks} deterministic moment, sign, and series assertions')
