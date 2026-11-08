#!/usr/bin/env python3
"""Self-contained finite checks for stochastic party-list welfare-price identities.
Inputs are artificial mathematical instances. Run with Python 3 standard library.
"""
from itertools import product
from math import comb, factorial, sqrt, log, log2, exp
from fractions import Fraction
from collections import Counter
from random import Random


def vectors(total, size):
    if size == 1:
        yield (total,)
        return
    for x in range(total+1):
        for rest in vectors(total-x, size-1):
            yield (x,)+rest


def axioms_truth(profile, x, a):
    n=len(profile); ell=n*a; r=len(x)
    assert sum(x)==ell
    groups=[]
    for mask in range(1,1<<n):
        S=[i for i in range(n) if mask>>i&1]
        common=set.intersection(*(set([profile[i]]) for i in S))
        if not common: continue
        party=next(iter(common)); required=ell*len(S)//n
        groups.append((S,party,required))
    pjr=all(x[party]>=q for S,party,q in groups)
    ejr=all(any(x[profile[i]]>=q for i in S) for S,party,q in groups)
    # Static-profile EJR+ literal group/round check, using maximum sigma and tau.
    ejrp=True
    for S,party,q in groups:
        for sigma in range(1,len(S)+1):
            for tau in range(1,ell+1):
                threshold=tau*sigma//n
                # if any round is assigned to a candidate other than the unanimously approved one
                if ell-x[party]>0 and max(x[profile[i]] for i in S)<threshold:
                    ejrp=False
    return pjr,ejr,ejrp


def check_all():
    tested=0
    for n in range(2,6):
        for r in range(1,4):
            for a in (1,2):
                ell=n*a
                for profile in product(range(r),repeat=n):
                    pop=Counter(profile)
                    formula = n*max(pop.values())/sum(v*v for v in pop.values())
                    best=[-1,-1,-1]
                    for x in vectors(ell,r):
                        checks=axioms_truth(profile,x,a)
                        welfare=sum(pop.get(i,0)*x[i] for i in range(r))
                        for j,ok in enumerate(checks):
                            if ok: best[j]=max(best[j],welfare)
                    expected=a*sum(v*v for v in pop.values())
                    if tuple(best)!=(expected,)*3:
                        raise AssertionError((n,r,a,profile,best,expected))
                    assert all(abs((ell*max(pop.values()))/w - formula)<1e-10 for w in best)
                    tested+=1
    return tested


def falling(x,d):
    v=1
    for z in range(d): v*=x-z
    return v


def check_occupancy_moments():
    checks=0
    for n in range(2,7):
        for r in range(1,5):
            for k in range(2,min(4,n)+1):
                for d in range(1,min(r,n//k)+1):
                    total=0
                    for picks in product(range(r),repeat=n):
                        pop=Counter(picks)
                        y=sum(pop.get(i,0)==k for i in range(r))
                        total+=falling(y,d)
                    observed=Fraction(total,r**n)
                    theory=(Fraction(falling(r,d)*falling(n,k*d),factorial(k)**d*r**(k*d))
                            *Fraction(r-d,r)**(n-k*d))
                    assert observed==theory, (n,r,k,d,observed,theory)
                    checks+=1
    return checks


def simulation():
    rng=Random(1729)
    result=[]
    for n,r,reps in [(100,3,2500),(300,3,2500),(500,500,1200),(1000,1000,1200),(10000,10000,200)]:
        price=[]
        for _ in range(reps):
            cnt=[0]*r
            for _ in range(n): cnt[rng.randrange(r)]+=1
            price.append(n*max(cnt)/sum(v*v for v in cnt))
        result.append((n,r,reps,round(sum(price)/reps,6),round(max(price),6)))
    return result

def birthday_simulation():
    rg=Random(271828)
    reports=[]
    for n,k,c,reps in ((1200,2,.5,1500),(1800,3,1.,1400),(1800,4,1.,1300)):
        parties=round(c*n**(k/(k-1)))
        hits=0
        for _ in range(reps):
            pop=Counter(rg.randrange(parties) for j in range(n))
            hits+=(max(pop.values())==k)
        p=1-exp(-1/(factorial(k)*c**(k-1)))
        reports.append((n,k,parties,reps,round(hits/reps,4),round(p,4)))
    return reports


if __name__=='__main__':
    n=check_all()
    print('exact literal PJR/EJR/EJR+ quota verification profiles:',n)
    print('exact sparse-occupancy factorial moments:',check_occupancy_moments())
    for row in simulation():print('simulation n r rep mean max:',*row)
    for row in birthday_simulation():print('birthday window n k R reps empirical_p limit_p:',*row)
