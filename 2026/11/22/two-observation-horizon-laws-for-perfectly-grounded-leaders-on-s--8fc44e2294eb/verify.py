"""Reproduce the finite-horizon leader-placement theorem on unweighted stars.

Requires Python 3 with NumPy. Exact statements are proved in RESULT.md;
the independent matrix computations here are finite corroboration only.
"""
import math
import numpy as np


def roots(m,k):
    disc=math.sqrt((m+1)**2-4*k)
    return (2*k/(m+1+disc), (m+1+disc)/2)


def spectra(m,k,leader_hub):
    if leader_hub:
        return [1.0]*(m-k+1)
    if k==m:
        return [float(m)]
    lo,hi=roots(m,k)
    return [1.0]*(m-k-1)+[lo,hi]


def matrix_spectrum(m,k,leader_hub):
    L=np.zeros((m+1,m+1),dtype=float)
    for u in range(1,m+1):
        L[0,0]+=1;L[u,u]+=1;L[0,u]-=1;L[u,0]-=1
    S=([0]+list(range(1,k)) if leader_hub else list(range(1,k+1)))
    F=[i for i in range(m+1) if i not in S]
    return np.linalg.eigvalsh(L[np.ix_(F,F)])


def H(sp,t):
    return sum(math.exp(-2*t*x) for x in sp)


def E(sp,t):
    return sum(-math.expm1(-2*t*x)/(2*x) for x in sp)


def delta_H(m,k,t):
    return H(spectra(m,k,False),t)-H(spectra(m,k,True),t)


def delta_E(m,k,t):
    return E(spectra(m,k,False),t)-E(spectra(m,k,True),t)


def bisect(f,lo,hi):
    assert f(lo)<0<f(hi)
    for _ in range(100):
        x=(lo+hi)/2
        if f(x)<0:lo=x
        else:hi=x
    return (lo+hi)/2


count=0
for m in range(2,33):
    for k in range(1,m+1):
        for hub in (True,False):
            a=matrix_spectrum(m,k,hub)
            b=np.array(sorted(spectra(m,k,hub)))
            assert np.allclose(a,b,rtol=1e-10,atol=1e-10), (m,k,hub,a,b)
            count+=1
            for T in (.001,.02,.1,.3,.75,1.5,4.0):
                hn=np.exp(-2*T*a).sum()
                en=np.sum(-np.expm1(-2*T*a)/(2*a))
                assert abs(hn-H(b,T))<1e-9
                assert abs(en-E(b,T))<1e-9
                count+=2
        if k==m:
            for T in (.01,.1,1,10):
                assert delta_H(m,k,T)<0 and delta_E(m,k,T)<0
                count+=2
            continue
        # Check the single instantaneous switch from a strict convex equation.
        lo,hi=roots(m,k)
        alpha=1-lo;beta=hi-1
        assert 0<alpha<beta
        # A small positive endpoint before the switch.
        d=lambda t: math.exp(alpha*2*t)+math.exp(-beta*2*t)-2
        left=1e-5
        assert d(left)<0
        right=1.0
        while d(right)<0:right*=2
        TH=bisect(d,left,right)
        assert delta_H(m,k,TH*.5)<0 and delta_H(m,k,TH*1.5)>0
        count+=3
        if 2*k<m+1:
            de=lambda t:delta_E(m,k,t)
            right=max(TH*2,1.0)
            while de(right)<=0: right*=2
            TE=bisect(de,1e-5,right)
            assert TE>TH
            assert de(TE*.5)<0 and de(TE*1.5)>0
            count+=3
        else:
            assert (m+1)/k-2<=0
            for t in (.01,TH,5*TH,30*TH):
                assert delta_E(m,k,t)<1e-9
                count+=1

# Check the separate all-budget stationary sign, including equality.
for m in range(2,60):
    for k in range(1,m+1):
        leaf=spectra(m,k,False)
        hub=spectra(m,k,True)
        got=sum(1/x for x in leaf)-sum(1/x for x in hub)
        want=(m+1-2*k)/k
        assert abs(got-want)<1e-9
        count+=1
print('VERIFIED',count,'matrix, transient, and stationary comparisons')
