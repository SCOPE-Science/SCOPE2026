#!/usr/bin/env python3
"""Numerical and symbolic cross-checks for three-site periodic heat-kernel precision transition."""
import mpmath as mp
mp.mp.dps=65

def H(t,x):
    return mp.jtheta(3,x/2,mp.exp(-t))

def excess(t,a):
    return H(t,a)**2-H(t,0)*H(t,2*a)

def root(t):
    lo=mp.pi/2
    hi=mp.acos(-mp.mpf(1)/3)
    for _ in range(240):
        mid=(lo+hi)/2
        if excess(t,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

checks=0
for t in ['0.025','0.1','0.3','1','2','5','9']:
    T=mp.mpf(t)
    a=root(T)
    assert mp.pi/2<a<mp.acos(-mp.mpf(1)/3)
    assert abs(excess(T,a))<mp.mpf('1e-50')*(H(T,0)**2)
    checks+=2
    for f in ['0.65','0.85','1.15','1.35']:
        aa=a*mp.mpf(f)
        if aa>=mp.pi:continue
        K=mp.matrix([[H(T,x-y) for y in [-aa,mp.mpf(0),aa]] for x in [-aa,mp.mpf(0),aa]])
        Q=K**-1
        assert mp.sign(Q[0,2])==mp.sign(excess(T,aa))
        assert mp.sign(Q[0,2])==(1 if aa<a else -1)
        checks+=2
    print('t=',t,'root=',mp.nstr(a,25))
# factor identity, nonzero q sample
for r in [mp.mpf('.01'),mp.mpf('.3'),mp.mpf('.9')]:
    for c in [mp.mpf('-1'),mp.mpf('-1')/3,mp.mpf('0'),mp.mpf('.5'),mp.mpf('1')]:
        B=1+2*r*c+r**2
        A=(1+r)**2
        C=(1-r)**2+4*r*c*c
        assert abs(B*B-A*C-4*r*(1-c)*(c*(1+r+r*r)+r))<mp.mpf('1e-60')
        checks+=1
print('assertions',checks)
print('small_t_limit',mp.nstr(mp.pi*(2-mp.sqrt(2)),25))
