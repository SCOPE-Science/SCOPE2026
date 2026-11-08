#!/usr/bin/env python3
"""Finite spectral check for the explicit fractional Volterra companion.
Requires numpy and scipy (see requirements.txt). A numerical experiment, not an infinite proof.
"""
import numpy as np
from scipy.special import loggamma, gamma

ETA=0.5
EPS=0.15
A=EPS*abs(gamma(1-1j))
PHASE=np.angle(gamma(1-1j))+np.log(2)

def moment(j):
    j=np.asarray(j,dtype=np.float64)
    return 1/(2*j+2)+EPS*np.real(np.exp(loggamma(2*j+2)+loggamma(1-1j)-loggamma(2*j+3-1j)))

def profile(u,angles=3000):
    theta=2*np.pi*(np.arange(angles)+0.5)/angles
    r=np.abs(1+ETA*np.exp(1j*theta))
    x=r/2
    for _ in range(75):
        new=r/2*(1+A*np.cos(u+np.log(x)+PHASE))
        if np.max(abs(new-x))<1e-14:
            x=new
            break
        x=new
    return float(np.mean(x))

def finite_count(N):
    L=2*N
    d=moment(np.arange(L+2))
    diagonal=d[1:L+1]**2+ETA**2*d[2:L+2]**2
    off=ETA*d[2:L+1]**2
    cutoff=1/N**2
    pivot=float(diagonal[0]-cutoff)
    below=int(pivot<0)
    for idx in range(1,L):
        pivot=float(diagonal[idx]-cutoff-off[idx-1]**2/(pivot if abs(pivot)>1e-35 else 1e-35))
        below+=int(pivot<0)
    return L-below

if __name__=='__main__':
    assert 0 < A < 1/np.sqrt(2)
    assert all(moment(np.arange(1,40))>0)
    errors=[]
    for N in (200,500,1000,3000,8000):
        empirical=finite_count(N)/N
        predicted=profile(np.log(N))
        diff=abs(empirical-predicted)
        print(f'N={N:5d}  t*N(t)={empirical:.9f}  Psi={predicted:.9f}  error={diff:.9f}')
        errors.append(diff)
    assert max(errors)<0.012
    values=[profile(2*np.pi*j/160) for j in range(160)]
    angular=np.abs(1+ETA*np.exp(2j*np.pi*(np.arange(5000)+0.5)/5000))
    assert abs(np.mean(values)-np.mean(angular)/2)<2e-6
    assert max(values)-min(values)>0.02
    print('LOG_PERIODIC_VOL_TWOTERM_FINITE_OK',len(errors),'counts; periodic mean and nonconstancy corroborated')
