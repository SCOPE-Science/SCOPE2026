#!/usr/bin/env python3
"""Independent high-precision facet checks for the divisor-parabola inball theorem.

Scientific scope: verification on finite test domains; the infinite theorem is
proved separately by monotonicity of the top-to-chord radius functional.
"""
from decimal import Decimal, localcontext
from math import isqrt


def divisors(n):
    small = [i for i in range(1, isqrt(n) + 1) if n % i == 0]
    return small + [n // i for i in reversed(small) if i * i != n]


def predicted(n):
    ds = divisors(n)
    d = ds[-2]
    with localcontext() as ctx:
        ctx.prec = 65
        h = Decimal(n)
        m = Decimal(n + d)
        s = (1 + m * m).sqrt()
        r = h * m / (1 + s)
        c = h*h - r
        return +r, +c


def verify(n):
    ds = divisors(n)
    r,c = predicted(n)
    with localcontext() as ctx:
        ctx.prec = 65
        h = Decimal(n)
        eps = Decimal('1e-45')
        assert abs((h*h-c) - r) < eps
        tangencies = []
        for a,b in [(1,1)] + list(zip(ds[:-1],ds[1:])):
            a,b = Decimal(a),Decimal(b)
            slope = a+b
            radius_to_edge = (c + a*b)/(1+slope*slope).sqrt()
            if abs(radius_to_edge-r)<eps:
                tangencies.append((int(a),int(b)))
            else:
                assert radius_to_edge > r, (n,a,b, radius_to_edge-r)
        assert tangencies == [(ds[-2],ds[-1])], (n,tangencies)
        m = Decimal(ds[-2] + n)
        x_contact = r*m/(1+m*m).sqrt()
        assert Decimal(ds[-2]) < x_contact < h
        # Lower non-active facets remain strictly outside the constructed disk.
        return len(ds), x_contact


if __name__ == '__main__':
    ncases, facet_checks = 0,0
    for n in range(2,2001):
        ds=divisors(n)
        verify(n)
        ncases+=1
        facet_checks+=len(ds)
    # Check the least-prime fingerprint numerically for a short prime-power family.
    for p in (2,3,5,7,11):
        n=p**4
        r,c=predicted(n)
        defect=Decimal(n)-r
        target=Decimal(p)/Decimal(p+1)
        assert abs(defect-target) < Decimal(2)/Decimal(n)
    print('PASS:',ncases,'exact-formula high-precision cases,', facet_checks,'facet-distance comparisons; contact feet interior')
    print('Examples:', [(n,str(predicted(n)[0])[:21]) for n in (2,3,4,6,12,30)])
