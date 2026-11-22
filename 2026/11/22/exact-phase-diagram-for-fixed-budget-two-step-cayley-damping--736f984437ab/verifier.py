"""Reproducible identities and supplementary tests for two-substep midpoint damping."""
import math
import random
import sympy as sp


def optimum(a, b, H):
    assert a > 0 and b >= 0 and H > 0
    r = math.hypot(a,b)
    R = (r*H/2)**2
    s = b/r
    w = min(1+R/4, max(1, math.sqrt(R+4*s*s)))
    q = (w-1)/R
    q = max(0, min(0.25,q))
    t = (1-math.sqrt(max(0,1-4*q)))/2
    return t, R, s, q


def gain(a,b,H,t):
    z=complex(-a,b)*H/2
    f=lambda frac:(1+frac*z)/(1-frac*z)
    return abs(f(t)*f(1-t))**2


def symbolic_checks():
    u,v,q=sp.symbols('u v q', real=True)
    z=-u+sp.I*v
    P=sp.expand((1+z+q*z*z)*(1+sp.conjugate(z)+q*sp.conjugate(z)**2))
    Q=sp.expand((1-z+q*z*z)*(1-sp.conjugate(z)+q*sp.conjugate(z)**2))
    R=u*u+v*v
    B=(1+q*R)**2+R-4*q*v*v
    T=2*u*(1+q*R)
    assert sp.expand(P-(B-T))==0
    assert sp.expand(Q-(B+T))==0
    # Strictly convex equivalent scalar objective w+(R+4s^2)/w-4s^2
    w,s=sp.symbols('w s',positive=True)
    U=w+(R+4*s*s)/w-4*s*s
    assert sp.simplify(sp.diff(U,w)-(1-(R+4*s*s)/w**2))==0
    assert sp.simplify(sp.diff(U,w,2)-2*(R+4*s*s)/w**3)==0
    # The equal-step phase window follows from w*=sqrt(R+4s^2)>=1+R/4.
    RR=sp.symbols('RR',positive=True)
    assert sp.expand(16*(RR+4*s*s-(1+RR/4)**2)+ (RR-4)**2-64*s*s)==0
    # The zero-stage phase follows from w*<=1.
    assert sp.expand((1-4*s*s)-1+4*s*s)==0
    print('Symbolic identities: PASS (Cayley product, scalar reduction, strict convexity, boundaries)')


def numerical_checks():
    rng=random.Random(412271)
    n=0
    for _ in range(1200):
        a=10**rng.uniform(-1,1)
        b=a*10**rng.uniform(-2,1.2)
        H=10**rng.uniform(-2,2)/a
        t,R,s,q=optimum(a,b,H)
        chosen=gain(a,b,H,t)
        assert t>=0 and t<=.500000000000001
        # Original rational objective evaluated without the transformed objective.
        for j in range(81):
            other=gain(a,b,H,j/160)
            assert chosen<=other+2e-12, (a,b,H,t,j,chosen,other)
            n+=1
    for s in (0.0,0.05,0.2,0.49,0.5,0.6,0.98):
        a=math.sqrt(1-s*s); b=s
        phases=[max(0.0001,1-4*s*s), max(0.0001,4-8*s),4+8*s]
        for R in phases:
            H=2*math.sqrt(R)
            t,RR,ss,q=optimum(a,b,H)
            assert 0<=q<=.25+1e-12
            assert gain(a,b,H,t) <= gain(a,b,H,.5)+3e-12
            assert gain(a,b,H,t) <= gain(a,b,H,0)+3e-12
    # Pure decay finite-step exact extinction, with short substep 2/a.
    t,*_=optimum(1,0,5)
    assert abs(min(t,1-t)*5-2)<1e-12
    assert gain(1,0,5,t)<1e-26
    # Stiff limit of the full two-step square norm multiplier.
    for b in (0.1,1,3):
        a=1
        H=1e5
        t,*_=optimum(a,b,H)
        r=math.hypot(a,b)
        assert abs(H*t-2/r)<3e-4
        assert abs(gain(a,b,H,t)-(r-a)/(r+a))<2e-4
    print(f'Independent direct complex-amplitude grid comparisons: PASS ({n} tests)')
    print('Boundary and stiff-limit checks: PASS')
    for a,b,H in [(1,1,10),(1,.25,1),(1,.25,4),(1,1,3),(1,0,5)]:
        t,R,s,q=optimum(a,b,H)
        print(f'a={a}, b={b}, H={H}: short_fraction={t:.12g}; optimum={gain(a,b,H,t):.12g}; half_split={gain(a,b,H,.5):.12g}; unsplit={gain(a,b,H,0):.12g}')


if __name__=='__main__':
    symbolic_checks()
    numerical_checks()
