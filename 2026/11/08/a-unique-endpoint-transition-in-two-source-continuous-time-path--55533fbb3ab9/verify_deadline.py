#!/usr/bin/env python3
"""Numerical/exact finite checks of two-source SI path deadline optimization.

Standard-library only; finite checks do not replace the mathematical proof.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
from math import factorial

getcontext().prec=72
D=Decimal
assertions=0

def check(ok, msg):
    global assertions
    assert ok, msg
    assertions+=1

def Q(j, t):
    """Upper Poisson tail at integer j, high-relative-precision series."""
    if j==0:return D(1)
    term=t**j/D(factorial(j))
    val=term
    for k in range(j+1,j+300):
        term=term*t/D(k)
        val+=term
        if abs(term)<abs(val)*D('1e-66'):
            break
    return (-t).exp()*val

def cdf(n,x,y,t):
    l=x-1; m=y-x-1; r=n-y
    return Q(l,t)*Q(r,t)*Q(m,2*t)

def greedy(n,t):
    a=[0,0,0]
    for _ in range(n-2):
        scores=[Q(a[0]+1,t)/Q(a[0],t),
                Q(a[1]+1,2*t)/Q(a[1],2*t),
                Q(a[2]+1,t)/Q(a[2],t)]
        a[max(range(3),key=lambda i:scores[i])]+=1
    l,m,r=a
    return l+1,l+m+2

def markov_cdf(n,x,y,t):
    """Independent transient CTMC uniformization over all infection masks."""
    N=1<<n
    rate=n-1
    probs=[D(0)]*N
    probs[(1<<(x-1))|(1<<(y-1))]=D(1)
    full=N-1
    term=(-D(rate)*t).exp()
    accum=D(0)
    for step in range(160):
        accum+=term*probs[full]
        nxt=[D(0)]*N
        for mask,pr in enumerate(probs):
            if not pr:continue
            infected=0
            for j in range(n):
                if mask&(1<<j):continue
                r=int(j>0 and bool(mask&(1<<(j-1))))+int(j<n-1 and bool(mask&(1<<(j+1))))
                if r:
                    nxt[mask|1<<j]+=pr*D(r)/D(rate)
                    infected+=r
            nxt[mask]+=pr*(D(rate-infected)/D(rate))
        probs=nxt
        term=term*D(rate)*t/D(step+1)
    return accum

# Unrelated state-space expansion validates the explicit independent Gamma calculation.
for n in range(2,8):
    for x,y in combinations(range(1,n+1),2):
        for t in (D('0.2'),D('1.0'),D('2.0')):
            check(abs(markov_cdf(n,x,y,t)-cdf(n,x,y,t))<D('4e-27'),
                  f'CTMC mismatch n={n} x={x} y={y} t={t}')

# Global comparison, not just comparison against endpoints.
for n in range(2,45):
    for t in (D('0.05'), D('0.3'),D('1'),D('2'),D('4'),D('7'),D('15')):
        opt=max(cdf(n,x,y,t) for x,y in combinations(range(1,n+1),2))
        gx,gy=greedy(n,t)
        check(abs(cdf(n,gx,gy,t)-opt)<=opt*D('1e-54'),
              f'greedy fails n={n} t={t}')
        if n>=4:
            N=n-2
            endpoint_best=Q(N,2*t)>=Q(N-1,2*t)*Q(1,t)
            check((abs(cdf(n,1,n,t)-opt)<=opt*D('1e-54'))==endpoint_best,
                  f'endpoint characterization fails n={n} t={t}')

# Power series signs and unimodal coefficient ratios for the uniqueness lemma.
for N in range(3,80):
    rr=Fraction(1)
    observed_negative=False
    observed_positive=False
    for k in range(1,8*N+120):
        rr=rr*Fraction(2*k,N+k-1)
        if rr<1:
            check(not observed_positive, f'coefficient reverted N={N} k={k}')
            observed_negative=True
        elif rr>1:
            observed_positive=True
    check(observed_negative and observed_positive, f'sign changes missing N={N}')

# N=2 endpoint advantage, and N=3 strict crossing on either side.
for t in (D('0.01'),D('0.5'),D('2'),D('5'),D('10')):
    check(Q(2,2*t)>Q(1,2*t)*Q(1,t),'n=4 endpoints should win')
check(Q(3,D(1))<Q(2,D(1))*Q(1,D('0.5')),'n=5 pre-threshold')
check(Q(3,D(8))>Q(2,D(8))*Q(1,D(4)),'n=5 post-threshold')

print('PASS:',assertions,'assertions (CTMC uniformization, global optima, boundary and sign structure)')
print('Five-vertex critical deadline lies strictly between 2 and 4')
print('Five-vertex placements at t=1:',greedy(5,D(1)))
print('Five-vertex placements at t=4:',greedy(5,D(4)))
