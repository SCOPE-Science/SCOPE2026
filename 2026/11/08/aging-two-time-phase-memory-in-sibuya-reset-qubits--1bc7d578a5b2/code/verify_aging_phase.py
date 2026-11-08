#!/usr/bin/env python3
"""Reproduce finite-time identities for Sibuya-reset phase memory.
SciPy and NumPy are used only for numerical evaluations, not for infinite-time proof.
"""
import math
import cmath
import json
import argparse
import numpy as np
from scipy.special import betainc

def seq(g, n):
    U = np.empty(n+1); S = np.empty(n+1); p = np.zeros(n+1)
    U[0]=S[0]=1.0
    for i in range(1,n+1):
        U[i]=U[i-1]*(i-1+g)/i
        S[i]=S[i-1]*(i-g)/i
        p[i]=S[i-1]*g/i
    return U,S,p

def exact(t,k,g,z):
    U,S,p=seq(g,t+k)
    m=np.array([sum(U[s-a]*S[a]*z**a for a in range(s+1)) for s in range(k+1)],complex)
    H=sum(U[t-a]*S[a+k] for a in range(t+1))
    R=sum(U[t-a]*z**(-a)*sum(p[a+j]*m[k-j] for j in range(1,k+1)) for a in range(t+1))
    return z**k*H+R,H,R

def direct(t,k,g,z):
    # independent construction of the joint law using an age Markov chain
    U,S,p=seq(g,t+k)
    at=np.array([U[t-a]*S[a] for a in range(t+1)])
    Q=0j
    for a,prob in enumerate(at):
        ages=np.zeros(t+k+1);ages[a]=1.
        for j in range(k):
            new=np.zeros_like(ages)
            for b in range(t+j+1):
                if ages[b]==0:continue
                hz=g/(b+1)
                new[0]+=ages[b]*hz
                new[b+1]+=ages[b]*(1-hz)
            ages=new
        Q+=prob*sum(z**(b-a)*ages[b] for b in range(t+k+1))
    return Q

def H(t,k,g):
    U,S,_=seq(g,t+k)
    return float(np.dot(U[:t+1],S[k:k+t+1][::-1]))

def profile(g,u):
    return float(betainc(g,1-g,1/(1+u)))

def run():
    N=0
    for g in (.2,.5,.8):
        for z in (-1,complex(.6,.8),cmath.exp(1j*.77)):
            for t in (0,1,2,5,8):
                for k in (0,1,3,5):
                    C,h,R=exact(t,k,g,z)
                    ref=direct(t,k,g,z)
                    assert abs(C-ref)<2.e-12,(g,z,t,k,C,ref)
                    assert abs(h.imag if isinstance(h,complex) else 0)<1.e-12
                    assert 0<=h<=1+2.e-12
                    N+=3
    # exact Sibuya mass, renewal and stationary age distributions (separate computation)
    for g in (.2,.5,.8):
        U,S,p=seq(g,100)
        for t in range(1,100):
            assert abs(sum(U[t-a]*S[a] for a in range(t+1))-1)<2.e-12
            assert abs(sum(p[1:t+1])+S[t]-1)<2.e-12
            N+=2
    # limiting persistence at macroscopic times, and fixed-lag persistence
    for g in (.25,.5,.75):
        for u in (.5,1,2):
            h=H(4000,round(4000*u),g)
            assert abs(h-profile(g,u))<.012,(g,u,h,profile(g,u))
            N+=1
    for g in (.25,.5,.75):
        h=H(4000,4,g)
        assert h>.80,(g,h)
        N+=1
    assert abs(profile(.5,1)-.5)<1.e-14
    N+=1
    print(json.dumps({'status':'passed','finite_assertions':N,'profile_half_at_equal_ages':profile(.5,1),
                      'sample_persistence_g05_t4000_k4000':H(4000,4000,.5)},sort_keys=True))

if __name__=='__main__':
    run()
