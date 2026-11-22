"""Finite checks for sharp mixed-norm stability of a positive-weight exponential map."""
from itertools import product
from math import exp, log, cosh
from fractions import Fraction
import random


def discrepancy(weights):
    total=sum(weights)
    candidates=[]
    n=len(weights)
    for signs in product((0,1),repeat=n):
        k=sum(w for w,b in zip(weights,signs) if b)
        if 0<k<total:
            candidates.append(abs(log(k/(total-k))))
    return min(candidates)

def expected(weights, beta, radius):
    if radius == 0:
        return 0.0
    d=max(0, discrepancy(weights)-beta*radius)
    return beta/cosh(d/2)**2

def softmax(x, weights, beta):
    a=[log(c)+beta*u for c,u in zip(weights,x)]
    z=max(a)
    e=[exp(u-z) for u in a]
    return [v/sum(e) for v in e]

def jac_norm(p,beta):
    # exact binary variation variational formula by exhaustive signs
    n=len(p)
    return max(4*beta*sum(p[i] for i in range(n) if flags[i])*(1-sum(p[i] for i in range(n) if flags[i])) for flags in product((0,1),repeat=n))

def sharp_candidate(weights, beta, radius):
    n=len(weights)
    total=sum(weights)
    best=(float('inf'),None)
    for flags in product((0,1),repeat=n):
        a=sum(w for w,b in zip(weights,flags) if b)
        if not 0<a<total:continue
        raw=log(a/(total-a))
        if abs(raw)<best[0]:best=(abs(raw), flags)
    raw,bits=best
    # tilt towards half mass using maximal allowed logit range
    t=min(radius,raw/beta)
    if sum(w for w,b in zip(weights,bits) if b)*2<total:
        x=[t if b else 0 for b in bits]
    else:
        x=[0 if b else t for b in bits]
    return x

def run():
    rng=random.Random(55441)
    total_tests=0
    # All small integer weight patterns, tested at several positive diameters.
    for n in range(2,6):
        for w in product(range(1,5),repeat=n):
            for beta,r in [(1,0.000001),(1,0.03),(1,0.3),(1,2.0),(2,0.1)]:
                x=sharp_candidate(w,beta,r)
                assert max(x)-min(x)<=r+1e-12
                p=softmax(x,w,beta)
                actual=jac_norm(p,beta)
                target=expected(w,beta,r)
                assert abs(actual-target)<=2e-11*max(1,target),(w,beta,r,actual,target)
                total_tests+=1
    # Independent Monte Carlo two-point Lipschitz ratios: never exceed sharp coefficient.
    for n in range(2,13):
        for j in range(200):
            w=[rng.randint(1,80) for _ in range(n)]
            beta=rng.uniform(.2,3.2)
            r=rng.uniform(.01,2.)
            x=[rng.uniform(0,r) for _ in w]
            y=[rng.uniform(0,r) for _ in w]
            px=softmax(x,w,beta)
            py=softmax(y,w,beta)
            ratio=sum(abs(a-b) for a,b in zip(px,py))/max(abs(a-b) for a,b in zip(x,y))
            assert ratio<=expected(w,beta,r)*(1+2e-11)
            total_tests+=1
    # Positive-width boundary can be approximated by interior Jacobians in any direction.
    for n in range(2,11):
        w=[rng.randint(1,10) for _ in range(n)]
        beta=1.3;r=.2
        x=sharp_candidate(w,beta,r)
        xx=[(1-1e-6)*v for v in x]
        p=softmax(xx,w,beta)
        assert jac_norm(p,beta) >= expected(w,beta,r)-1e-5
        total_tests+=1
    # NP-hardness reduction gap for bounded total integer weights, exhaustive small examples.
    for n in range(2,7):
        for w in product(range(1,4),repeat=n):
            C=sum(w)
            balanced=any(2*sum(w[i] for i,b in enumerate(bits) if b)==C for bits in product((0,1),repeat=n))
            assert (discrepancy(w)<=1/C) == balanced
            total_tests+=1
    # edge case R=0: domain consists only of constants.
    assert expected([1,1,1],1,0)==0
    total_tests+=1
    print('PASS',total_tests,'supplementary checks')

if __name__=='__main__':run()
