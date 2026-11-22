#!/usr/bin/env python3
"""Independent bit-matrix and polynomial validation of binary neighbor-XOR on C_n square K_2.
Python 3 standard library only. Recomputes powers, ranks, and fixed point counts.
"""
from math import gcd

def degree(x): return x.bit_length()-1

def mod(a,b):
    assert b
    while a and degree(a)>=degree(b): a^= b <<(degree(a)-degree(b))
    return a

def pgcd(a,b):
    while b: a,b=b,mod(a,b)
    return a

def pmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
    return c

def ppow(a,t):
    c=1
    while t:
        if t&1:c=pmul(c,a)
        a=pmul(a,a);t>>=1
    return c

def graph_map(n):
    # Bit positions: first n vertices of rail zero, next n of rail one.
    # Return columns of adjacency operator.
    cols=[]
    for rail in (0,1):
        for j in range(n):
            x=0
            for a,b in ((rail,(j-1)%n),(rail,(j+1)%n),(1-rail,j)):
                x^=1<<(a*n+b)
            cols.append(x)
    return cols

def compose(A,B):
    out=[]
    for col in B:
        y=0
        while col:
            lsb=col&-col
            y^=A[lsb.bit_length()-1]
            col^=lsb
        out.append(y)
    return out

def rank(A):
    piv={}
    for w in A:
        while w:
            k=w.bit_length()-1
            if k in piv: w^=piv[k]
            else: piv[k]=w;break
    return len(piv)

def stable_rank(n,t):
    if n%3: return 2*n
    v=n&-n
    if v==1: return 2*n-4 + (4 if t==0 else 2 if t==1 else 0)
    return 2*n-4*min(t,v)

def fixed_dim_formula(n,t):
    q=0b111; z=0b10
    P=ppow(q,t)^ppow(z,t)
    f=(1<<n)|1
    return degree(pgcd(f, pmul(P,P) if t%2 else P))*(1 if t%2 else 2)

def check():
    tests=0
    for n in range(3,45):
        A=graph_map(n); power=[1<<i for i in range(2*n)]
        for t in range(0,35):
            r=rank(power)
            expect=stable_rank(n,t)
            assert r==expect,(n,t,r,expect)
            if t:
                diff=[power[i]^(1<<i) for i in range(2*n)]
                fixed_dim=2*n-rank(diff)
                predicted=fixed_dim_formula(n,t)
                assert fixed_dim==predicted,(n,t,fixed_dim,predicted)
            power=compose(A,power)
            tests+=1
    print('matrix_rank_fixedpoint_gcd_tests_passed',tests)
    print('n periodic_dimension maximal_transient_fraction last_time_histogram')
    for n in [3,4,5,6,7,9,12,15,18,24,30,36]:
        d=stable_rank(n,40)
        D=0 if n%3 else (2 if n%2 else n&-n)
        counts=[];prev=0
        for t in range(D+1):
            cumulative=1<<(d+2*n-stable_rank(n,t))
            counts.append(cumulative-prev);prev=cumulative
        assert sum(counts)==1<<(2*n)
        print(n,d,D,counts if D<=8 else 'histogram_length='+str(len(counts)))
if __name__=='__main__': check()
