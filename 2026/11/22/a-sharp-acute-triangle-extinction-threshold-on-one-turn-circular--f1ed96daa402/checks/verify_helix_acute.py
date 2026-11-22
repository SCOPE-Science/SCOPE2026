"""Standalone reproducibility checks for the acute one-turn helix theorem.
Numerics check analytical identities but do not replace the proof.
Run: python checks/verify_helix_acute.py (Python 3.9+; standard library only).
"""
import math
import random

PI = math.pi
T = 2 * PI

def sinc(x):
    return 1.0 if x == 0 else math.sin(x)/x

def g(t):
    return 1/math.tan(t/2)-2/t-math.tan(t)

def root():
    lo, hi = 2.5, 2.8
    assert g(lo) > 0 > g(hi)
    for _ in range(90):
        m = (lo+hi)/2
        if g(m) > 0:
            lo = m
        else:
            hi = m
    return (lo+hi)/2

def R(a,b):
    return -math.cos((a+b)/2)*sinc(a/2)*sinc(b/2)

def dots(a,b,c):
    s=a+b
    first=1-math.cos(a)-math.cos(s)+math.cos(b)+c*c*a*s
    middle=1-math.cos(a)-math.cos(b)+math.cos(s)-c*c*a*b
    last=1-math.cos(b)-math.cos(s)+math.cos(a)+c*c*b*s
    return first,middle,last

def vector(t,c):
    return (math.cos(t), math.sin(t), c*t)

def direct_dots(t1,t2,t3,c):
    u,v,w = (vector(t,c) for t in [t1,t2,t3])
    def diff(p,q):return tuple(x-y for x,y in zip(p,q))
    def dot(x,y):return sum(a*b for a,b in zip(x,y))
    return (dot(diff(v,u),diff(w,u)),
            dot(diff(u,v),diff(w,v)),
            dot(diff(u,w),diff(v,w)))

def coeff(t):
    m=R(t,t)
    h1=.25/(math.sin(t/2)**2)-1/t**2
    h2=h1+.5/(math.cos(t)**2)
    return 3*(PI-t)/(PI**2*m*math.sqrt(h1*h2))

def probability_mid_only(c,n=950):
    # midpoint Riemann quadrature on a triangular domain, using the exact
    # order-statistic density. For c near c* both end angles are positive
    # throughout the surviving region.
    h=T/n
    res=0.0
    for i in range(n):
        a=(i+.5)*h
        for j in range(n-i-1):
            b=(j+.5)*h
            if R(a,b)>c*c:
                x,y,z=dots(a,b,c)
                if x>0 and z>0:
                    res+=(T-a-b)
    return res*h*h*6/(T**3)

def run():
    t=root(); m=R(t,t); pc=math.sqrt(m); C=coeff(t)
    assert 2.6 < t < 2.8 and 0.68 < pc < 0.69
    assert abs(t-2.670778089087041)<2e-13
    assert abs(pc-0.6874374448319006)<2e-13
    assert abs(C-0.9898164405674238)<2e-12
    assert all(q>0 for q in dots(t,t,pc)[::2])
    assert abs(dots(t,t,pc)[1])<1e-12
    # Independent vector-coordinate verification of all three angles.
    rng=random.Random(812411)
    for c in [0, .2, .6, pc, .8, 1.2]:
        for _ in range(10000):
            x,y,z=sorted(rng.random()*T for i in range(3))
            d1=dots(y-x,z-y,c)
            d2=direct_dots(x,y,z,c)
            assert all(abs(a-b)<2e-13 for a,b in zip(d1,d2))
    # A fixed-grid global test is only a check; uniqueness is proved
    # analytically by strict log-sinc concavity and the root derivative.
    for i in range(1,351):
        a=i*T/351
        for j in range(1,351-i):
            b=j*T/351
            assert R(a,b)<=m+5e-13
    # Coefficient of the onset, independently computed with a direct
    # two-dimensional integral of angle signs, including the endpoint tests.
    for eps in [.012, .006]:
        c=math.sqrt(m-eps)
        p=probability_mid_only(c)
        assert abs(p/(eps*C)-1)<.055, (c,p,eps*C)
    print('HELIX_ONE_TURN_ACUTENESS_CHECKS_OK')
    print('t_star={:.15f}; c_star={:.15f}; onset_coefficient={:.15f}'.format(t,pc,C))
if __name__=='__main__':
    run()
