#!/usr/bin/env python3
"""Independent integer-arithmetic check for adjacent binary cyclotomic gaps."""
from collections import Counter
from math import gcd

def predicted(q):
    assert q > 5 and gcd(q, 5) == 1
    h, r = divmod(q, 5)
    if r == 1:
        return {(1,4):2*h-1,(4,1):2*h-1,(2,3):2*h-1,(3,2):2*h-1,
                (2,4):1,(4,2):1,(3,3):1}
    if r == 2:
        return {(1,1):4*h+3,(1,2):2*h,(2,1):2*h,(1,4):2*h,(4,1):2*h}
    if r == 3:
        return {(1,1):4*h+1,(1,2):2*h+2,(2,1):2*h+2,(1,4):2*h,(4,1):2*h}
    return {(1,3):1,(3,1):1,(2,2):1,(1,4):2*h,(4,1):2*h,
            (2,3):2*h+1,(3,2):2*h+1}

def semigroup_coeffs(q):
    degree = 4 * (q - 1)
    # All representable integers below 5q have exactly one such expression.
    member = [0] * (degree + 1)
    for b in range(5):
        for a in range((degree - b*q)//5 + 1) if b*q <= degree else []:
            member[5*a + q*b] = 1
    return [member[n] - (member[n-1] if n else 0) for n in range(degree+1)]

def pair_counts(c):
    positions = [n for n,v in enumerate(c) if v]
    gaps = [b-a for a,b in zip(positions,positions[1:])]
    return Counter(zip(gaps,gaps[1:]))

def cyclic_block_counts(r):
    out = Counter()
    for j in range(4):
        active = {(k*r)%5 for k in range(j+1)}
        activeword = [int(i in active) for i in range(5)]
        places = [i for i in range(5) if activeword[i] != activeword[(i-1)%5]]
        gaps = [(places[(a+1)%len(places)]-places[a])%5 for a in range(len(places))]
        out.update((gaps[a],gaps[(a+1)%len(gaps)]) for a in range(len(gaps)))
    return out

def main():
    count=0
    for q in range(6,501):
        if gcd(q,5)!=1: continue
        obs=pair_counts(semigroup_coeffs(q))
        exp=Counter(predicted(q))
        assert obs==exp,(q,obs,exp)
        count+=1
    for r in range(1,5):
        q=5+r
        assert pair_counts(semigroup_coeffs(q+5))-pair_counts(semigroup_coeffs(q)) == cyclic_block_counts(r)
        assert pair_counts(semigroup_coeffs(q+10))-pair_counts(semigroup_coeffs(q+5)) == cyclic_block_counts(r)
    # Separate polynomial construction for prime q, using exact cyclotomic division.
    import sympy as sp
    x=sp.Symbol('x')
    checked=0
    for q in sp.primerange(7,101):
        f=sp.Poly(sp.cyclotomic_poly(5*q,x),x)
        coeff=[int(f.nth(i)) for i in range(f.degree()+1)]
        assert f.degree()==4*(q-1)
        assert pair_counts(coeff)==Counter(predicted(q))
        assert coeff==semigroup_coeffs(q)
        checked+=1
    print(f'PASS: {count} semigroup moduli; 4 base/insertion checks; {checked} independently constructed prime cyclotomic polynomials.')
if __name__=='__main__': main()
