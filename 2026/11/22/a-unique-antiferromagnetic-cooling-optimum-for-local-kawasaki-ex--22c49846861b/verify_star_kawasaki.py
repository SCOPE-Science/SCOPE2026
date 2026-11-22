#!/usr/bin/env python3
"""Exact rates and independently assembled full-state spectral checks for star spin exchange."""
import itertools,math
import numpy as np
from scipy.optimize import brentq

def gap_formula(n,k,a):
    c=n-k+1
    if k==1:return a
    if k==n:return 1-a
    s=k*a+c*(1-a)
    return (2*n*a*(1-a))/(s+math.sqrt(max(0,s*s-4*n*a*(1-a))))  # stable rationalization

def gap_full(n,k,a):
    # all configurations indexed by k occupied sites among hub=0 and leaves=1..n
    states=list(itertools.combinations(range(n+1),k))
    idx={s:i for i,s in enumerate(states)}
    Q=np.zeros((len(states),len(states)))
    for i,s in enumerate(states):
        ss=set(s)
        for leaf in range(1,n+1):
            if (0 in ss)!=(leaf in ss):
                nxt=tuple(sorted(ss.symmetric_difference({0,leaf})))
                rate=(1-a) if 0 in ss else a
                j=idx[nxt]
                Q[i,j]+=rate
                Q[i,i]-=rate
    # reversibility weights = constant on each hub class, ratio pi_hub1/pi_hub0=a/(1-a)
    w=np.array([(a/(1-a)) if 0 in s else 1. for s in states]); H=np.sqrt(w[:,None]/w[None,:])*Q
    assert np.max(np.abs(H-H.T))<2e-12,(n,k,a)
    ev=np.linalg.eigvalsh(-H)
    assert abs(ev[0])<1e-9,(n,k,a,ev[0]);return ev[1]

if __name__=='__main__':
    checks=0
    for n in range(3,9):
        for k in range(1,n+1):
            for a in (0.13,0.29,0.5,0.69,0.87):
                pred=gap_formula(n,k,a)
                obs=gap_full(n,k,a)
                assert abs(obs-pred)<1e-9,(n,k,a,pred,obs)
                checks+=1
    for n in range(4,17):
        for k in range(2,n):
            c=n-k+1;d=k-c
            if d==0:
                assert abs(gap_formula(n,k,.5)-.5)<1e-10
                continue
            def derivative(a):
                g=gap_formula(n,k,a)
                return n*(1-2*a)-d*g
            if d>0: opt=brentq(derivative,1e-8,.5)
            else:opt=brentq(derivative,.5,1-1e-8)
            assert gap_formula(n,k,opt)>.5
            assert gap_formula(n,k,opt)>gap_formula(n,k,(opt+.5)/2)
    print('EXACT_RATES_FULL_STATES_OK',checks)
