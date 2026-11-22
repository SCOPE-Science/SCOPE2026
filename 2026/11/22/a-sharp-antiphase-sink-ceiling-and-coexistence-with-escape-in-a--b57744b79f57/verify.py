"""Finite consistency checks for the explicit Gaussian-cubic anti-diagonal theorem."""
import math

E2 = math.exp(2)

def f(a, x):
    return a*x*(1-x*x)*math.exp(-x*x)

def fd(a, x):
    u=x*x
    return a*math.exp(-u)*(1-5*u+2*u*u)

def calc(a, u):
    s=math.sqrt(u)
    b=(a*(1-u)*math.exp(-u)-1)/2
    xp=f(a,s)+b*(-2*s)
    yp=f(a,-s)+b*(2*s)
    lam_normal=fd(a,s)
    lam_tangent=fd(a,s)-2*b
    assert abs(xp-s)<1e-10*max(1,s)
    assert abs(yp+s)<1e-10*max(1,s)
    assert abs(lam_tangent-(1+2*a*u*(u-2)*math.exp(-u)))<1e-10
    # The full two-by-two derivative has off-diagonal entries b.
    diagonal=fd(a,s)-b
    assert abs((diagonal+b)-lam_normal)<1e-10
    assert abs((diagonal-b)-lam_tangent)<1e-10
    return b,lam_normal,lam_tangent

def bisect(g,lo,hi):
    flo=g(lo)
    for _ in range(120):
        mid=(lo+hi)/2
        fm=g(mid)
        if flo*fm<=0:
            hi=mid
        else:
            lo=mid; flo=fm
    return (lo+hi)/2

def roots(c):
    g=lambda u:(1-u)*math.exp(-u)-c
    r=[]
    if -math.exp(-2)<c<1:
        r.append(bisect(g,0,2))
    if -math.exp(-2)<c<0:
        r.append(bisect(g,2,100))
    return r

n=0
for a in (0.12,0.5,3.11,4.0,6.0):
    bf=-0.5-a/(2*E2)
    assert bf<-.5
    for du in (0.0002,0.001,0.01,0.03):
        u=2-du
        b,normal,tangent=calc(a,u)
        assert bf<b<-.5
        assert abs(normal)<1 and abs(tangent)<1
        allroots=roots((1+2*b)/a)
        assert len(allroots)==2
        assert abs(allroots[0]-u)<1e-8
        assert allroots[1]>2
        _,_,outer_tangent=calc(a,allroots[1])
        assert outer_tangent>1
        # Distinct finite hyperbolic sinks, with an unbounded open half-difference cone.
        n+=1
for a in (E2, E2+0.1, 9.0, 50.0):
    for u in (0.0001,0.03,0.1,0.15,0.17,0.3,0.6,0.9,1,1.2,1.7,1.95,2,2.05,3,7):
        _,normal,tangent=calc(a,u)
        assert not(abs(normal)<1 and abs(tangent)<1)
        n+=1
for a in (0.3,3.11,8.0):
    for c,expected in ((-0.3,0),(-math.exp(-2)/2,2),(-0.08,2),(0,1),(0.4,1),(1.2,0)):
        if c<0 and c>-math.exp(-2): expected=2
        if c==0: expected=1
        assert len(roots(c))==expected
        n+=1
print('PASS',n,'parameter and Jacobian checks')
