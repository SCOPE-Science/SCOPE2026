"""Exact Schur identities and finite-network eigenmode checks for the ideal-storage map.
Run: python verify.py. Standard library only.
"""
from fractions import Fraction as Q
from math import cos, pi, exp, log, sqrt
from cmath import sqrt as csqrt

# Characteristic polynomial of every symmetric-averaging eigenmode.
def trace_det(r,d,w):
    a=1-r
    return a+d*w, d*(r+a*w)

def jury(r,d,w):
    t,z=trace_det(r,d,w)
    return 1-t+z, 1+t+z, 1-z

def roots(r,d,w):
    t,z=trace_det(r,d,w)
    D=complex(float(t*t-4*z),0)
    return ((float(t)+csqrt(D))/2,(float(t)-csqrt(D))/2)

checks=0
for ir in range(1,20):
    r=Q(ir,20)
    for idd in range(1,30):
        d=Q(idd,30)
        for iw in range(-20,21):
            w=Q(iw,20)
            j1,j2,j3=jury(r,d,w)
            assert j1==r*(1+d*(1-w))
            assert j2==2-r+d*(r+(2-r)*w)
            assert j3==1-d*(r+(1-r)*w)
            assert j1>0 and j2>0 and j3>0
            checks+=1

# Exact boundary (d=1) gives strict damping on all proper modes.
for ir in range(1,20):
    r=Q(ir,20)
    for iw in range(-20,20):
        j=jury(r,Q(1),Q(iw,20))
        assert min(j)>0
        checks+=1

# Spectral checks on genuine Moore tori: p in [0,1], 3 to 8 cells per axis.
torus_checks=0
for nx in range(3,9):
    for ny in range(3,9):
        for p in (0,.25,.5,1):
            for ix in range(nx):
                for iy in range(ny):
                    # 8 different Moore neighbors on each torus.
                    w=1-p+p/8*((1+2*cos(2*pi*ix/nx))*(1+2*cos(2*pi*iy/ny))-1)
                    assert -1-1e-12<=w<=1+1e-12
                    for r,d in ((.1,.9),(.5,.9),(.9,.9),(.1,.999),(.7,.999)):
                        assert max(abs(q) for q in roots(r,d,w))<1+1e-10
                        torus_checks+=1

# Check two boundary crossings and degenerate tangency in b=5*c coordinates.
for cr in (2.05,2.25,2.5,3,4,7):
    from bisect import bisect_left
    def fun(b): return b/(1+exp(b-cr))-1
    lowa,lowb=1.0,2.0
    higha,highb=2.0,max(6.0,cr+5)
    assert fun(lowa)<0 and fun(lowb)>0 and fun(higha)>0 and fun(highb)<0
    for _ in range(80):
        mid=(lowa+lowb)/2
        if fun(mid)<0:lowa=mid
        else:lowb=mid
    for _ in range(80):
        mid=(higha+highb)/2
        if fun(mid)>0:higha=mid
        else:highb=mid
    assert abs(fun((lowa+lowb)/2))<1e-12
    assert abs(fun((higha+highb)/2))<1e-12
assert abs(2/(1+exp(2-2))-1)<1e-12
print(f'VERIFY_OK exact_jury_samples={checks} torus_eigenmodes={torus_checks} phase_cases=7')
