#!/usr/bin/env python3
"""Exact F2 computations for primitive-polynomial three-coordinate images.

Uses independent polynomial divisibility and recurrence-kernel linear algebra.
Python standard library only. This is finite diagnostic evidence, not an
exhaustive proof of the theorem quantified over all degrees and spans.
"""
from itertools import combinations
from math import floor, log2

def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        a<<=1;b>>=1
    return out

def power(a,n):
    b=1
    while n:
        if n&1:b=mul(a,b)
        a=mul(a,a);n>>=1
    return b

def mod(a,b):
    while a and a.bit_length()>=b.bit_length():
        a^=b<<(a.bit_length()-b.bit_length())
    return a

def valuation2(x):
    assert x>0
    return (x&-x).bit_length()-1

def root_powers(p):
    d=p.bit_length()-1
    q=(1<<d)-1
    xs=[1]
    for _ in range(q-1):xs.append(mod(xs[-1]<<1,p))
    assert len(set(xs))==q and mod(xs[-1]<<1,p)==1
    return xs

def first_trinomial_span(p):
    q=(1<<(p.bit_length()-1))-1
    for v in range(2,q):
        for u in range(1,v):
            if mod(1^(1<<u)^(1<<v),p)==0:return v,u
    raise AssertionError('primitive polynomial has no line')

def expected(p,abc,n,powers=None):
    assert n>=1
    a,b,c=abc
    if powers is None:powers=root_powers(p)
    q=len(powers)
    residues=[a%q,b%q,c%q]
    cuts=[1<<valuation2(b-a),1<<valuation2(c-b),1<<valuation2(c-a)]
    if len(set(residues))==1:
        return int(n<=min(cuts))+int(n<=max(cuts))
    if len(set(residues))==2:
        pair=next((u,v) for u,v in combinations(abc,2) if u%q==v%q)
        return int(n <= (1<<valuation2(pair[1]-pair[0])))
    collinear=(powers[residues[0]]^powers[residues[1]]^powers[residues[2]])==0
    return int(collinear and n<=min(cuts))

def by_divisibility(p,abc,n):
    modulus=power(p,n)
    hits=0
    for mask in range(1,8):
        poly=0
        for j,x in enumerate(abc):
            if mask>>j&1:poly^=1<<x
        if mod(poly,modulus)==0:hits+=1
    assert hits in (0,1,3)
    return (hits+1).bit_length()-1

def by_kernel(p,abc,n):
    poly=power(p,n)
    d=poly.bit_length()-1
    a,b,c=abc
    upto=c
    rows=[1<<i for i in range(min(d,upto+1))]
    if d<=upto:
        js=[j for j in range(d) if poly>>j&1]
        for i in range(d,upto+1):
            v=0
            for j in js:v^=rows[i-d+j]
            rows.append(v)
    basis={}
    for i in (a,b,c):
        x=rows[i]
        while x:
            lead=x.bit_length()-1
            if lead not in basis:
                basis[lead]=x;break
            x^=basis[lead]
    return 3-len(basis)

def main():
    tests=0
    for p,cmax,nmax in [(0b1011,32,26),(0b101111,28,18)]:
        roots=root_powers(p)
        d=p.bit_length()-1
        q=(1<<d)-1
        m,u=first_trinomial_span(p)
        print('P bits:',bin(p),'degree:',d,'multiplicative order:',q,
              'minimum 3-term span:',m,'witness:',(0,u,m))
        for a,b,c in combinations(range(cmax+1),3):
            abc=(a,b,c)
            for n in range(1,nmax+1):
                want=expected(p,abc,n,roots)
                got1=by_divisibility(p,abc,n)
                got2=by_kernel(p,abc,n)
                assert want==got1==got2,(p,abc,n,want,got1,got2)
                tests+=1
        for L in range(2,33):
            max_t=1
            for abc in combinations(range(L+1),3):
                t=next((n for n in range(1,18) if expected(p,abc,n,roots)==0),18)
                max_t=max(max_t,t)
            want=1 if L<m else 1+(1<<floor(log2(L/m)))
            assert max_t==want,(p,L,max_t,want)
        print('All span cutoff L=2..32 PASS')
    print('Independent 3-way comparisons PASS:',tests)

if __name__=='__main__':main()
