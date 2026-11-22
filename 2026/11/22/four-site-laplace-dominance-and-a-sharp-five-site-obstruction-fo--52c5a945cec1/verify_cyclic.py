#!/usr/bin/env python3
"""Exact rational checks for a cyclic versus iid reset-destination comparison.

The manuscript supplies the all-parameter proof. This program checks a finite
set of rational cases and an exact Brownian-compatible five-site witness.
"""
from fractions import Fraction as F
from itertools import product


def cyclic_blocks(q, k):
    m = len(q)
    return sum((product_value(q[(i+j) % m] for j in range(k)) for i in range(m)), F(0)) / m


def product_value(a):
    p = F(1)
    for x in a:
        p *= x
    return p


def transforms(q, c):
    """Exact rational Laplace transforms by periodic block summation."""
    m = len(q)
    p = product_value(q)
    window = sum((c**(k-1) * cyclic_blocks(q, k) for k in range(1, m+1)), F(0))
    f_cycle = F(1) - (F(1)-c) * window / (F(1)-c**m * p)
    meanq = sum(q, F(0))/m
    f_iid = (F(1)-meanq)/(F(1)-c*meanq)
    return f_cycle, f_iid


def main():
    checks = 0
    q = [F(3,4),F(3,4),F(3,4),F(1,4),F(1,4)]
    c = F(1,4)
    a,b = transforms(q,c)
    assert a == F(2729396,5242745); checks+=1
    assert b == F(12,23); checks+=1
    assert a-b == -F(136832,120583135); checks+=1
    assert cyclic_blocks(q,2) > (sum(q)/len(q))**2; checks+=1
    # The identity B_(km+j)=P^k B_j, including whole cycles, is exact.
    for m in range(1,8):
        x = [F(i+1,2*m+2) for i in range(m)]
        p = product_value(x)
        for k in range(4):
            for j in range(m):
                assert cyclic_blocks(x,k*m+j) == p**k*cyclic_blocks(x,j)
                checks += 1
    for m in range(1,5):
        choices = [F(1,8), F(2,8), F(4,8), F(6,8)]
        for vec in product(choices, repeat=m):
            avg = sum(vec)/m
            for k in range(1, 3*m+1):
                assert cyclic_blocks(vec,k) <= avg**k
                checks += 1
            for c in (F(1,8),F(1,4),F(1,2),F(7,8)):
                ac,ai=transforms(vec,c)
                assert ac >= ai
                checks += 1
    print('PASS', checks, 'exact-rational assertions; witness:',a,b,a-b)

if __name__ == '__main__':
    main()
