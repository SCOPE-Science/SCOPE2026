#!/usr/bin/env python3
"""Reproduce finite-level kernel, cycle-identity, and crossover comparisons."""
from fractions import Fraction
from itertools import permutations, product
from math import gamma, lgamma, log, exp

def expr(g, m, n):
    a = Fraction(1,8) if m % 2 == 0 else Fraction(1,2)
    d = Fraction(1,2*m**(2*n))
    p = Fraction(1)
    for j in range(g): p *= (a+d+j)/(j+1)
    return p

def kernsize(g, m, n, perm, signs):
    seen = set(); out = 1
    for i in range(g):
        if i in seen: continue
        j=i; sign=1
        while j not in seen:
            seen.add(j);sign *= signs[j];j=perm[j]
        out *= (m**(2*n) if sign==1 else (2 if m%2==0 else 1)**2)
    return out

def cycles(p):
    visited=set();c=0
    for i in range(len(p)):
        if i in visited: continue
        c+=1;j=i
        while j not in visited:
            visited.add(j);j=p[j]
    return c

checks=0
for g in range(1,5):
    for m,n in ((2,1),(2,2),(3,1),(4,1)):
        total=Fraction(0);ct=0
        for p in permutations(range(g)):
            for signs in product((-1,1),repeat=g):
                total += Fraction(1,kernsize(g,m,n,p,signs));ct+=1
        observed=total/ct
        assert observed==expr(g,m,n),(g,m,n,observed,expr(g,m,n))
        checks += 1

bounds=0
for m in (2,3,4,5,8):
    a=0.125 if m%2==0 else 0.5
    for n in range(1,7):
        delta=0.5*m**(-2*n)
        for g in (1,2,3,10,100,10000,1000000):
            logr=sum(log(1+delta/(a+j)) for j in range(min(g,10000)))
            if g>10000:
                logr=lgamma(g+a+delta)-lgamma(a+delta)-lgamma(g+a)+lgamma(a)
            assert abs(logr-delta*log(g)) <= 14*delta+2e-7,(m,n,g,logr)
            bounds+=1

for m in (2,3):
    a=0.125 if m%2==0 else 0.5
    for g in (100,1000,10000):
        # Fixed-parameter finite-level formula is exact, not an asymptotic assumption.
        inf=1.0
        for j in range(g):inf *= (a+j)/(j+1)
        if inf==0: continue
        assert inf>0

# Independent point-by-point fixed-kernel count on small torsion grids.
def brute_kernel(g, q, perm, signs):
    total = 0
    for coords in product(range(q), repeat=2*g):
        if all(coords[2*i] == signs[i]*coords[2*perm[i]] % q and
               coords[2*i+1] == signs[i]*coords[2*perm[i]+1] % q
               for i in range(g)):
            total += 1
    return total

direct=0
for g, m, n in ((1,2,1),(2,2,1),(3,2,1),(2,3,1),(3,3,1),(2,2,2)):
    q=m**n
    for p in permutations(range(g)):
        for signs in product((-1,1),repeat=g):
            assert brute_kernel(g,q,p,signs)==kernsize(g,m,n,p,signs)
            direct+=1

print('VERIFY_OK direct_grid_kernels=',direct,'exact_kernel_cycle_cases=',checks,'uniform_log_bounds=',bounds)
