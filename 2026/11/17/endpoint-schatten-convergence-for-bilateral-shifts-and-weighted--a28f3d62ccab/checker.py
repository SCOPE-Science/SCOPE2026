"""Finite rational and floating-point diagnostics for weighted-shift identities.
This is supplementary testing; general statements are established analytically.
"""
from fractions import Fraction
from math import comb, exp, isclose, lgamma
import random


def binomial_weights(n, t):
    return [Fraction(comb(n, i))*t**i*(1-t)**(n-i) for i in range(n+1)]


def direct_iteration_power_weights(weights, t, n):
    w = list(map(Fraction, weights))
    for _ in range(n):
        w = [((1-t)*w[j]+t*w[j+1]) for j in range(len(w)-1)]
    return w


def exact_binomial_power_weights(weights, t, n):
    b = binomial_weights(n,t)
    return [sum((b[i]*weights[j+i] for i in range(n+1)),Fraction(0)) for j in range(len(weights)-n)]


def bound_p_power(u, t, n, R):
    b=[comb(n,i)*t**i*(1-t)**(n-i) for i in range(n+1)]
    keys=list(u)
    U=sum(u.values())
    tail=sum(v for k,v in u.items() if abs(k)>R)
    beta=max(sum(b[i] for i in range(n+1) if abs(k+i)<=R) for k in range(-n-R-2,R+3))
    alpha=1-beta
    rhs=(tail/alpha)**alpha*(U/beta)**beta if tail>0 else 0
    S=0
    for k in range(min(keys)-n-1,max(keys)+2):
        terms=[u.get(k+i,0) for i in range(n+1)]
        S+=exp(sum(float(b[i])*__import__('math').log(v) for i,v in enumerate(terms))) if all(terms) else 0
    return S,rhs,beta

assertions=0
for t in (Fraction(1,2),Fraction(1,3),Fraction(2,5)):
    for n in range(0,8):
        a=[Fraction(j*j+3*j+2,100+j) for j in range(n+12)]
        assert direct_iteration_power_weights(a,t,n)==exact_binomial_power_weights(a,t,n)
        assertions+=len(a)-n
random.seed(19422)
for t in (0.21,0.50,0.79):
    for n in (5,9,13,20,40,80):
        for R in (0,1,2):
            for trial in range(5):
                u={k:exp(-0.4*abs(k))+random.random()*exp(-abs(k)) for k in range(-15,16)}
                s,rhs,beta=bound_p_power(u,t,n,R)
                assert s<=rhs*(1+1e-11), (t,n,R,s,rhs)
                assert 0<beta<1,(t,n,R,beta)
                assertions+=2
# Exact scalar cyclic log dynamics: binomial update on cyclic indices.
for t in (Fraction(1,2),Fraction(1,3)):
    for L in range(2,10):
        logs=[Fraction(j*j+1,7*j+14) for j in range(L)]
        mean=sum(logs)/L
        curr=logs[:]
        for _ in range(500):
            curr=[(1-t)*curr[j]+t*curr[(j+1)%L] for j in range(L)]
            assert sum(curr)/L==mean
            assertions+=1
        assert max(abs(float(x-mean)) for x in curr)<1e-3
        assertions+=1
print('PASS',assertions,'finite assertions')
