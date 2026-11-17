#!/usr/bin/env python3
"""Independent numerical diagnostics for antipodal pair tails on the sphere."""
from math import acos, cos, pi, sin, sqrt, comb
import numpy as np
from scipy.integrate import quad


def lens(r):
    if r >= 2: return 0.0
    return 2*acos(r/2)-r*sqrt(max(0.,4-r*r))/2

I=quad(lambda r:2*pi*r*lens(r)**2,0,2,epsabs=2e-12)[0]
C=1-16/(3*pi*pi)
assert abs(I-(pi**3-16*pi/3))<1e-10

def approx(n,d):
    p=(1-cos(d))/2; m=comb(n,2)
    return m*p-comb(m,2)*p**2+(comb(m,3)-comb(n,3)-3*comb(n,4)*C)*p**3

def cap(rng,center_sign,angle,size):
    # cap centered on north/south pole; center_sign in {+1,-1}
    z=center_sign*(1-rng.random(size)*(1-cos(angle)))
    phi=rng.uniform(0.,2*pi,size)
    xy=np.sqrt(1-z*z)
    return np.column_stack((xy*np.cos(phi),xy*np.sin(phi),z))

def cond_cycle(d, count, seed):
    rng=np.random.default_rng(seed); total=0
    for start in range(0,count,100000):
        k=min(100000,count-start)
        a=np.array([0.,0.,1.]);b=cap(rng,1.,2*d,k)
        c=cap(rng,-1.,d,k); e=cap(rng,-1.,d,k)
        ok=(np.einsum('ij,ij->i',b,c)<-cos(d))&(np.einsum('ij,ij->i',b,e)<-cos(d))
        total+=int(ok.sum())
    p=(1-cos(d))/2; p2=(1-cos(2*d))/2
    q_over_p3=p2*total/count/p
    return q_over_p3,total/count

def diam_mc(n,d,count,seed):
    rng=np.random.default_rng(seed);total=0
    for start in range(0,count,100000):
        k=min(100000,count-start)
        v=rng.standard_normal((k,n,3));v/=np.linalg.norm(v,axis=2,keepdims=True)
        dots=np.einsum('kic,kjc->kij',v,v)
        good=np.any(np.triu(dots < -cos(d),1),axis=(1,2))
        total+=int(good.sum())
    return total/count

print('Analytic lens constant:',repr(C),'numerical integral:',repr(I/pi**3))
for delta in (.16,.25,.38):
    q,pcond=cond_cycle(delta,800000,10000+int(delta*10000))
    # Conditional Monte Carlo uncertainty based on binomial count
    se=((1-cos(2*delta))/2)/((1-cos(delta))/2)*sqrt(pcond*(1-pcond)/800000)
    print('C4 delta',delta,'ratio q/p^3',round(q,6),'statistical_se',round(se,6))
for n,delta in [(4,.25),(5,.22),(7,.14)]:
    observed=diam_mc(n,delta,700000,n*1000+int(delta*1000))
    theory=approx(n,delta)
    print('Diameter n',n,'delta',delta,'observed',round(observed,7),'cubic',round(theory,7),'absolute_error',round(abs(observed-theory),7))
    assert abs(observed-theory)<.004
print('ANTIPODAL_CYCLE_SMALL_CAP_DIAGNOSTIC_OK')
