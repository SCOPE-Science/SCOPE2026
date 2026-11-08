"""Direct numerical evaluation of subcube heat-sampling rank and face singular values.
Only finite-dimensional checks; the accompanying mathematical proof covers all d.
"""
from itertools import combinations
from math import comb, exp, log
import numpy as np

def popcount(x): return x.bit_count()

def analytical_rank(d,c,K,m):
    return sum(comb(d-c,k)*min(m, 1+min(c,K-k)) for k in range(min(K,d-c)+1))

def matrix(d,c,K,times):
    n=1<<d
    # Take the face with the first c bits fixed to zero.
    face=[x for x in range(n) if x & ((1<<c)-1)==0]
    modes=[s for s in range(n) if popcount(s)<=K]
    a=np.empty((len(face)*len(times),len(modes)))
    for j,t in enumerate(times):
        for i,x in enumerate(face):
            for l,s in enumerate(modes):
                a[j*len(face)+i,l] = (-1 if popcount(s&x)%2 else 1)*2**(-d/2)*exp(-2*popcount(s)*t/d)
    return a

count=0
for d in range(2,7):
    for c in range(d+1):
        for K in range(d+1):
            for m in range(1,min(4,d+2)):
                a=matrix(d,c,K,[0.4*j for j in range(m)])
                rank=np.linalg.matrix_rank(a,tol=1.e-9)
                expected=analytical_rank(d,c,K,m)
                assert rank==expected,(d,c,K,m,rank,expected)
                count+=1

for d in range(2,8):
    tau=.83
    r=exp(-2*tau/d)
    a=matrix(d,1,d,[0,tau])
    measured=np.linalg.eigvalsh(a.T@a)
    expected=[]
    for k in range(d):
        T=2+r**(2*k)*(1+r*r)
        disc=max(0,T*T-4*r**(2*k)*(1-r)**2)
        expected += [(T-np.sqrt(disc))/4]*comb(d-1,k)
        expected += [(T+np.sqrt(disc))/4]*comb(d-1,k)
    assert np.allclose(np.sort(measured),np.sort(expected),atol=2e-12,rtol=2e-10),(d,np.max(abs(np.sort(measured)-np.sort(expected))))
    tstar=d/2*log((d+1)/(d-1))
    def log_det(t):
        rr=exp(-2*t/d)
        return 2**(d-1)*log((1-rr)/2) + (d-1)*2**(d-2)*log(rr)
    assert log_det(tstar)>log_det(tstar*.85)
    assert log_det(tstar)>log_det(tstar*1.15)
    got=np.linalg.slogdet(matrix(d,1,d,[0,tstar]))
    assert got[0]!=0 and abs(got[1]-log_det(tstar))<2e-8,(d,got,log_det(tstar))
print('CHECK_OK rank_cases=',count,' two_time_spectrum_dimensions=6')
