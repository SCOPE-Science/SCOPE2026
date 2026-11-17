#!/usr/bin/env python3
"""Exact rational checks for the complete-graph mean-max variation theorem."""
from fractions import Fraction as Q
from itertools import product
from math import floor
import random

def variation(v):
    return sum((abs(v[i]-v[j]) for i in range(len(v)) for j in range(i+1,len(v))), Q(0))

def maximal(v):
    assert all(t>=0 for t in v)
    a=sum(v,Q(0))/len(v)
    return [max(t,a) for t in v]

def constant(n):
    if n==2: return Q(1,2)
    return 1+Q(((n-2)**2)//4,n*(n-1))

def active_cut_j(n,k,l,x):
    z=k-x
    return Q((n-l)*x*(n-x)+l*z*(n-z), n)

def all_cuts():
    n_cases=0
    for n in range(2,32):
        bound=constant(n)
        top=Q(0); where=None
        for k in range(1,n):
            for l in range(1,n):
                for x in range(max(0,k+l-n),min(k,l)+1):
                    r=active_cut_j(n,k,l,x)/Q(l*(n-l))
                    n_cases+=1
                    assert r<=bound, (n,k,l,x,r,bound)
                    if r>top:top=r;where=(k,l,x)
        assert top==bound,(n,top,bound,where)
    print('EXACT_ACTIVE_CUT_TABLES_PASSED',n_cases)

def brute():
    count=0
    for n in range(2,9):
        for smask in range(1,(1<<n)-1):
            S={i for i in range(n) if smask>>i&1}
            for umask in range(1,(1<<n)-1):
                U={i for i in range(n) if umask>>i&1}
                h=[Q(int(i in U)) for i in range(n)]
                mean=sum(h)/n
                Ah=[h[i] if i in S else mean for i in range(n)]
                r=variation(Ah)/variation(h)
                assert r<=constant(n)
                assert variation(Ah)==active_cut_j(n,len(S),len(U),len(S&U))
                count+=1
    print('INDEPENDENT_EXPLICIT_ACTIVE_CUTS_PASSED',count)

def explicit():
    count=0
    for n in range(2,301):
        if n==2: S={0}
        else: S=set(range(1+n//2))
        f=[Q(1 if i in S else 0) for i in range(n)]
        g=f.copy();g[0]+=Q(1,1000)
        v=variation([a-b for a,b in zip(maximal(g),maximal(f))]);
        d=variation([a-b for a,b in zip(g,f)])
        assert v/d==constant(n),(n,v/d,constant(n))
        count+=1
    print('EXACT_STRICT_BRANCH_WITNESSES_PASSED',count)

def randomized():
    rng=random.Random(10731)
    count=0
    for n in range(2,20):
        for _ in range(200):
            a=[Q(rng.randrange(10),rng.randrange(1,6)) for _ in range(n)]
            b=[Q(rng.randrange(10),rng.randrange(1,6)) for _ in range(n)]
            inp=variation([x-y for x,y in zip(a,b)])
            if not inp:continue
            out=variation([x-y for x,y in zip(maximal(a),maximal(b))])
            assert out<=constant(n)*inp,(n,a,b,out,inp)
            count+=1
    print('EXACT_TWO_INPUT_RATIONAL_PAIRS_PASSED',count)

def signed():
    for n in range(2,21):
        f=[Q(1),Q(-1)]+[Q(0)]*(n-2)
        g=[z+Q(1,10) for z in f]
        def Mabs(x): return maximal(list(map(abs,x)))
        assert variation([x-y for x,y in zip(Mabs(f),Mabs(g))])>0
        assert variation([x-y for x,y in zip(f,g)])==0
    print('SIGNED_SEMINORM_OBSTRUCTION_CHECKS_PASSED',19)

if __name__=='__main__':
    all_cuts();brute();explicit();randomized();signed()
    print('ALL_COMPLETE_GRAPH_TWO_INPUT_BV_CHECKS_PASSED')
