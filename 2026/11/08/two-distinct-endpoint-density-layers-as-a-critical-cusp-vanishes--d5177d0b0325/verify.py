"""Reproducible algebraic and finite-grid checks for a vanishing critical cusp."""
import math
import numpy as np

checks=0
for theta in [1.25,1.6,1.9,1.98]:
    K=(2-theta)/(2*math.sqrt(2))
    lam=1/(1+theta/2)
    for x in [i/100 for i in range(101)]:
        u=(math.sqrt(K*K+theta*(1-x))-K)/theta
        g0=.5-u*u; g1=.5+u*u
        w=u/(K+theta*u) if u>0 else 0.
        if x <1:
            assert abs(w-(1-K/math.sqrt(K*K+theta*(1-x)))/theta)<3e-13
        for g in [g0,g1]:
            v=1-theta*abs(g-.5)-2*K*math.sqrt(abs(g-.5))
            assert abs(v-x)<1e-11,(theta,x,g,v)
            checks+=1
    assert abs(lam-(1/(theta+K*math.sqrt(2))))<3e-14

def G(s): return 1-1/math.sqrt(1+s)
def H(s): return sum(2**(-j)*G(s/(2**j)) for j in range(1,95))
for s in [0,.02,.1,1,2,10,100]:
    assert abs(H(s)-.5*(H(s/2)+G(s/2)))<1e-15
    for theta in [1.9,1.99,1.99999]:
        K=(2-theta)/(2*math.sqrt(2))
        lam=1/(1+theta/2)
        x=K*K*s/theta
        u=(math.sqrt(K*K+theta*(1-x))-K)/theta
        t=theta*(.5-u*u)/(K*K)
        if theta>1.9999:
            assert abs(t-s/2)<1e-4*(1+s)
        if s and theta>1.9999:
            assert abs(t-s/2)<1e-4*(1+s)
        wr=(1/theta)*(1-1/math.sqrt(1+s))
        assert abs(theta*wr-G(s))<1e-14
        checks+=1
assert abs(sum(2**(-2*j-1) for j in range(1,95))-1/6)<1e-15

# Approximate transfer fixed points on a fine grid; these are illustrative, not a proof.
for theta in [1.9,1.98]:
    K=(2-theta)/(2*math.sqrt(2)); n=240001
    grid=np.linspace(0,1,n)
    u=(np.sqrt(K*K+theta*(1-grid))-K)/theta
    g0=.5-u*u;g1=.5+u*u
    w=(1/theta)*(1-K/np.sqrt(K*K+theta*(1-grid)))
    h=np.ones(n)
    for it in range(250):
        hn=w*(np.interp(g0,grid,h)+np.interp(g1,grid,h))
        hn/=np.trapezoid(hn,grid)
        change=np.max(abs(hn-h))
        h=hn
        if change<1e-12: break
    assert change<2e-11,(theta,it,change)
    assert abs(h[0])<1e-10 and abs(h[-1])<1e-10,(theta,h[0],h[-1])
    assert abs(h[n//2]-1)<.15
    scales=[.2,1,4,10]
    errs=[]
    for s in scales:
        a=K*K*s/theta
        left=np.interp(a,grid,h)
        right=np.interp(1-a,grid,h)
        errs.append((abs(left-H(s)),abs(right-G(s))))
        assert abs(right-G(s))<.08,(theta,s,right,G(s))
        assert abs(left-H(s))<.08,(theta,s,left,H(s))
        checks+=2
    print('GRID', theta, 'iterations',it+1,'L1',np.trapezoid(abs(h-1),grid), 'max_err',max(map(max,errs)))

print('VERIFY_OK', 'algebra_and_series_checks=',checks,'grid_thetas=2')
