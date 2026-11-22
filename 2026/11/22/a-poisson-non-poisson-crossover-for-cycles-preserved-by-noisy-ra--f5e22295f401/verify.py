#!/usr/bin/env python3
"""Finite exact verification of cycle thinning for two noisy random maps.
Run with Python 3. No dependencies outside the standard library.
"""
from itertools import product
from math import factorial
from collections import Counter
from fractions import Fraction


def falling(n, r):
    x=1
    for j in range(r):x*=n-j
    return x


def cycles_of_map(f):
    n=len(f)
    status=[0]*n
    out=[]
    for i in range(n):
        if status[i]:continue
        path=[]
        pos={}
        v=i
        while status[v]==0 and v not in pos:
            pos[v]=len(path)
            path.append(v)
            v=f[v]
        if v in pos:
            out.append(len(path)-pos[v])
        for x in path:status[x]=1
    return Counter(out)


def direct_expectation(n,k,s):
    return Fraction(falling(n,k),n**k*k)*s**k


def direct_pair(n,k,l,s):
    m=k+l
    return Fraction(falling(n,m),n**m*k*l)*s**m if m<=n else Fraction(0)


def check():
    assertions=0
    examples=0
    for n in range(2,7):
        s=Fraction(2,3)+Fraction(1,3*n)
        sums=[Fraction(0) for _ in range(n)]
        pairs=[[Fraction(0) for _ in range(n)] for _ in range(n)]
        cdf=Fraction(0)
        for f in product(range(n),repeat=n):
            cs=cycles_of_map(f)
            examples+=1
            for k in range(1,n+1):
                sums[k-1]+=cs[k]*s**k
                for l in range(1,n+1):
                    x=cs[k]*(cs[l]-(k==l))
                    pairs[k-1][l-1]+=x*s**(k+l)
            # Conditional zero common cycles: all cycles individually fail.
            z=Fraction(1)
            for k,m in cs.items(): z*=(1-s**k)**m
            cdf+=z
        samples=n**n
        for k in range(1,n+1):
            assert sums[k-1]/samples==direct_expectation(n,k,s),(n,k,'mean')
            assertions+=1
            for l in range(1,n+1):
                assert pairs[k-1][l-1]/samples==direct_pair(n,k,l,s),(n,k,l,'pair')
                assertions+=1
        # Exact alternating sum over ordered disjoint candidate cycles.
        z=Fraction(0)
        for r in range(0,n+1):
            # Recursive sum of (n)_K/n^K * s^K / product(k_i), divided by r!.
            subsum=Fraction(0)
            for ks in product(range(1,n+1),repeat=r):
                K=sum(ks)
                if K<=n:
                    v=Fraction(falling(n,K),n**K)*s**K
                    for k in ks:v/=k
                    subsum+=v
            z+=(-1)**r*subsum/factorial(r)
        assert cdf/samples==z,(n,'void')
        assertions+=1
        print(f'n={n}: checked {samples} maps, {n+n*n+1} exact equalities, s={s}')
    print(f'PASS: {assertions} exact identities; {examples} complete maps enumerated.')

if __name__=='__main__':check()
