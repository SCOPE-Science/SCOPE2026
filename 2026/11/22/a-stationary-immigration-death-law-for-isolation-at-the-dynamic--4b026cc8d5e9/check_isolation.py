#!/usr/bin/env python3
"""Reproducible finite and asymptotic checks for an evolving Bernoulli graph.

Run: python3 check_isolation.py
Only standard-library modules are required.
"""
from fractions import Fraction
from itertools import product, combinations
from math import exp, log, factorial

CHECKS = 0

def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1

def q_snapshot(p, a, S):
    """Edge is zero at every sampled index in S, for two samples."""
    if S == (0,) or S == (1,):
        return 1 - p
    if S == (0, 1):
        return (1 - p) * (1 - p * (1-a))
    raise ValueError(S)

def exact_joint_tagged(n,p,a,tagged):
    """Formula for designated vertices; each tag is (vertex, sample-index-set)."""
    tags = dict(tagged)
    out = 1
    for (v,S) in tagged:
        out *= q_snapshot(p,a,tuple(sorted(S))) ** (n-len(tags))
    for v,w in combinations(tags,2):
        out *= q_snapshot(p,a,tuple(sorted(set(tags[v])|set(tags[w]))))
    return out

def brute(n,p,a,tagged):
    edges=list(combinations(range(n),2))
    prob=( (1-p)*((1-p)+p*a), (1-p)*p*(1-a), p*(1-p)*(1-a), p*(p+(1-p)*a) )
    states=((0,0),(0,1),(1,0),(1,1))
    total=Fraction(0)
    for codes in product(range(4), repeat=len(edges)):
        weight=Fraction(1)
        for code in codes:
            weight *= prob[code]
        if not weight:
            continue
        wanted=True
        for v,S in tagged:
            for idx,(i,j) in enumerate(edges):
                if v==i or v==j:
                    if any(states[codes[idx]][t] for t in S):
                        wanted=False
                        break
            if not wanted:
                break
        if wanted:
            total+=weight
    return total

for n in (3,4):
    for p,a in ((Fraction(1,4),Fraction(1,2)),(Fraction(2,5),Fraction(3,4))):
        for tagged in (
            ((0,(0,)),), ((0,(0,1)),),
            ((0,(0,)),(1,(1,))), ((0,(0,1)),(1,(1,))),
            ((0,(1,)),(1,(0,))),
            ((0,(0,)),(1,(0,)),(2,(1,))),
        ):
            expected=exact_joint_tagged(n,p,a,tagged)
            actual=brute(n,p,a,tagged)
            check(actual==expected, f'joint n={n} p={p} a={a} tagged={tagged}')


def q_n(n, x, times):
    p=(log(n)+x)/n
    logq=log(1-p)
    for i in range(1,len(times)):
        logq+=log(1-p*(1-exp(-(times[i]-times[i-1])/log(n))))
    return exp(logq)

def mu_n(n,x,ts,subset):
    """Expected count of vertices isolated at precisely subset of snapshots."""
    m=len(ts)
    complement=[j for j in range(m) if j not in subset]
    total=0.0
    for flags in product((0,1), repeat=len(complement)):
        more=[complement[k] for k,b in enumerate(flags) if b]
        ind=sorted(subset+tuple(more))
        total+=(-1)**len(more)*q_n(n,x,[ts[j] for j in ind])**(n-1)
    return n*total

def mu_limit(x,ts,subset):
    if not subset or tuple(range(subset[0],subset[-1]+1))!=subset:
        return 0.
    a,b=subset[0],subset[-1]
    value=exp(-x-(ts[b]-ts[a]))
    if a: value*=1-exp(-(ts[a]-ts[a-1]))
    if b+1<len(ts): value*=1-exp(-(ts[b+1]-ts[b]))
    return value

x=0.2
for ts in ((0.,0.9),(0.,0.6,1.7),(0.,0.5,1.2,2.6)):
    m=len(ts)
    for n in (10000,40000):
        errors=[]
        for mask in range(1,2**m):
            subset=tuple(i for i in range(m) if mask&(1<<i))
            got=mu_n(n,x,ts,subset)
            expect=mu_limit(x,ts,subset)
            check(abs(got-expect)<0.06, f'limit n={n} ts={ts} subset={subset}: {got}, {expect}')
        for j in range(m):
            mass=sum(mu_limit(x,ts,tuple(i for i in range(m) if mask&(1<<i))) for mask in range(1,2**m) if mask&(1<<j))
            check(abs(mass-exp(-x))<1.e-12, f'stationary mass {ts},{j}')

for n in (5000,20000,80000):
    for t in (0.2,1.1,2.3):
        p=(log(n)+x)/n
        q0=1-p
        q2=q_n(n,x,(0.,t))
        mean=n*q0**(n-1)
        joint=n*q2**(n-1)+n*(n-1)*q0**(2*(n-2))*q2
        covariance=joint-mean**2
        check(abs(covariance-exp(-x-t))<0.05, f'covariance {n} {t} {covariance}')

# The connected-block profile intensities must be nonnegative and cover one-time means.
for m in range(2,8):
    ts=tuple(float(i*i)/4 for i in range(m))
    for mask in range(1,2**m):
        subset=tuple(i for i in range(m) if mask&(1<<i))
        check(mu_limit(0.4,ts,subset)>=0, f'mass sign m={m}, mask={mask}')

print(f'PASS {CHECKS} deterministic assertions')
