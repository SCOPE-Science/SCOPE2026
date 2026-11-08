#!/usr/bin/env python3
"""Finite exact and sampled checks of a coupling for linear anti-preferential attachment.
Run: python3 verify.py; Python standard library. Finite tests are not infinite proofs.
"""
from fractions import Fraction
from collections import Counter
from math import log, isclose
from random import Random
from itertools import product

checks=0

def verify(condition, label):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(label)

def old_probs(degs):
    n=len(degs)
    D=sum(degs)
    return [Fraction(1, n-1)*(1-Fraction(d,D)) for d in degs]

def one_step_distributions(state, m):
    """Enumerate all sequential m-edge attachments to old vertices."""
    outcomes={tuple(state):Fraction(1)}
    for _ in range(m):
        next_outcomes={}
        for degs,mass in outcomes.items():
            probs=old_probs(degs)
            verify(sum(probs)==1,('normalization',degs))
            verify(all(z>=0 for z in probs),('nonnegative',degs))
            n=len(degs); D=sum(degs)
            for j in range(n):
                r=Fraction(degs[j],D)
                verify(probs[j]==Fraction(1,n)*(1-r)/Fraction(n-1,n),('rejection identity',degs,j))
            verify(sum(Fraction(degs[j],n*D) for j in range(n))==Fraction(1,n),('reject probability',degs))
            for j,prob in enumerate(probs):
                arr=list(degs)
                arr[j]+=1
                arr=tuple(arr)
                next_outcomes[arr]=next_outcomes.get(arr,Fraction(0))+mass*prob
        outcomes=next_outcomes
    return {s+(m,):p for s,p in outcomes.items()}

def exact_checks():
    for m in (1,2,3):
        states={tuple((m,2*m)):Fraction(1)}
        for n in range(2,6):
            next_states={}
            for state,mass in states.items():
                verify(sum(state)==m*(2*n-1),('old total degrees',m,n,state))
                outcomes=one_step_distributions(state,m)
                for s,pr in outcomes.items():
                    verify(sum(s)==m*(2*(n+1)-1),('new total degrees',m,n,s))
                    next_states[s]=next_states.get(s,Fraction(0))+pr*mass
            states=next_states
            verify(sum(states.values())==1,('global mass',m,n))
    # Uniform recursive model exact finite mixture: individual excess indegree distribution.
    for m in (1,2,3):
        for N in range(4,15):
            for born in range(3,N+1):
                poly=[Fraction(1)]
                for n in range(born,N):
                    a=Fraction(1,n)
                    for _ in range(m):
                        nxt=[Fraction(0)]*(len(poly)+1)
                        for k,x in enumerate(poly):
                            nxt[k]+=x*(1-a)
                            nxt[k+1]+=x*a
                        poly=nxt
                verify(sum(poly)==1,('uniform poisson-binomial norm',m,N,born))
                verify(sum(i*v for i,v in enumerate(poly))==m*sum(Fraction(1,n) for n in range(born,N)),('uniform mean',m,N,born))

def couple_simulate(m, N, seed):
    rng=Random(seed)
    orig=[m,2*m]
    unif=[m,2*m]
    rejected=0
    mismatched=0
    for n in range(2,N):
        for step in range(m):
            D=sum(orig) if n<5 else (2*n-1)*m+step
            verify(D==sum(orig) if n<5 else D==(2*n-1)*m+step,('degree formula',n,step))
            u=rng.randrange(n)
            y=u
            if rng.random()<orig[u]/D:
                rejected+=1
                while True:
                    y=rng.randrange(n)
                    if rng.random()>=orig[y]/D:
                        break
            if y!=u:
                mismatched+=1
            unif[u]+=1
            orig[y]+=1
        orig.append(m)
        unif.append(m)
    verify(mismatched<=rejected,('mismatch<=rejections',m,N))
    ca=Counter(orig)
    cb=Counter(unif)
    total_variation=sum(abs(ca.get(k,0)-cb.get(k,0)) for k in ca.keys()|cb.keys())/(2*N)
    verify(total_variation<=2*rejected/N,('histogram TV coupling',m,N,total_variation,rejected))
    verify(abs(rejected-m*log(N/2))<max(25,8*(m*log(N))**0.5),('rejection typical',m,N,rejected))
    for r in range(0,8):
        target=1/(m+1)*(m/(m+1))**r
        empirical=cb.get(m+r,0)/N
        if N>=10000:
            verify(abs(empirical-target)<0.027,('geometric comparison',m,N,r,empirical,target))
    return rejected,mismatched,total_variation

if __name__=='__main__':
    exact_checks()
    for m in (1,2,3):
        outcome=couple_simulate(m,20000,131+m)
        print('simulation',m,outcome)
    print('VERIFY_OK check_count=',checks)
    print('LIMITS: independent analytic Borel-Cantelli and concentration arguments prove almost-sure limit; finite checks do not.')
