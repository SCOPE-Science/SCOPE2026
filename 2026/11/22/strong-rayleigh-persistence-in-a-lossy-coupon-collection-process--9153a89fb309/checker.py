#!/usr/bin/env python3
"""Exact finite-size checks for the coupon-retention polynomial theorem.
Requires Python 3 and sympy (for exact real-root counting).
"""
from fractions import Fraction as Q
from math import comb
from itertools import product
from sympy import Poly, Symbol, Rational, oo

z=Symbol('z')
ASSERTIONS=0

def check(condition, why):
    global ASSERTIONS
    assert condition,why
    ASSERTIONS+=1

def recurrence(poly, n, p):
    # Polynomial represented by ascending coefficients.
    q=1-p
    # a(x)=poly(x); b(x)=x*(poly(x)+(1-x)*poly'(x)/n).
    derivative=[j*poly[j] for j in range(1,len(poly))]
    def add(a,b):
        return [ (a[i] if i<len(a) else Q(0)) + (b[i] if i<len(b) else Q(0)) for i in range(max(len(a),len(b)))]
    def mul(a,b):
        c=[Q(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return c
    b=mul([Q(0),Q(1)],add(poly, mul([Q(1),Q(-1)], [x/n for x in derivative]) if derivative else [Q(0)]))
    # compose b(p+qz) with Horner
    ans=[Q(0)]
    for c in b[::-1]: ans=add(mul(ans,[p,q]),[c])
    while len(ans)>1 and ans[-1]==0:ans.pop()
    return ans

def direct_step(dist,n,p):
    q=1-p
    result=[Q(0)]*(1<<n)
    for state,weight in enumerate(dist):
        if not weight:continue
        for picked in range(n):
            enlarged=state | (1<<picked)
            for out in range(1<<n):
                if out & ~enlarged:continue
                kept=out.bit_count(); lost=(enlarged^out).bit_count()
                result[out]+=weight*Q(1,n)*q**kept*p**lost
    return result

def poly_of_states(dist,n):
    arr=[Q(0)]*(n+1)
    for mask,pr in enumerate(dist):arr[mask.bit_count()]+=pr
    while len(arr)>1 and arr[-1]==0:arr.pop()
    return arr

def rational_root_count(coeff):
    if len(coeff)<=1:return 0
    p=Poly(sum(Rational(c.numerator,c.denominator)*z**j for j,c in enumerate(coeff)),z,domain='QQ')
    return p.count_roots(-oo,0)

def run():
    for n in range(1,7):
        for r in range(4):
            choices=(Q(1,2),Q(1,4),Q(3,4),Q(0),Q(1))
            steps= min(7,n+2)
            ps=[choices[(r+2*i)%len(choices)] for i in range(steps)]
            dist=[Q(1)]+[Q(0)]*((1<<n)-1)
            poly=[Q(1)]
            for i,p in enumerate(ps):
                poly=recurrence(poly,n,p)
                dist=direct_step(dist,n,p)
                check(poly==poly_of_states(dist,n),f'PGF n={n},t={i},p={p}')
                check(sum(dist)==1,f'mass n={n},t={i}')
                check(sum(poly)==1,f'PGF mass n={n},t={i}')
                check(rational_root_count(poly)==len(poly)-1,f'real roots n={n},t={i},p={p}')
                check(all(co>=0 for co in poly),f'nonnegative n={n},t={i}')
                for k in range(n+1):
                    size_mass=sum(dist[mask] for mask in range(1<<n) if mask.bit_count()==k)
                    for mask in range(1<<n):
                        if mask.bit_count()==k:
                            check(dist[mask]*comb(n,k)==size_mass,f'exchangeability n={n},t={i},k={k}')
    print(f'PASS: {ASSERTIONS} exact finite-state / polynomial / real-root assertions')
if __name__=='__main__':run()
