#!/usr/bin/env python3
"""Exact checks of fixed-position-set Fourier spectra for uniform permutations."""
from itertools import permutations
from math import comb, factorial
from fractions import Fraction

checks = 0

def check(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def multiplier(n, k):
    return sum(comb(k, j) * (-2)**j * factorial(n-j) for j in range(k+1))

def derangements(n):
    return sum((-1)**j * (factorial(n)//factorial(j)) for j in range(n+1))

def walsh_transform(a):
    a = list(a)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2*step):
            for j in range(step):
                u, v = a[start+j], a[start+j+step]
                a[start+j], a[start+j+step] = u+v, u-v
        step *= 2
    return a

for n in range(1, 9):
    histogram = [0]*(1<<n)
    for perm in permutations(range(n)):
        mask = 0
        for i, v in enumerate(perm):
            if i == v:
                mask |= 1 << i
        histogram[mask] += 1
    check(sum(histogram) == factorial(n), ('total', n))
    for mask, count in enumerate(histogram):
        check(count == derangements(n-mask.bit_count()), ('histogram',n,mask))
    spectrum = walsh_transform(histogram)
    for mask, value in enumerate(spectrum):
        check(value == multiplier(n,mask.bit_count()), ('transform',n,mask))

for n in range(1, 151):
    row = [multiplier(n,k) for k in range(n+1)]
    check(row[0]==factorial(n), ('trivial frequency',n))
    check(Fraction(row[-1],factorial(n)) == sum((Fraction((-2)**j,factorial(j)) for j in range(n+1)),Fraction(0)),('last frequency',n))
    if n>=2:
        for k in range(n):
            check(row[k]-row[k+1] == 2*multiplier(n-1,k), ('Pascal recurrence',n,k))
    if n>=4:
        check(all(v>0 for v in row),('positivity',n))
        if n==4:
            check(min(row)==4,('order four minimum',n))
        else:
            check(all(row[k]>row[k+1] for k in range(n)),('strict decrease',n))
            check(min(row)==row[-1],('last is min',n))
        condition = Fraction(max(row),min(row))
        check(condition<=15,('uniform bound',n))
        check((condition==15)==(n==5),('sharp uniqueness',n))
    if n==1: check(row==[1,-1],('n=1',))
    if n==2: check(row==[2,0,2],('n=2',))
    if n==3: check(row==[6,2,2,-2],('n=3',))
print(f'PASS: {checks} independent exact-integer/rational assertions')
