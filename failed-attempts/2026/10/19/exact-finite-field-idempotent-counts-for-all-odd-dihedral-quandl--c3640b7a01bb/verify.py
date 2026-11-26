#!/usr/bin/env python3
"""Exact finite-field tests for idempotents in odd dihedral quandle algebras.

Self-contained. Run: python3 verify.py
The theorem's arbitrary-modulus, arbitrary-field proof is symbolic;
these tests exhaust the listed finite algebras only.
"""
from itertools import product
from math import gcd


def divisors(n):
    return [r for r in range(1, n+1) if n % r == 0]


def phi(n):
    return sum(gcd(a,n)==1 for a in range(n))


def formula(n,q):
    assert n >= 3 and n%2==1 and gcd(n,q)==1
    count=2
    for r in divisors(n):
        if r==1: continue
        d=1
        while pow(2,d,r)!=1: d+=1
        powers=[pow(2,j,r) for j in range(d)]
        minus=(-1)%r in powers
        H=set(powers)|{(-x)%r for x in powers}
        h=len(H)
        m=phi(r)//h
        s=1; u=q%r
        while u not in H:
            s+=1; u=(u*q)%r
        assert m%s==0
        if minus:
            a=next(j for j,x in enumerate(powers) if x==u)
            epsilon=1
            N=2**(d//2)+1
        else:
            a=next(j for j,x in enumerate(powers) if x==u or (-x)%r==u)
            epsilon=1 if powers[a]==u else -1
            N=2**d-1
        g=gcd(N, q**s - epsilon*2**a)
        assert g>=1
        count *= (g+1)**(m//s)
    return count


def arithmetic(q):
    # Each test field is prime or F_4 = F_2[t]/(t^2+t+1).
    if q == 4:
        def mul(a,b):
            r=0
            for i in range(2):
                if (b>>i)&1: r ^= a<<i
            if r&8: r ^= 0b1110
            if r&4: r ^= 0b111
            return r
        return lambda a,b: a^b,mul
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q


def direct_count(n,q):
    add,mul=arithmetic(q)
    count=0
    for a in product(range(q), repeat=n):
        z=[0]*n
        support=[i for i,x in enumerate(a) if x]
        for i in support:
            z[i]=add(z[i],mul(a[i],a[i]))
        for loc,i in enumerate(support):
            for j in support[loc+1:]:
                v=mul(a[i],a[j])
                z[(2*j-i)%n]=add(z[(2*j-i)%n],v)
                z[(2*i-j)%n]=add(z[(2*i-j)%n],v)
        if tuple(z)==a: count+=1
    return count


def run():
    cases=[(3,2),(3,4),(3,5),(5,2),(5,3),(5,4),(5,7),
           (7,2),(7,3),(9,2),(9,5),(11,2),(13,2),(15,2)]
    for n,q in cases:
        expected=formula(n,q)
        actual=direct_count(n,q)
        print(f'n={n} q={q} predicted={expected} enumerated={actual} '+('PASS' if actual==expected else 'FAIL'),flush=True)
        assert expected==actual,(n,q,expected,actual)
    print('VERIFY_OK')

if __name__=='__main__':run()
