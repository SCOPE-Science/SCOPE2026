"""Deterministic quadrature checks for point-anchored random torus sections.
No numerical quadrature is used to prove the limiting formulae.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gamma


def nodes(N, lo, hi):
    x,w=leggauss(N)
    return lo+(hi-lo)*(x+1)/2, w*(hi-lo)/2


def arccdf(x):
    return .5 + np.arcsin(np.clip(x,-1,1))/np.pi


def probs(r, nb=120, nr=26, nt=60):
    bet,wb=nodes(nb,0,np.pi/2)
    rad2,wr=nodes(nr,0,1)
    theta,wt=nodes(nt,0,2*np.pi)
    h=np.sqrt(rad2)[:,None]*np.cos(theta)[None,:]
    v=np.sqrt(rad2)[:,None]*np.sin(theta)[None,:]
    volumeweight=(1+h/r)*wr[:,None]*wt[None,:]/(2*np.pi)
    out=0.
    for beta,ww in zip(bet,wb):
        s=np.sin(beta); q=np.cos(beta); c=r*s
        a=(r+h)*s; b=v*q
        L=abs(c-1); U=c+1
        d=arccdf((U-b)/a)-arccdf((L-b)/a)+arccdf((-L-b)/a)-arccdf((-U-b)/a)
        out+=ww*s*np.sum(volumeweight*d)
    # annulus using narrow-angle scale; the exact formula holds at all r>1.
    ts,ww=nodes(nb,0,1)
    ann=0.
    for t,weight in zip(ts,ww):
        s=t/r; q=np.sqrt(1-s*s)
        a=(r+h)*s; b=v*q
        target=1-t
        sub=arccdf((target-b)/a)-arccdf((-target-b)/a)
        ann+=weight*t/(r*r*q)*np.sum(volumeweight*sub)
    return float(out),float(ann)

J=np.sqrt(np.pi)*gamma(.75)/(2*gamma(1.25))
Cdisk=128/(15*np.pi**2)*J
Cann=16/(9*np.pi**2)

if __name__=='__main__':
    # Independent angular-grid geometry checks at non-tangential parameters.
    rng=np.random.default_rng(314159)
    ph=(np.arange(20000)+.5)*(2*np.pi/20000)
    for _ in range(130):
        R=rng.uniform(1.15,24.)
        beta=rng.uniform(.01,np.pi/2-.01)
        s=np.sin(beta); q=np.cos(beta); c=R*s
        angle=rng.uniform(0,2*np.pi); rad=np.sqrt(rng.random())
        h=rad*np.cos(angle); v=rad*np.sin(angle)
        aa=(R+h)*s; bb=v*q
        L=abs(c-1); U=c+1
        m=aa*np.cos(ph)+bb
        geom=np.mean((np.abs(m)>L)&(np.abs(m)<U))
        exact=(arccdf((U-bb)/aa)-arccdf((L-bb)/aa)
               +arccdf((-L-bb)/aa)-arccdf((-U-bb)/aa))
        assert abs(geom-exact)<0.00015, (geom,exact)
        if c<1:
            geomann=np.mean(np.abs(m)<1-c)
            exactann=arccdf((1-c-bb)/aa)-arccdf((-1+c-bb)/aa)
            assert abs(geomann-exactann)<0.00015
    print('Geometry checks: 130 angular CDF comparisons passed')
    assert abs(Cdisk-1.0359209536249056)<1e-14
    assert abs(Cann-0.18012654869748937)<1e-14
    print('Analytic constants:',Cdisk,Cann)
    olddisk=100.; oldann=100.
    for r in [5.,20.,80.,320.]:
        p,a=probs(r)
        assert abs(p*np.sqrt(r)-Cdisk)<olddisk
        assert abs(a*r*r-Cann)<oldann
        olddisk=abs(p*np.sqrt(r)-Cdisk); oldann=abs(a*r*r-Cann)
        print(f'r={r:g} Pdisk={p:.11f} sqrt(r)*Pdisk={p*np.sqrt(r):.9f} '
              f'Pannulus={a:.11f} r^2*Pannulus={a*r*r:.9f}')
