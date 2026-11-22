#!/usr/bin/env python3
"""Reproducibility checks for a three-node Gaussian-kernel weight phase diagram.
Python 3 standard library only. All computational checks are finite illustrations;
the analytic monotonicity argument is needed for the universal theorem.
"""
import math
import random


def target(ell, components):
    # components are (mixing_probability, Gaussian standard deviation)
    c = [(p * ell / math.hypot(ell, sd), ell**2 / (ell**2 + sd**2)) for p, sd in components]
    mass = sum(w for w, b in c)
    return mass, [(w/mass, b) for w, b in c]


def h(q, law):
    return 2 * sum(p * q**(1+b) for p,b in law) - 1 - q**4


def hp(q, law):
    return 2 * sum(p*(1+b)*q**b for p,b in law) - 4*q**3


def q_peak(law):
    lo,hi = 0.,1.
    for _ in range(85):
        mid=(lo+hi)/2
        if hp(mid,law)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def weights(ell, a, eta, components):
    m0, law=target(ell, components)
    q=math.exp(-a*a/(2*ell*ell))
    m_a=m0*sum(p*q**b for p,b in law)
    den=(1+eta+q**4)*(1+eta)-2*q**2
    outer=((1+eta)*m_a-q*m0)/den
    middle=((1+eta+q**4)*m0-2*q*m_a)/den
    return (outer,middle,outer)


def solve3(mat, rhs):
    a=[list(row)+[val] for row,val in zip(mat,rhs)]
    for col in range(3):
        ix=max(range(col,3),key=lambda j:abs(a[j][col]))
        a[col],a[ix]=a[ix],a[col]
        z=a[col][col]
        assert abs(z)>1e-12
        for j in range(col,4): a[col][j]/=z
        for i in range(3):
            if i!=col:
                m=a[i][col]
                for j in range(col,4): a[i][j]-=m*a[col][j]
    return [a[i][3] for i in range(3)]

rng=random.Random(13274)
checks=0
for _ in range(6000):
    ell=math.exp(rng.uniform(-1.5,1.5))
    k=rng.randint(1,6)
    scales=[math.exp(rng.uniform(-2.5,2.5))*ell for _ in range(k)]
    probs=[rng.random()+.01 for _ in range(k)]
    norm=sum(probs); components=[(p/norm,s) for p,s in zip(probs,scales)]
    a=ell*math.exp(rng.uniform(-2.4,1.2))
    eta=math.exp(rng.uniform(-6,1))
    m0,law=target(ell,components)
    q=math.exp(-a*a/(2*ell*ell))
    ma=m0*sum(p*q**b for p,b in law)
    direct=solve3([[1+eta,q,q**4],[q,1+eta,q],[q**4,q,1+eta]], [ma,m0,ma])
    formula=weights(ell,a,eta,components)
    for x,y in zip(direct,formula):
        assert abs(x-y)<3e-8*(1+abs(x)+abs(y)),(direct,formula)
    assert formula[0]>0 and formula[2]>0
    assert (formula[1]<0)==(h(q,law)>eta)
    checks+=1

bound=3*2**(-4/3)-1
for _ in range(1200):
    k=rng.randint(1,7)
    scales=[math.exp(rng.uniform(-4,5)) for i in range(k)]
    probs=[rng.random()+.001 for i in range(k)]
    norm=sum(probs)
    m0,law=target(1,[(p/norm,s) for p,s in zip(probs,scales)])
    q0=q_peak(law)
    hm=h(q0,law)
    assert 0<hm<bound
    for mult in [.1,.3,.6,1.,1.2]:
        q=min(.999999,max(.000001,q0*mult))
        assert h(q,law)<=hm+1e-11
    for eta in [0.,.2*hm,.8*hm,1.1*hm]:
        # Along each branch h must be monotone, so at most two roots.
        left=[h(q0*i/40,law)-eta for i in range(1,40)]
        right=[h(q0+(1-q0)*i/40,law)-eta for i in range(1,40)]
        assert all(left[i] <= left[i+1]+1e-13 for i in range(38))
        assert all(right[i] >= right[i+1]-1e-13 for i in range(38))
    checks+=1

for sd in [10,100,1000]:
    _,law=target(1,[(1,sd)])
    assert abs(h(q_peak(law),law)-bound)<3/sd**2
    checks+=1

print('PASS',checks,'finite direct solves/phase checks; universal bound',format(bound,'.15g'))
