#!/usr/bin/env python3
"""Exact finite-field enumeration for weighted-permutation evolution algebras."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial, gcd

class Field:
    def __init__(self,q):
        self.q=q
        if q in (4,8):
            self.p=2;self.bits={4:2,8:3}[q];self.poly={4:0b111,8:0b1011}[q]
        else:
            self.p=q;self.bits=1;self.poly=None
    def add(self,a,b):
        return a^b if self.bits>1 else (a+b)%self.p
    def mul(self,a,b):
        if self.bits==1:return (a*b)%self.p
        z=0;x=a;y=b
        while y:
            if y&1:z^=x
            y>>=1;x<<=1
            if x&(1<<self.bits):x^=self.poly
        return z
    def sq(self,a): return self.mul(a,a)

def cycle_lengths(perm):
    seen=set();out=[]
    for i in range(len(perm)):
        if i in seen:continue
        j=i;length=0
        while j not in seen:
            seen.add(j);length+=1;j=perm[j]
        out.append(length)
    return out

def theoretical_weight_count(q,perm):
    # Conditional law of I, with exact rational coefficients.
    law={1:Fraction(1)}
    for L in cycle_lengths(perm):
        d=gcd(pow(2,L)-1,q-1)
        local={1:Fraction(d-1,d),1+d:Fraction(1,d)}
        nxt={}
        for a,pa in law.items():
            for b,pb in local.items():nxt[a*b]=nxt.get(a*b,Fraction(0))+pa*pb
        law={k:v for k,v in nxt.items() if v}
    return law

def check(q,n):
    F=Field(q); expected=Counter();observed=Counter();perms=list(permutations(range(n)))
    for perm in perms:
        law=theoretical_weight_count(q,perm)
        for k,v in law.items():expected[k]+=v*pow(q-1,n)
        for weights in product(range(1,q),repeat=n):
            idem=0
            for x in product(range(q),repeat=n):
                y=[0]*n
                for i in range(n):y[perm[i]]=F.mul(weights[i],F.sq(x[i]))
                if y==list(x):idem+=1
            observed[idem]+=1
    assert all(v.denominator==1 for v in expected.values()),(q,n,expected)
    assert observed==expected,(q,n,observed,expected)
    N=factorial(n)*pow(q-1,n)
    assert sum(observed.values())==N
    assert sum(i*c for i,c in observed.items())==N*(n+1)
    if q==4:
        assert all(i&(i-1)==0 for i in observed)  # all counts powers of two
        p_zero=Fraction(observed.get(1,0),N)
        if n%2:
            assert p_zero==0
        else:
            m=n//2
            poch=Fraction(1)
            for r in range(m):poch*=Fraction(1,3)+r
            assert p_zero==poch/factorial(m)
        second_moment=Fraction(sum(i*i*c for i,c in observed.items()),N)
        generating_coefficient=sum((-1)**j*comb(n-j+4,4) for j in range(n+1))
        assert second_moment==generating_coefficient
    return N,dict(sorted(observed.items()))

if __name__=='__main__':
    cases=[(2,n) for n in range(1,5)]+[(3,n) for n in range(1,5)]+[(4,n) for n in range(1,5)]+[(5,n) for n in range(1,4)]+[(7,n) for n in range(1,4)]+[(8,n) for n in range(1,4)]
    cnt=0;total=0
    for q,n in cases:
        N,counts=check(q,n)
        total+=N;cnt+=1
        print(f'PASS q={q} n={n} matrices={N} distribution={counts}')
    print(f'VERIFY_OK cases={cnt} matrices={total}')
