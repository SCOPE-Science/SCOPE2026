#!/usr/bin/env python3
"""Finite independent enumeration for joint burst-deletion sphere statistics.
Scientific arithmetic only; no external dependencies.
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import gcd, comb

def descendants(w, b):
    return {w[:i]+w[i+b:] for i in range(len(w)-b+1)}

def B(w, b):
    return len(descendants(w, b))

def predicted(w, b):
    return 1+sum(w[i] != w[i+b] for i in range(len(w)-b))

def enumerate_one(q,n):
    counts=Counter()
    single={b:Counter() for b in range(1,n)}
    for w in product(range(q),repeat=n):
        v=[B(w,b) for b in range(1,n)]
        for b,x in enumerate(v,1):
            assert x==predicted(w,b),(q,n,w,b,x,predicted(w,b))
            single[b][x]+=1
        counts[tuple(v)]+=1
    N=q**n
    for b in range(1,n):
        for k in range(n-b+1):
            assert single[b][k+1] == q**b*comb(n-b,k)*(q-1)**k, (q,n,b,k,single[b][k+1])
    for a,b in combinations(range(1,n),2):
        joint=Counter()
        for v,c in counts.items():
            joint[(v[a-1],v[b-1])]+=c
        independent=all(c*N==single[a][u]*single[b][v] for (u,v),c in joint.items())
        # Check even cells not in joint: if independence predicted, every marginal combination must occur
        independent=independent and all(joint[(u,v)]*N==cu*cv for u,cu in single[a].items() for v,cv in single[b].items())
        pred_ind=n <= a+b-gcd(a,b)
        assert independent == pred_ind,(q,n,a,b,independent,pred_ind)
        joint_min=sum(z for (u,v),z in joint.items() if u==1 and v==1)
        beta=max(0,n-a-b+gcd(a,b))
        assert joint_min == q**(a+b-n+beta),(q,n,a,b,joint_min,beta)
        mean_a=Fraction(1,1)+Fraction((n-a)*(q-1),q)
        mean_b=Fraction(1,1)+Fraction((n-b)*(q-1),q)
        cov=sum(Fraction(c,N)*(u-mean_a)*(v-mean_b) for (u,v),c in joint.items())
        assert cov==0,(q,n,a,b,cov)
    for a,b,c in combinations(range(1,n),3):
        means=[Fraction(1,1)+Fraction((n-d)*(q-1),q) for d in (a,b,c)]
        obs=sum(Fraction(count,N)*(v[a-1]-means[0])*(v[b-1]-means[1])*(v[c-1]-means[2]) for v,count in counts.items())
        expected=Fraction(-2*(n-c)*(q-1),q**3) if a+b==c else Fraction(0)
        assert obs==expected,(q,n,a,b,c,obs,expected)
    return (q,n,N,len(counts))

if __name__=='__main__':
    todo=[(2,n) for n in range(2,10)]+[(3,n) for n in range(2,8)]+[(4,n) for n in range(2,7)]
    for q,n in todo:
        print('CHECKED',*enumerate_one(q,n))
    print('ALL_BURST_JOINT_STATISTICS_PASSED',len(todo),'parameter_cases')
