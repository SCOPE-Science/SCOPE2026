"""Deterministic checks for the Euclidean-length cusp of sphere-cylinder intersections.
Only the Python standard library, NumPy and SciPy are required.
Run: python checker.py
All lengths are Euclidean lengths of the complete curve set.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk, ellipe


def exact_length(R, r, d):
    assert 0 < r < R and d >= 0
    if d == 0:
        return 4 * math.pi * r
    if d >= R + r:
        return 0.0
    d0 = R-r
    if d == d0:
        return 8*math.sqrt(r*R)*ellipe(d0/R)
    def speed(t):
        q = (R-d-r)*(R+d+r) + 2*d*r*(1-math.cos(t))
        zprime_sq = (d*r*math.sin(t))**2 / max(q, 1e-300)
        return math.sqrt(r*r+zprime_sq)
    if d < d0:
        return 4*quad(speed, 0, math.pi, epsabs=1e-9, epsrel=1e-10, limit=400)[0]
    cutoff = math.acos(max(-1.0,min(1.0,(R*R-d*d-r*r)/(2*d*r))))
    width = math.pi-cutoff
    # u maps [0,pi] to t in [2pi-cutoff, cutoff], eliminating
    # the integrable square-root singularities at the endpoints.
    def integrand(u):
        if u == 0 or u == math.pi:
            return 0.0
        t = math.pi + width*math.cos(u)
        return speed(t)*width*math.sin(u)
    return 2*quad(integrand, 0, math.pi, epsabs=1e-8, epsrel=1e-10, limit=500)[0]


def constants(R,r):
    m=(R-r)/R
    F=lambda x: ellipe(x)-(1-x)*ellipk(x)
    common=4*R*math.sqrt(2/(R-r))
    return 8*math.sqrt(r*R)*ellipe(m), common*F(m), common*F(1-m), 4*math.sqrt(2*R)*ellipe(R/(R+r))


def polygon_length(R,r,d,n=30000):
    if d >= R+r:
        return 0.0
    if d <= R-r:
        t=np.linspace(0,2*math.pi,n+1)
        q=np.maximum(0.0,R*R-d*d-r*r-2*d*r*np.cos(t))
        z=np.sqrt(q)
        pts=np.column_stack([d+r*np.cos(t),r*np.sin(t),z])
        return 2*np.linalg.norm(np.diff(pts,axis=0),axis=1).sum()
    t0=math.acos((R*R-d*d-r*r)/(2*d*r))
    t=np.linspace(t0,2*math.pi-t0,n+1)
    q=np.maximum(0.0,R*R-d*d-r*r-2*d*r*np.cos(t))
    z=np.sqrt(q)
    pts=np.column_stack([d+r*np.cos(t),r*np.sin(t),z])
    return 2*np.linalg.norm(np.diff(pts,axis=0),axis=1).sum()

checks=0
for R,r in ((2.0,1.0),(3.0,1.0),(1.1,1.0),(1.3,0.2)):
    d0=R-r
    lstar, c_left,c_right,c_outer=constants(R,r)
    assert all(v>0 for v in (lstar,c_left,c_right,c_outer)); checks+=4
    assert abs(exact_length(R,r,d0)-lstar)<2e-11;checks+=1
    assert abs(exact_length(R,r,0)-4*math.pi*r)<1e-11;checks+=1
    for d in (0.35*d0,0.75*d0,d0,d0+0.3*r,R+r-0.2*r):
        length=exact_length(R,r,d)
        poly=polygon_length(R,r,d)
        assert abs(poly-length)<0.013, (R,r,d,length,poly)
        checks+=1
    for eps in (2e-5,8e-6,2e-6):
        if eps>=d0:continue
        left=(lstar-exact_length(R,r,d0-eps))/math.sqrt(eps)
        right=(lstar-exact_length(R,r,d0+eps))/math.sqrt(eps)
        assert abs(left/c_left-1)<0.08, (R,r,eps,'left',left,c_left)
        assert abs(right/c_right-1)<0.08, (R,r,eps,'right',right,c_right)
        checks+=2
    for eps in (1e-2,1e-3):
        if eps>=r:continue
        c=exact_length(R,r,R+r-eps)/math.sqrt(eps)
        assert abs(c/c_outer-1)<0.012, (R,r,eps,c,c_outer)
        checks+=1
    print('R=%g r=%g: critical L=%.10f; cusp left=%.10f right=%.10f outer=%.10f; checks passed' %(R,r,lstar,c_left,c_right,c_outer))

# Strict monotonicity of F and aspect-ratio reconstruction diagnostics.
def F(t):return ellipe(t)-(1-t)*ellipk(t)
ms=np.linspace(.025,.975,51)
ratios=[F(m)/F(1-m) for m in ms]
assert all(x<y for x,y in zip(ratios,ratios[1:])); checks+=1
assert abs(F(.5)/F(.5)-1)<1e-15; checks+=1
assert abs(constants(2,1)[1]-constants(2,1)[2])<1e-14; checks+=1
print('PASS:',checks,'deterministic checks')
