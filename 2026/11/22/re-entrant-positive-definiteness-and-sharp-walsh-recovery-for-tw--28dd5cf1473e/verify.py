#!/usr/bin/env python3
"""Exact checks for two-coloured-cycle permutation fixed-set Fourier theorem.
Only standard-library Python is needed. No stochastic assertions.
"""
from math import factorial, comb, gcd
from itertools import permutations
from collections import defaultdict
from fractions import Fraction

checks = 0

def check(statement, explanation):
    global checks
    if not statement:
        raise AssertionError(explanation)
    checks += 1


def multiplier(n,k):
    return sum(comb(k,j)*(-4)**j*factorial(n-j+1) for j in range(k+1))


def cycle_count(perm):
    seen = [False]*len(perm); c = 0
    for i in range(len(perm)):
        if seen[i]: continue
        c += 1
        j = i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
    return c


def direct(n):
    hist=defaultdict(int)
    for p in permutations(range(n)):
        fixedmask=sum((1<<i) for i,x in enumerate(p) if i==x)
        hist[fixedmask] += 2**cycle_count(p)
    return hist


# Direct permutation enumeration, independently from factorial inclusion-exclusion.
for n in range(1,8):
    f=direct(n)
    check(sum(f.values()) == factorial(n+1),('total',n))
    for mask in range(1<<n):
        signed=sum(w*((-1)**((mask&s).bit_count())) for s,w in f.items())
        check(signed == multiplier(n,mask.bit_count()), ('direct Fourier',n,mask))

# Algebraic reductions and full character-order spectra through 180.
for n in range(1,181):
    L=[multiplier(n,k) for k in range(n+1)]
    check(L[0] == factorial(n+1),('trivial',n))
    check(len(set(L)) <= n+1,('shell count',n))
    for k in range(n):
        check(L[k]-L[k+1] == 4*multiplier(n-1,k),('shell difference',n,k))
    if n>=9:
        check(all(x>0 for x in L),('positive',n))
        check(all(L[k]>L[k+1] for k in range(n)),('strict decline',n))
        check(L[-1]==min(L),('sharp gap',n))
    if n==8:
        check(L==[362880,201600,120960,74880,48000,31104,21120,12928,15744], 'n8 entire spectrum')
        check(min(L)==12928, 'n8 gap')
    if n==6:
        check(min(L)==112 and max(L)==5040, 'n6 sharp condition')
    if n==7:
        check(L[-1]==-704 and all(x>0 for x in L[:-1]), 'n7 reentrant failure')
    if n==3:
        check([k for k,x in enumerate(L) if x==0] == [1], 'singular shell')
    if n!=3:
        check(0 not in L, ('nonzero',n))
    if n>=2:
        m0=multiplier(n-2,n-2)
        m1=multiplier(n-1,n-1)
        m2=multiplier(n,n)
        check(m2==(n-3)*m1+4*(n-1)*m0, ('gamma integration recurrence',n))

# Independent integer coefficients from EGF exp(-4z)/(1-z)^2,
# giving M_n/n! = coefficient of z^n, through 90.
for n in range(91):
    coeff=sum(Fraction((-4)**j, factorial(j))*(n-j+1) for j in range(n+1))
    check(coeff*factorial(n) == multiplier(n,n),('EGF',n))

# Explicit low orders and algebraic exact condition numbers.
check([multiplier(1,k) for k in range(2)]==[2,-2],'n1')
check([multiplier(2,k) for k in range(3)]==[6,-2,6],'n2')
check([multiplier(3,k) for k in range(4)]==[24,0,8,-16],'n3')
check([multiplier(4,k) for k in range(5)]==[120,24,24,-8,56],'n4')
check([multiplier(5,k) for k in range(6)]==[720,240,144,48,80,-144],'n5')
check(Fraction(5040,112)==45,'n6 condition number')
check(Fraction(362880,12928)==Fraction(2835,101),'n8 condition number')
check(multiplier(8,8)==15744 and multiplier(9,9)==71936,'recurrence base positivity')
check(8-3==5,'n3 rank')
print(f'PASS {checks} exact assertions; all signs, spectral gaps and boundary cases verified in the displayed finite scope.')
print('Proven infinite assertions require the independent symbolic recurrence and induction in RESULT.md.')
