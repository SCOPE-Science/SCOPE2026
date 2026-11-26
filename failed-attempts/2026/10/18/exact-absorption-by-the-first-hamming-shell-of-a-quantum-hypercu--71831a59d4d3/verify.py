"""Finite-dimensional reproducibility checks for the absorbing-shell hypercube theorem."""
import math
import numpy as np
from scipy.linalg import expm


def kraw(d, k, s):
    return sum((-1)**j * math.comb(s, j)*math.comb(d-s,k-j)
               for j in range(max(0,k-d+s), min(k,s)+1))


def formula(d,s):
    t = (d if 0 < s < d else 1)/math.comb(d,s)
    if d%2==0:
        t -= kraw(d,d//2,s)**2/(2**d*math.comb(d,d//2))
    return t


def spectral_bright(d):
    n=1<<d
    walsh=np.empty((n,n))
    for z in range(n):
        for x in range(n):
            walsh[z,x]=(-1)**((z&x).bit_count())/math.sqrt(n)
    bright=np.zeros((n,n))
    total_rank=0
    for k in range(d+1):
        f=walsh[[z for z in range(n) if z.bit_count()==k],:]
        sampled=f[:,[1<<i for i in range(d)]]
        u,s,_=np.linalg.svd(sampled,full_matrices=False)
        rank=int(np.sum(s>1e-10))
        total_rank+=rank
        bright+=(f.T@u[:,:rank])@(f.T@u[:,:rank]).T
    return bright,total_rank


checks=0
worst=0.0
for d in range(2,9):
    p,r=spectral_bright(d)
    assert r==d*d-d+2-int(d%2==0),(d,r)
    checks+=1
    for x in range(1<<d):
        err=abs(p[x,x]-formula(d,x.bit_count()))
        worst=max(worst,err)
        assert err<1e-11,(d,x,err)
        checks+=1
    assert abs(np.trace(p)-r)<1e-9
    assert np.max(abs(p@p-p))<1e-9
    checks+=2
    if d<=4:
        n=1<<d
        ham=np.zeros((n,n),complex)
        for x in range(n):
            for i in range(d):
                ham[x,x^(1<<i)]=1.0
        rates=np.array([0.6+0.11*i for i in range(d)])
        generator=ham-0.5j*sum(rates[i]*np.diag(np.eye(n)[1<<i]) for i in range(d))
        evolution=expm(-1j*generator*300)
        svals=np.sum(abs(evolution)**2,axis=0)
        for x in range(n):
            err=abs((1-svals[x])-formula(d,x.bit_count()))
            worst=max(worst,err)
            assert err<1e-7,('finite-time check',d,x,err)
            checks+=1
    print('dimension',d,'bright',r,'dark',(1<<d)-r)
print('checks',checks,'maximum absolute discrepancy',worst)
