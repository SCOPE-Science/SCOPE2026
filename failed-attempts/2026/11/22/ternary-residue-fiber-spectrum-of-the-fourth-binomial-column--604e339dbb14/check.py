#!/usr/bin/env python3
"""Reproduce finite residue-fiber checks for the quartic binomial polynomial.
No external packages are needed. Finite tests are not an infinite proof.
"""
from math import comb
from collections import Counter

def roots_square_3(m,z):
    if m == 0:
        return 1
    modulus = 3**m
    z %= modulus
    if z == 0:
        return 3**(m//2)
    v=0
    while z%3==0:
        z//=3
        v+=1
    if v%2 or z%3!=1:
        return 0
    return 2*3**(v//2)

def predicted(k,y):
    if y%3:
        return 2
    m=k-1
    modulus=3**m
    c = pow(128,-1,modulus) if m>0 else 0
    return 2+3*roots_square_3(m, (y//3-c)%modulus)

def main():
    checks=0
    for k in range(1,9):
        q=3**k
        period=3*q
        observed=[0]*q
        for n in range(period):
            observed[comb(n,4)%q if n>=4 else 0]+=1
        expected=[predicted(k,y) for y in range(q)]
        assert observed==expected, ('incorrect histogram',k,[(y,a,b) for y,(a,b) in enumerate(zip(observed,expected)) if a!=b][:5])
        assert min(observed)==2
        # Exact minimal period is 3^(k+1); 3^k is not a period (at n=1).
        assert (comb(1+q,4)%q if 1+q>=4 else 0) != 0
        assert sum(observed)==period
        print('k=',k,'period=',period,'fiber_spectrum=',dict(sorted(Counter(observed).items())))
        checks+=period+q
    # Independently test the algebraic polynomial decomposition modulo 3^8.
    mod=3**8
    inv8=pow(8,-1,mod)
    inv128=pow(128,-1,mod)
    for t in range(2000):
        F=comb(3*t,4) if t>=2 else 0
        G=((9*t**4-18*t**3+11*t*t-2*t)*inv8)%mod
        u=2*t-1
        identity=(1+u*u*(9*u*u-10))*inv128%mod
        assert F%mod==(3*G)%mod
        assert G==identity
        checks+=2
    for k in range(1,7):
        modulus=3**k
        inverse128=pow(128,-1,modulus)
        inverse2=pow(2,-1,modulus)
        images=set()
        for u in range(modulus):
            A=((9*u*u-10)*inverse128)%modulus
            # Hensel lift the unique root of A congruent to 1 modulo 3.
            root=1
            for j in range(1,k):
                base=3**j
                root=next(root+d*base for d in range(3)
                          if ((root+d*base)**2-A)%(base*3)==0)
            assert root**2%modulus==A
            w=u*root%modulus
            images.add(w)
            t=((u+1)*inverse2)%modulus
            G=((9*t**4-18*t**3+11*t*t-2*t)*pow(8,-1,modulus))%modulus
            assert G==(inverse128+w*w)%modulus
            checks+=2
        assert len(images)==modulus, ('square conjugacy not bijective',k)
    print('PASS: checks=',checks)
if __name__=='__main__': main()
