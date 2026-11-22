#!/usr/bin/env python3
"""Numerical diagnostics for oscillatory beta moments and harmonic multiplicities.
Uses only mpmath and standard Python; these finite checks are not proofs.
"""
from math import comb, factorial
import mpmath as mp
mp.mp.dps = 55

def eig(k, d, lam, gam):
    m = mp.mpf(k) + mp.mpf(d)/2
    beta = mp.mpf(lam)-mp.mpf(gam)
    return mp.exp(1j)*mp.gamma(m)*mp.hyperu(m, -beta, -1j)/mp.beta(m, mp.mpf(lam)+1)

def asymp(k, lam, gam):
    k=mp.mpf(k); lam=mp.mpf(lam); gam=mp.mpf(gam)
    beta=lam-gam
    return (mp.sqrt(mp.pi)/mp.gamma(lam+1)*k**((2*lam+2*gam+1)/4)
            *mp.exp(-mp.sqrt(2*k))
            *mp.exp(1j*(mp.sqrt(2*k)+mp.mpf('0.5')-mp.pi*(2*beta+1)/8)))

def cutoff(k, d, lam, gam, eps):
    m=mp.mpf(k)+mp.mpf(d)/2
    beta=mp.mpf(lam)-mp.mpf(gam)
    return mp.quad(lambda t:t**(m-1)*(1-t)**beta*mp.exp(1j/(1-t)),
                   [0,1-mp.mpf(eps)])/mp.beta(m,mp.mpf(lam)+1)

checks=0
for d in [2,3,4,5,7]:
    for k in [1,2,3,8,15,30]:
        h=comb(k+d-1,d-1)-(comb(k+d-3,d-1) if k+d-3>=d-1 else 0)
        assert h>0
        if d==2: assert h==2
        checks+=1
for lam,gam in [('-0.7','0.6'),('-0.5','0.75'),('0.0','0.0'),('0.4','0.75'),('0.8','1.25')]:
    for d in [2,3,5]:
        ratios=[]
        for k in [80,260,800]:
            z=eig(k,d,lam,gam)/asymp(k,lam,gam)
            ratios.append(abs(z-1))
            checks+=1
        assert ratios[-1]<ratios[0] and ratios[-1] < mp.mpf('0.16'),(lam,gam,d,ratios)
for lam,gam in [('-0.5','0.75'),('-0.5','1.0'),('0.2','0.75')]:
    vals=[]
    for eps in ['0.08','0.04','0.02']:
        ep=mp.mpf(eps)
        k=int(mp.nint((mp.mpf(lam)+1)/ep-mp.mpf('1')))
        m=mp.mpf(k)+1
        beta=mp.mpf(lam)-mp.mpf(gam)
        delta=eig(k,2,lam,gam)-cutoff(k,2,lam,gam,eps)
        endpoint=1j*ep**(beta+2)*(1-ep)**(m-1)*mp.exp(1j/ep)/mp.beta(m,mp.mpf(lam)+1)
        assert abs(delta/endpoint-1) < mp.mpf('0.09'),(lam,gam,eps,delta/endpoint)
        vals.append(abs(delta)/ep**(1-mp.mpf(gam)))
        checks+=1
    assert vals[-1]/vals[0] > mp.mpf('.65') and vals[-1]/vals[0] < mp.mpf('1.35')
print('PASS',checks,'finite diagnostics; no claim of infinite certification')
