#!/usr/bin/env python3
"""Optional seeded, finite-size numerical corroboration of hypersimplex width variances.

Pure Python and no dependencies beyond the standard library. Not a proof of asymptotics.
"""
from math import erf, exp, pi, sqrt
from random import Random
from statistics import variance
rng=Random(18271)
N,REPS=600,3000

def asymptotic_variance(t):
    density=exp(-t*t/2)/sqrt(2*pi)
    upper=(1-erf(t/sqrt(2)))/2
    m=2*(density-t*upper)
    return 2*((1+t*t)*upper-t*density)-m*m-2*density*density

for t in (0.5,1.0,1.5,2.0):
    alpha=(1-erf(t/sqrt(2)))/2
    k=int(alpha*N)
    assert 0<k<=N//2
    widths=[]
    for _ in range(REPS):
        g=[rng.gauss(0,1) for _ in range(N)]
        mean=sum(g)/N
        norm=sqrt(sum((x-mean)**2 for x in g))
        g.sort()
        widths.append((sum(g[-k:])-sum(g[:k]))/norm)
    sampled=variance(widths)
    predicted=asymptotic_variance(t)
    assert abs(sampled-predicted)<0.003,(t,sampled,predicted)
    print('t=',t,'n=',N,'k=',k,'sample_variance=',round(sampled,8),'limiting_variance=',round(predicted,8))
print('HYPERSIMPLEX_FINITE_SIZE_SAMPLING_PASSED')
