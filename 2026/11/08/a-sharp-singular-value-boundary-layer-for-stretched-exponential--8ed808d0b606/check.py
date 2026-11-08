#!/usr/bin/env python3
"""Finite diagnostics for the stretched-exponential weighted-shift singular-value law.
The analytical proof is required for all infinite-dimensional and asymptotic statements.
"""
import math


def binomial_probabilities(n, theta):
    k0 = int((n+1)*theta)
    k0 = min(n, max(0, k0))
    values = [0.0] * (n+1)
    logp = (math.lgamma(n+1)-math.lgamma(k0+1)-math.lgamma(n-k0+1)
            +k0*math.log(theta)+(n-k0)*math.log1p(-theta))
    values[k0] = math.exp(logp)
    for k in range(k0, 0, -1):
        values[k-1] = values[k] * k/(n-k+1)*(1-theta)/theta
    for k in range(k0, n):
        values[k+1] = values[k]*(n-k)/(k+1)*theta/(1-theta)
    scale=sum(values)
    return [u/scale for u in values]


def mean_power(n, theta, alpha, j, probs=None):
    if probs is None:
        probs=binomial_probabilities(n,theta)
    return sum(p*(j+1+k)**alpha for k,p in enumerate(probs))


def power_difference(n, theta, alpha, j, probs):
    if j == 0:
        return 0.0
    return sum(p*((j+1+k)**alpha-(1+k)**alpha) for k,p in enumerate(probs))


def effective_schatten_mass(n, theta, alpha, c, p, limit=5000):
    probs = binomial_probabilities(n,theta)
    result = 0.0
    for j in range(limit):
        value=math.exp(-p*c*power_difference(n,theta,alpha,j,probs))
        result+=value
        if j>max(80,2*n) and value<1e-12:
            return result
    return result


def run():
    checks=0
    for theta in (0.2,0.4,0.65):
        for alpha in (0.5,1.0,1.5,2.0):
            for n in (0,2,4,8,12):
                probs=binomial_probabilities(n,theta) if n else [1.0]
                assert abs(sum(probs)-1)<1e-12
                checks+=1
                logs=[-0.8*(j+1)**alpha for j in range(22)]
                for _ in range(n):
                    logs=[(1-theta)*logs[j]+theta*logs[j+1] for j in range(len(logs)-1)]
                for j in range(8):
                    expected=-0.8*mean_power(n,theta,alpha,j,probs)
                    assert abs(logs[j]-expected)<1e-10*max(1,abs(expected)),(theta,alpha,n,j,logs[j],expected)
                    checks+=1
    for theta in (0.2,0.4,0.65):
        for n in (1,5,70):
            probs=binomial_probabilities(n,theta)
            for j in (0,1,4,18):
                delta=power_difference(n,theta,1.0,j,probs)
                assert abs(delta-j)<1e-10
                checks+=1
    for theta,alpha,c,p,n in (
        (0.4,1.0,0.8,1.5,70),
        (0.65,1.0,1.2,2.0,80),
        (0.4,0.5,0.8,1.5,500),
        (0.4,0.5,0.8,1.5,800),
        (0.4,1.5,0.8,1.5,500),
        (0.4,2.0,0.8,1.5,200),
    ):
        E=effective_schatten_mass(n,theta,alpha,c,p)
        if alpha == 1:
            predicted=1/(1-math.exp(-p*c))
            assert abs(E-predicted)<1e-10,(alpha,n,E,predicted)
        elif alpha>1:
            assert abs(E-1)<0.04,(alpha,n,E)
        else:
            predicted=n**(1-alpha)*theta**(1-alpha)/(p*c*alpha)
            assert abs(E/predicted-1)<0.10,(alpha,n,E,predicted)
        checks+=1
    print(f'Passed {checks} finite diagnostic assertions; not an asymptotic proof.')

if __name__=='__main__':
    run()
