#!/usr/bin/env python3
"""Exact separate checks for the permutation peak-position Walsh theorem."""
from fractions import Fraction
from itertools import permutations
from math import factorial,gcd
from functools import reduce


def peak_mask(perm):
    m=0
    for i in range(1,len(perm)-1):
        if perm[i-1]<perm[i]>perm[i+1]:
            m |= 1<<(i-1)
    return m


def fwht(a):
    a=list(a)
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(h):
                x,y=a[i+j],a[i+j+h]
                a[i+j],a[i+j+h]=x+y,x-y
        h<<=1
    return a


def direct(n):
    f=[0]*(1<<max(n-2,0))
    for p in permutations(range(n)):
        f[peak_mask(p)]+=1
    return f


def exact_descent(n):
    """MacMahon exact descent-set enumerator from multinomial upper sets."""
    m=n-1
    a=[]
    for d in range(1<<m):
        cuts=[0]+[i+1 for i in range(m) if d>>i&1]+[n]
        den=1
        for j in range(len(cuts)-1): den*=factorial(cuts[j+1]-cuts[j])
        a.append(factorial(n)//den)
    for j in range(m):
        for mask in range(1<<m):
            if mask>>j&1: a[mask]-=a[mask^(1<<j)]
    f=[0]*(1<<max(n-2,0))
    for d,v in enumerate(a):
        s=0
        for j in range(1,m):
            if d>>j&1 and not (d>>(j-1)&1): s|=1<<(j-1)
        f[s]+=v
    assert sum(f)==factorial(n)
    return f


def tangent_coefficients(rmax):
    # c[r] is [z^(2r+1)] tan z. The only divisions are by odd integers.
    c=[Fraction(1)]
    for r in range(1,rmax):
        c.append(sum((c[i]*c[r-1-i] for i in range(r)),Fraction(0))/(2*r+1))
    for q in c: assert q.denominator%2==1
    return c


def joint_probability(b,c):
    # b is a set of interior peak indices encoded by bits 0..n-3
    if b & (b<<1): return Fraction(0)
    arr=[i for i in range(b.bit_length()) if b>>i&1]
    if not arr: return Fraction(1)
    lengths=[]
    run=1
    for i,j in zip(arr,arr[1:]):
        if j-i==2: run+=1
        else:
            lengths.append(run);run=1
    lengths.append(run)
    p=Fraction(1)
    for v in lengths:p*=c[v]
    return p


def moments(n):
    m=max(n-2,0)
    cs=tangent_coefficients(m+1)
    a=[(-2)**b.bit_count()*joint_probability(b,cs) for b in range(1<<m)]
    # subset zeta: W[S]/n! = sum_{B subset S}(-2)^|B| P(B subset peaks)
    for j in range(m):
        for s in range(1<<m):
            if s>>j&1:a[s]+=a[s^(1<<j)]
    return a


def main():
    checks=0
    for n in range(1,14):
        f=exact_descent(n)
        expected=fwht(f)
        q=moments(n)
        assert len(expected)==len(q)
        for i,v in enumerate(expected):
            assert q[i]*factorial(n)==v,(n,i,q[i],v)
            assert q[i].numerator%2==1 and q[i].denominator%2==1,(n,i,q[i])
            assert v!=0 and (abs(v)&-abs(v))==(factorial(n)&-factorial(n))
            checks+=3
        assert reduce(gcd, (abs(x) for x in expected))==(factorial(n)&-factorial(n))
        assert f[0]==(1<<(n-1))
        checks+=2
        if n<=8:
            assert f==direct(n)
            checks+=len(f)
        print(f'n={n:2}: dimension={len(f):5}; |spectrum| gcd={reduce(gcd,(abs(x) for x in expected))}; no zeros; exact moments OK')
    print(f'PASS {checks} exact checks')

if __name__=='__main__':main()
