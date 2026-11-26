#!/usr/bin/env python3
"""Finite numerical checks of the Möbius-ladder price-frontier theorem."""
import numpy as np

def constants(n):
    theta=np.pi/n
    p=2-2*np.cos(theta)
    q=2-2*np.cos(2*theta)
    return p,q,4/p

def laplacian(n,rim,rung):
    assert len(rim)==2*n and len(rung)==n
    L=np.zeros((2*n,2*n),float)
    for j,w in enumerate(rim):
        k=(j+1)%(2*n)
        L[j,j]+=w; L[k,k]+=w; L[j,k]-=w; L[k,j]-=w
    for j,a in enumerate(rung):
        k=j+n
        L[j,j]+=a; L[k,k]+=a; L[j,k]-=a; L[k,j]-=a
    return L

def exact_opt(n,t):
    p,q,tc=constants(n)
    if t<tc:
        b=2/(n*(4+t*(q-p)))
        a=(q-p)/(n*(4+t*(q-p)))
        gap=2*q/(n*(4+t*(q-p)))
    else:
        a=0.0; b=1/(2*n); gap=p/(2*n)
    return b,a,gap

def run():
    rng=np.random.default_rng(36047)
    counts=dict(optimal_spectra=0, spectral_certificates=0, random_comparisons=0, critical_family=0)
    for n in range(3,13):
        p,q,tc=constants(n)
        for t in [0.03,0.1,0.7,1,2,tc/2,tc,2*tc,1000]:
            b,a,gap=exact_opt(n,t)
            L=laplacian(n,[b]*(2*n),[a]*n)
            lam=np.linalg.eigvalsh(L)[1]
            assert abs((2*n*b+n*t*a)-1)<3e-13
            assert abs(lam-gap)<3e-12,(n,t,lam,gap)
            counts['optimal_spectra']+=1
            for _ in range(30):
                raw=rng.uniform(0,1,size=3*n)
                w=raw/(raw[:2*n].sum()+t*raw[2*n:].sum())
                B=w[:2*n].sum(); A=w[2*n:].sum()
                U=min(q*B/(2*n),(p*B+4*A)/(2*n))
                actual=np.linalg.eigvalsh(laplacian(n,w[:2*n],w[2*n:]))[1]
                assert actual<=U+3e-12,(n,t,actual,U)
                assert U<=gap+3e-12,(n,t,U,gap)
                counts['random_comparisons']+=1
                counts['spectral_certificates']+=2
        for s in np.linspace(0,1,7):
            # at the critical price: symmetric family from pure cycle to balancing
            B=(p/q)*(1-s)+s
            b=B/(2*n)
            a=(1-B)/(n*tc)
            L=laplacian(n,[b]*(2*n),[a]*n)
            assert abs(np.linalg.eigvalsh(L)[1]-p/(2*n))<3e-12
            counts['critical_family']+=1
    print('VERIFY_OK',counts)
if __name__=='__main__':run()
