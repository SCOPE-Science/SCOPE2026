#!/usr/bin/env python3
"""Reproducible finite checks for the circular hard-geometric graph theorem."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb, factorial, log, exp
import random


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def cyclic_singletons(n, chosen):
    chosen = set(chosen)
    return sum((i in chosen and ((i-1) % n) in chosen) for i in range(n))


def conditional_pmf(n, h, j):
    if h == n:
        return Fraction(int(j == n))
    if h == 0:
        return Fraction(int(j == 0))
    # Uniform positive compositions of n into h ordered parts.
    return Fraction(binom(h, j) * binom(n-h-1, h-j-1), binom(n-1, h-1))


def falling(n, k):
    v = 1
    for a in range(k): v *= n-a
    return v


def check_exact_gap_counts():
    checks = 0
    for n in range(3, 12):
        for h in range(n+1):
            count = Counter(cyclic_singletons(n, cc) for cc in combinations(range(n), h))
            denom = binom(n, h)
            assert sum(conditional_pmf(n, h, j) for j in range(n+1)) == 1
            checks += 1
            for j in range(n+1):
                assert Fraction(count.get(j, 0), denom) == conditional_pmf(n, h, j), (n,h,j)
                checks += 1
            if 0<h<n:
                for k in range(min(4,h)+1):
                    lhs = sum(Fraction(falling(j,k)*count.get(j,0),denom) for j in range(n+1))
                    rhs = Fraction(falling(h,k)*falling(h-1,k), falling(n-1,k))
                    assert lhs == rhs, (n,h,k)
                    checks += 1
    return checks


def exact_joint_from_spacings(n, radius):
    """Enumerate gap-indicator patterns via Dirichlet rectangle inclusion-exclusion.

    Probability that specified h gaps exceed r and other n-h do not:
       sum_{k=0}^{n-h} (-1)^k C(n-h,k) (1-(h+k)r)_+^(n-1).
    """
    patterns = Counter()
    for h in range(n+1):
        cellprob = sum(Fraction((-1)**k*comb(n-h,k)) *
                       max(Fraction(0), 1-(h+k)*radius)**(n-1)
                       for k in range(n-h+1))
        for pattern in combinations(range(n),h):
            patterns[(h,cyclic_singletons(n,pattern))] += cellprob
    return patterns


def check_dirichlet_integrals():
    checks=0
    for n in range(3,9):
        for r in [Fraction(1,10),Fraction(1,4),Fraction(2,5)]:
            d=exact_joint_from_spacings(n,r)
            assert sum(d.values()) == 1
            assert min(d.values()) >= 0
            checks+=2
            a=max(Fraction(0),1-r)**(n-1)
            b=max(Fraction(0),1-2*r)**(n-1)
            z=max(Fraction(0),1-3*r)**(n-1)
            H=sum(h*p for (h,j),p in d.items())
            J=sum(j*p for (h,j),p in d.items())
            HJ=sum(h*j*p for (h,j),p in d.items())
            assert H == n*a
            assert J == n*b
            assert HJ == 2*n*b + n*(n-2)*z
            checks += 3
    return checks


def check_numerical_scaling():
    checks = 0
    for x in [-1.0,0.0,1.0]:
        c=exp(-x/2)
        previous_error = None
        for n in [10000, 100000, 1000000]:
            r=(log(n)+x)/(2*n)
            a=(1-r)**(n-1)
            b=(1-2*r)**(n-1)
            z=(1-3*r)**(n-1)
            meanH=n*a
            meanI=n*b
            cross=2*n*b+n*(n-2)*z-n*n*a*b
            assert abs(meanH/(c*n**0.5)-1)<0.01
            assert abs(meanI/c**2-1)<0.01
            # At finite n the logarithmic correction can be visible.
            error = abs(cross-2*c*c)
            assert error < 10*c**3*(log(n)**2)/(n**0.5)
            if previous_error is not None:
                assert error < previous_error
                checks += 1
            previous_error = error
            checks+=3
    return checks


if __name__ == '__main__':
    a=check_exact_gap_counts()
    b=check_dirichlet_integrals()
    c=check_numerical_scaling()
    print(f'PASS: {a+b+c} exact or controlled numerical assertions ({a} conditional finite enumeration; {b} Dirichlet integrals; {c} asymptotic checks).')
