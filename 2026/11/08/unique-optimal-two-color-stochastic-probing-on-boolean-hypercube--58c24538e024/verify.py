#!/usr/bin/env python3
"""Exact standalone checks for hypercube two-color probing claims.
Run: python3 verify.py (standard library only). Analytic proof in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod
from random import Random

checks = 0

def test(condition, label='identity'):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f'{label}, check {checks}')


def parity(n):
    return -1 if n.bit_count() % 2 else 1


def hamming_heat_kernel(d, q):
    # q=exp(-2t) in (0,1]; transition kernel at XOR-displacement z.
    return [prod([((1+q)/2 if not (z>>k)&1 else (1-q)/2)
                     for k in range(d)]) for z in range(1 << d)]


def resolvent_green(d, mu):
    n = 1 << d
    return [sum((Q(parity(z & s), n*(mu+2*s.bit_count())) for s in range(n)), Q())
            for z in range(n)]


def spectra(d, w):
    n = 1 << d
    return [sum((parity(z&s)*w[z] for z in range(n)), Q())
            for s in range(n)]


def variance_direct(d, w, sig):
    n = 1 << d
    return 2*sum((w[x^y] for x in range(n) for y in range(n)
                 if x != y and sig[x] == sig[y]), Q())


def variance_spectrum(d, w, eig, sig):
    n = 1 << d
    # v=N(Lambda_0-2w(0)) + N*sum lambda(S)*hat_sigma(S)^2
    hats = [sum(sig[x]*parity(x&s) for x in range(n)) for s in range(n)]
    return n*(eig[0] - 2*w[0]) + sum((eig[s]*hats[s]*hats[s]/n for s in range(n)), Q())


def run_family(d, g, label):
    n=1<<d
    w=[z*z for z in g]
    eig=spectra(d,w)
    for s in range(n):
        for t in range(n):
            if s.bit_count()==t.bit_count():test(eig[s]==eig[t], label+' layer invariance')
    levels=[eig[(1<<r)-1] for r in range(d+1)]
    for r in range(d):test(levels[r]>levels[r+1]>0, label+' strict Fourier ordering')
    parity_sig=[parity(x) for x in range(n)]
    vmin=n*(levels[0]+levels[d]-2*w[0])
    test(variance_direct(d,w,parity_sig)==vmin, label+' extremal value')
    test(variance_spectrum(d,w,eig,parity_sig)==vmin, label+' Fourier value')
    test(vmin>=0, label+' nonnegative')
    rng=Random(109*d)
    patterns=product((-1,1), repeat=n) if d<=3 else (
        tuple(rng.choice((-1,1)) for _ in range(n)) for __ in range(600))
    equality=set()
    count=0
    for sig in patterns:
        count+=1
        vd=variance_direct(d,w,sig)
        vs=variance_spectrum(d,w,eig,sig)
        test(vd==vs, label+' variance agreement')
        test(vd>=vmin,label+' global min')
        if vd==vmin:
            test(all(sig[x]==sig[0]*parity(x) for x in range(n)),label+' equality rigidity')
            equality.add(sig)
        if d<=3:
            test(vd-vmin >= n*(levels[d-1]-levels[d]) *
                 (1-Q(sum(sig[x]*parity(x) for x in range(n))**2,n*n)),
                 label+' quantitative gap')
    if d<=3:
        test(count==2**n,label+' exhaustive count')
        test(len(equality)==2,label+' exactly two extremizers')
    return w,eig,vmin


def verify():
    for d in (1,2,3,4):
        n=1<<d
        for mu in (Q(1,2),Q(1),Q(2)):
            g=resolvent_green(d,mu)
            # Directly verify (mu I + hypercube Laplacian) times Green = delta.
            for x in range(n):
                for y in range(n):
                    test((mu+d)*g[x^y]-sum(g[(x^(1<<j))^y] for j in range(d)) == int(x==y),
                         'resolvent matrix inverse')
            w, eig, v=run_family(d,g,f'resolvent d={d} mu={mu}')
            if d==3 and mu==1:
                test(g[0]==Q(12,35),'d3 Green diagonal')
                test(g[1]==Q(13,105),'d3 Green distance 1')
                test(g[3]==Q(8,105),'d3 Green distance 2')
                test(g[7]==Q(2,35),'d3 Green distance 3')
                test(v==Q(1024,3675),'d3 optimum exact')
                test(2*n*(eig[0]-w[0])==Q(16,15),'d3 one-probe variance')
                test(v/(2*n*(eig[0]-w[0]))==Q(64,245),'d3 ratio')
    for d in (1,2,3,4):
        qs=[Q(1,2),Q(1,4)]
        weights=[Q(3,5),Q(2,5)]
        hs=[hamming_heat_kernel(d,q) for q in qs]
        g=[sum(weights[j]*hs[j][z] for j in range(2)) for z in range(1<<d)]
        w,eig,v=run_family(d,g,'heat-mixture d='+str(d))
        for r in range(d+1):
            predicted=sum(weights[i]*weights[j] *
                       ((1+qs[i]*qs[j])/2)**(d-r) *
                       ((qs[i]+qs[j])/2)**r
                       for i in range(2) for j in range(2))
            test(eig[(1<<r)-1]==predicted,'heat-product spectral formula')
    # Independent Rademacher-by-color exact distribution check (eight vertices)
    d=3;n=1<<d;g=resolvent_green(d,Q(1));w=[x*x for x in g]
    for sig in ([parity(x) for x in range(n)],
                [1,1,-1,1,1,1,-1,-1]):
        quad=[]
        for z in product((-1,1),repeat=n):
            val=sum((z[x]*g[x^y]*z[y] for x in range(n) for y in range(n)
                     if sig[x]==sig[y]),Q())
            quad.append(val)
        mean=sum(quad,Q())/len(quad)
        var=sum(((x-mean)**2 for x in quad),Q())/len(quad)
        test(mean==n*g[0],'estimator unbiased')
        test(var==variance_direct(d,w,sig),'actual Rademacher variance')
    print(f'VERIFY_OK: {checks} exact rational and exhaustive/sampled assertions; all true')

if __name__=='__main__':verify()
