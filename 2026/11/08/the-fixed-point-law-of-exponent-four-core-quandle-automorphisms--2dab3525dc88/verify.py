#!/usr/bin/env python3
"""Exact integer and direct small-quandle checks for finite exponent-four core symmetries."""
from itertools import product
from fractions import Fraction
from collections import Counter
from math import comb
from math import prod

def linear(m, x, r):
    return sum((((m[i] & x).bit_count() & 1) << i) for i in range(r))

def gl(r):
    for rows in product(range(1 << r), repeat=r):
        if len({linear(rows,x,r) for x in range(1<<r)}) == (1<<r):
            yield rows

def gl_size(j):
    return prod((1 << j)-(1 << i) for i in range(j))

def gaussian_binom(n,k):
    if k<0 or k>n:return 0
    numerator=prod(((1 << (n-i))-1) for i in range(k))
    denominator=prod(((1 << (k-i))-1) for i in range(k))
    assert numerator%denominator==0
    return numerator//denominator

def p_inverse(r,d):
    return sum((Fraction((-1)**(j-d)* (1 << ((j-d)*(j-d-1)//2)) *gaussian_binom(j,d),gl_size(j)) for j in range(d,r+1)),Fraction(0))

def count_formula(r):
    c=1<<r; D=0; fixed_stats={}; matrices=0
    for m in gl(r):
        matrices+=1
        K=sum(linear(m,x,r)==x for x in range(c))
        assert K&(K-1)==0
        # exactly c/K affine translations have K quotient fixed points
        # all other c-c/K translations have none
        # avoid division: each of K fixed fibres has c-1 - (c/K-1) = c-c/K choices with no fixed points
        # and c free choices on non-fixed fibres
        deriv=(c-c//K)*c**c + (c//K)*c**(c-K)*(c-c//K)**K
        D+=deriv
        fixed_stats[K]=fixed_stats.get(K,0)+1
    total=matrices*c**(c+1)
    return D,total,fixed_stats

def brute_quandle(r):
    c=1<<r
    def decode(x):return tuple((x >> (2*i)) & 3 for i in range(r))
    def encode(v):return sum((v[i] << (2*i)) for i in range(r))
    A=[decode(x) for x in range(4**r)]
    N=len(A)
    Q=[[encode(tuple((2*y[i]-x[i])%4 for i in range(r))) for y in A] for x in A]
    D=0; count=0; hist=Counter()
    for m in gl(r):
        for a in range(c):
            for lift in product(range(c),repeat=c):
                perm=[]
                for x in A:
                    parity=sum(((x[i]&1)<<i) for i in range(r))
                    b=sum((((x[i]>>1)&1)<<i) for i in range(r))
                    y1=linear(m,parity,r)^a
                    y2=linear(m,b,r)^lift[parity]
                    perm.append(encode(tuple(((y1>>i)&1)+2*((y2>>i)&1) for i in range(r))))
                assert len(set(perm))==N
                assert all(perm[Q[x][y]]==Q[perm[x]][perm[y]] for x in range(N) for y in range(N))
                count+=1
                fcount=sum(perm[i]==i for i in range(N))
                hist[fcount]+=1
                D+=(fcount==0)
    return D,count,dict(sorted(hist.items()))

if __name__=='__main__':
    for r in range(1,5):
        D,T,stat=count_formula(r)
        for d in range(r+1):
            assert p_inverse(r,d)==Fraction(stat.get(1<<d,0),gl_size(r)),(r,d)
        print('r',r,'D',D,'total',T,'P',Fraction(D,T),'GL_kernel_stats',stat)
        if r<=2:
            d,t,hist=brute_quandle(r)
            assert (d,t)==(D,T),(r,d,t,D,T)
            predicted=Counter()
            c=1<<r
            for K,ct in stat.items():
                predicted[0]+=ct*(c-c//K)*c**c
                for j in range(K+1):
                    predicted[j*K]+=ct*(c//K)*comb(K,j)*(c//K)**j*(c-c//K)**(K-j)*c**(c-K)
            assert hist==dict(sorted(predicted.items()))
            print('direct_checked',r,d,t,hist)
    print('DERANGEMENT_VERIFY_OK')
