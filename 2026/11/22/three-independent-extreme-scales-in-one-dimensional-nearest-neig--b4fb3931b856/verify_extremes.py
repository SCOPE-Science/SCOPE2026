#!/usr/bin/env python3
"""Finite checks for geometric extrema of a one-dimensional uniform sample.

Run: python verify_extremes.py
All displayed numerical checks are diagnostics, not proofs of an asymptotic law.
"""
import itertools
import math
import numpy as np


def direct_statistics(gaps):
    """Build sites from positive consecutive gaps, then compute graph lengths."""
    sites = [0]
    for d in gaps:
        sites.append(sites[-1] + d)
    n = len(sites)
    neighbors = []
    for i in range(n):
        j = min((j for j in range(n) if j != i),
                key=lambda j: (abs(sites[j]-sites[i]), j))
        neighbors.append(j)
    longest_gap = max(gaps)
    longest_directed = max(abs(sites[i]-sites[neighbors[i]]) for i in range(n))
    reciprocal = [abs(sites[i]-sites[j]) for i,j in enumerate(neighbors)
                  if i<j and neighbors[j]==i]
    assert reciprocal
    return longest_gap, longest_directed, max(reciprocal)


def spacing_statistics(gaps):
    n = len(gaps)+1
    a = max(gaps)
    b = max(gaps[0], gaps[-1],
            *(min(gaps[i-1],gaps[i]) for i in range(1,n-1)))
    reciprocal = []
    for i,g in enumerate(gaps):
        if (i==0 or g<gaps[i-1]) and (i==len(gaps)-1 or g<gaps[i+1]):
            reciprocal.append(g)
    assert reciprocal
    return a,b,max(reciprocal)


def test():
    counter=0
    for n in range(4,9):
        for gap in itertools.permutations(range(1,n)):
            d = direct_statistics(gap)
            f = spacing_statistics(gap)
            assert d==f,(n,gap,d,f)
            counter+=3
    # Check the single-site rare-event intensities against direct integration.
    import scipy.integrate as si
    for t in [0.,.25,.75,1.5,3.0]:
        qb=math.exp(-2*t)
        qc=math.exp(-3*t)/3
        b_num=si.quad(lambda x: math.exp(-x),t,math.inf)[0]**2
        c_num=si.quad(lambda x: math.exp(-3*x),t,math.inf)[0]
        assert abs(qb-b_num)<1e-11
        assert abs(qc-c_num)<1e-11
        counter+=2
    # Exact structural implications for every overlapping pair type,
    # tested over a bounded lattice of gap inputs (not an infinite proof).
    u1,u2,u3=4,3,2
    for m in (5,6):
        for gaps in itertools.product((1,2,3,4,5),repeat=m):
            A=[g>u1 for g in gaps]
            B=[gaps[i]>u2 and gaps[i+1]>u2 for i in range(m-1)]
            C=[gaps[i]>u3 and gaps[i-1]>gaps[i] and gaps[i+1]>gaps[i]
               for i in range(1,m-1)]
            for i in range(m-1):
                if B[i] and i<m-2 and B[i+1]:
                    assert all(g>u2 for g in gaps[i:i+3])
                counter+=1
            for i in range(1,m-3):
                if C[i-1] and C[i+1]:
                    assert all(g>u3 for g in gaps[i-1:i+4])
                counter+=1
    # Monte Carlo at one finite sample size for the three centered extrema.
    rng=np.random.default_rng(20261119)
    n,rep=8000,2400
    E=rng.exponential(size=(rep,n+1))
    gaps=E[:,1:n]
    S=E.sum(axis=1)
    scale=n/S
    a=gaps.max(axis=1)*scale
    b=np.maximum.reduce([gaps[:,0], gaps[:,-1],
                         np.minimum(gaps[:,:-1],gaps[:,1:]).max(axis=1)])*scale
    internal=(gaps[:,1:-1]<gaps[:,:-2]) & (gaps[:,1:-1]<gaps[:,2:])
    c=np.max(np.where(internal,gaps[:,1:-1],0.0),axis=1)
    c=np.maximum(c,np.where(gaps[:,0]<gaps[:,1],gaps[:,0],0))
    c=np.maximum(c,np.where(gaps[:,-1]<gaps[:,-2],gaps[:,-1],0))*scale
    normalized=np.stack([a-np.log(n-1),
                         2*b-np.log(n-2),
                         3*c-np.log((n-3)/3)],axis=1)
    p=(normalized<=0).mean(axis=0)
    joint=np.all(normalized<=0,axis=1).mean()
    expected=math.exp(-1)
    assert np.max(abs(p-expected))<0.045,(p,expected)
    assert abs(joint-math.exp(-3))<0.03,(joint,math.exp(-3))
    print(f'PASS: {counter-10} finite combinatorial checks and 10 numerical-integral comparisons.')
    print('Finite-n Monte Carlo diagnostic (n=8000, trials=2400):')
    print('  three marginal zero-threshold frequencies:',[round(float(v),4) for v in p])
    print('  joint zero-threshold frequency:',round(float(joint),4))
    print('  limiting comparison:', round(expected,4), round(math.exp(-3),4))
    print('Finite checks and simulation do not certify the infinite limit.')


if __name__=='__main__':
    test()
