#!/usr/bin/env python3
"""Independent exact rank and Walsh checks on the six-variable alternating-form metric."""
from collections import Counter
from fractions import Fraction
from math import comb

PAIRS = [(i,j) for i in range(6) for j in range(i+1,6)]
SIZE=1<<15

def half_rank(mask):
    rows=[0]*6
    for j,(a,b) in enumerate(PAIRS):
        if mask & (1<<j):
            rows[a]^=1<<b
            rows[b]^=1<<a
    pivot=0
    for col in range(6):
        t=next((x for x in range(pivot,6) if (rows[x]>>col)&1),None)
        if t is None:continue
        rows[pivot],rows[t]=rows[t],rows[pivot]
        for x in range(pivot+1,6):
            if (rows[x]>>col)&1:rows[x]^=rows[pivot]
        pivot+=1
    assert pivot%2==0
    return pivot//2

def walsh(vec):
    n=len(vec)
    step=1
    while step<n:
        for block in range(0,n,step*2):
            for j in range(block,block+step):
                a,b=vec[j],vec[j+step]
                vec[j]=a+b
                vec[j+step]=a-b
        step*=2
    return vec

def coeff(q,r):
    x=q**2-q+1
    y=q**2+q+1
    if r==1:
        return (q**7+q**5-q**4-q**2-1,
                q**2*(q-1)*(q**2+q+1)*(q**5-q**4-q**2-1),
                -q**6*(q-1)**2*(q**2+q+1))
    if r==2:
        return (q**5-q**4-q**2-1,
                -q**2*(q**5-q**4+q**3-q**2-1),
                q**6*(q-1))
    return (-x*y,q**2*x*y,-q**6)

def orbit_counts(q):
    M=((q**6-1)*(q**5-1))//((q**2-1)*(q-1))
    counts=[1,(q-1)*M,M*q**2*(q-1)*(q**3-1),q**6*(q-1)*(q**3-1)*(q**5-1)]
    assert sum(counts)==q**15
    return counts

def check_q2():
    ranks=[half_rank(k) for k in range(SIZE)]
    dist=Counter(ranks)
    assert tuple(dist[j] for j in range(4))==tuple(orbit_counts(2))
    trans=[None]+[walsh([int(r==j) for r in ranks]) for j in range(1,4)]
    for r in range(1,4):
        expected=coeff(2,r)
        xs=[i for i,t in enumerate(ranks) if t==r]
        for j in range(3):
            assert all(trans[j+1][i]==expected[j] for i in xs), (r,j)
        assert sum(expected)==-1
    assert (coeff(2,1),coeff(2,2),coeff(2,3))==(
        (139,308,-448),(11,-76,64),(-21,84,-64))
    print('q=2: all 32,768 Fourier characters and the three complete shell spectra match')

def check_numeric():
    import math
    for q in (2,3,4,5,7,11):
        count=orbit_counts(q)
        for r in (1,2,3):
            assert sum(coeff(q,r))==-1
        def f(r,p):
            a,b,c=coeff(q,r)
            return a+b*2**p+c*3**p
        low,high=0.0,1.0
        while f(2,high)<0:
            high*=2
        for _ in range(100):
            mid=(low+high)/2
            if f(2,mid)>0:high=mid
            else:low=mid
        beta=(low+high)/2
        assert f(2,beta*0.9)<0 and f(2,beta*1.1)>0
        assert all(f(r,beta*1.1)<0 for r in (1,3))
        if q==2:assert 0.05334<beta<0.05335 and q**15-1-count[2]==14539
        print(f'q={q}  beta={beta:.14g}  endpoint_nullity={count[2]}')
    print('ALTERNATING_SIX_NEGATIVE_TYPE_SPECTRUM_PASS')

if __name__=='__main__':
    check_q2()
    check_numeric()
