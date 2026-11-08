#!/usr/bin/env python3
"""Reproduce finite checks for an exact crown-graph spin-stability count.
Requires Python >=3.9 standard library only.  No external data files.
The proof of the all-n formula is in RESULT.md, not inferred from tests.
"""
from itertools import product
from math import comb, factorial
from fractions import Fraction


def predicted(n, ah):
    """Number of configurations with no energy-lowering single-spin flip."""
    a = Fraction(ah)
    assert n >= 3 and a > 0
    if a > n-1:
        return 1
    if a == n-1:
        return 2**(n+1)+n-1
    s = 2
    for m in range(-n,n+1,2):
        if abs(a-m) <= 1:
            s += comb(n,(n+m)//2)
    if a.denominator == 1 and (int(a)-n)%2 != 0:
        k = int(a)
        if k <= n-3:
            s += 2*n*comb(n-1,(n-1+k)//2)
    return s


def full_hamiltonian(spins,n,a):
    """From scratch, sum each surviving bipartite edge once."""
    return (sum(spins[i]*spins[n+j] for i in range(n)
                for j in range(n) if i!=j)
            - a*sum(spins))


def exhaustive(n,a):
    e = [(i,n+j) for i in range(n) for j in range(n) if i!=j]
    count=0
    for spins in product((-1,1),repeat=2*n):
        # Independently use exact energy of the flipped state, not local-field reductions.
        h0 = sum(spins[i]*spins[j] for i,j in e) - a*sum(spins)
        stable = True
        for k in range(2*n):
            flipped = list(spins)
            flipped[k] *= -1
            h1 = sum(flipped[i]*flipped[j] for i,j in e) - a*sum(flipped)
            if h1 < h0:
                stable = False
                break
        if stable:
            count += 1
    return count


def orbit_count(n,a):
    # Completely separate finite weighted enumeration over all four pair-types.
    a=Fraction(a)
    total=0
    for p in range(n+1):
        for q in range(n-p+1):
            for r in range(n-p-q+1):
                t=n-p-q-r
                A=p-q+r-t
                B=p-q-r+t
                typ=((1,1,p),(1,-1,r),(-1,1,t),(-1,-1,q))
                if all(x*(a-B+y)>=0 and y*(a-A+x)>=0 for x,y,z in typ if z):
                    total+=factorial(n)//(factorial(p)*factorial(q)*factorial(r)*factorial(t))
    return total


def run_checks():
    checks=0
    for n in range(3,7):
        aa=set([Fraction(1,5),Fraction(3,5),Fraction(1),Fraction(n-1),
                Fraction(n), Fraction(n+1), Fraction(n-1,2)])
        for k in range(1,n+1):
            aa.update([Fraction(k),Fraction(2*k+1,2)])
        for a in sorted(aa):
            x=predicted(n,a)
            y=exhaustive(n,a)
            assert x==y,(n,a,x,y)
            checks+=1
    for n in range(3,19):
        aa=set([Fraction(1,5),Fraction(n-1),Fraction(n),Fraction(n+1)])
        for k in range(1,n+1,3):
            aa.update([Fraction(k),Fraction(2*k+1,2)])
        for a in sorted(aa):
            x=predicted(n,a)
            y=orbit_count(n,a)
            assert x==y,(n,a,x,y)
            checks+=1
    # Recompute the critical count by an independent direct combinatorial expression.
    for n in range(3,19):
        a=Fraction(n-1)
        assert predicted(n,a)==2*(2**n)-1+n
        checks+=1
    print('PASS',checks,'comparisons: full graph energies and four-pair orbit counts')

if __name__=='__main__':
    run_checks()
