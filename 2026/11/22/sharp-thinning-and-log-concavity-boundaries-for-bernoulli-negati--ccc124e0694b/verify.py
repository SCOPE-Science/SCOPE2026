#!/usr/bin/env python3
"""Exact-rational diagnostic checks for Bernoulli--negative-binomial divisibility thresholds.
No finite grid proves the infinite-degree statements in RESULT.md.
"""
from fractions import Fraction as Q
from random import Random

def conditions(nu, theta, p):
    odds = p / (1-p)
    infinitely_divisible = odds <= theta and odds*odds <= nu*theta*theta
    thinning_self_decomposable = (odds <= theta and
        nu*(1-theta)*theta*theta >= (1+odds)*odds*odds)
    log_concave = nu >= 1
    return infinitely_divisible, thinning_self_decomposable, log_concave

def canonical(nu, theta, p, k):
    odds = p/(1-p)
    return (nu*theta**k + (1 if k%2 else -1)*odds**k)/k

def mass_coefficients(nu, theta, p, end):
    base = [Q(1)]
    for k in range(1,end+1):
        base.append(base[-1]*theta*(nu+k-1)/k)
    return [(1-p)*base[k] + (p*base[k-1] if k else 0)
            for k in range(end+1)]

def check():
    rng=Random(604219)
    count=0
    examples=[(Q(2),Q(1,2),Q(1,4),(True,True,True)),
              (Q(1),Q(1,2),Q(1,4),(True,False,True)),
              (Q(1),Q(1,2),Q(2,5),(False,False,True)),
              (Q(1,4),Q(1,2),Q(1,10),(True,True,False))]
    for nu,theta,p,expect in examples:
        assert conditions(nu,theta,p)==expect
        assert (nu*theta**2/(1-theta)**2-p*p)>0
        count+=2
    for _ in range(210):
        nu=Q(rng.randint(1,12),rng.randint(1,13))
        theta=Q(rng.randint(1,12),rng.randint(13,26))
        p=Q(rng.randint(1,12),rng.randint(13,26))
        odds=p/(1-p)
        id_case,dsd_case,lc_case=conditions(nu,theta,p)
        masses=mass_coefficients(nu,theta,p,24)
        assert all(v>0 for v in masses); count+=1
        # Differentiate the probability generating function and match
        # every coefficient through degree 22 in G' = G (log G)'.
        for k in range(1,23):
            lhs=k*masses[k]
            rhs=sum(j*canonical(nu,theta,p,j)*masses[k-j]
                    for j in range(1,k+1))
            assert lhs == rhs
            count+=1
        if id_case:
            for k in range(1,24):
                assert canonical(nu,theta,p,k)>=0
                count+=1
        if dsd_case:
            for k in range(1,23):
                assert k*canonical(nu,theta,p,k) >= (k+1)*canonical(nu,theta,p,k+1)
                count+=1
        if lc_case:
            for k in range(1,23):
                assert masses[k]**2>=masses[k-1]*masses[k+1]
                count+=1
        # For failure, identify the *infinite* obstruction analytically:
        # if odds > theta, eventually even coefficients turn negative;
        # otherwise degree 2 decides the failure.
        if not id_case and odds<=theta:
            assert canonical(nu,theta,p,2)<0
            count+=1
        if id_case and not dsd_case:
            assert (2*canonical(nu,theta,p,2)
                    <3*canonical(nu,theta,p,3))
            count+=1
    print('Exact rational diagnostic assertions:',count)
    print('Four contrasting parameter points passed.')
    return count

if __name__=='__main__':
    check()
