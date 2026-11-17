"""Independent numerical evaluations of hyperbolic cone ball-area identities.
Python 3 standard library only. Scientific identity proofs are in RESULT.md.
"""
from math import pi, sin, cos, tan, atan, asin, asinh, sinh, cosh, acosh, atanh, tanh, exp, log, sqrt, isclose

def simpson(f, lo, hi, n=24000):
    assert n % 2 == 0 and hi >= lo
    h = (hi-lo)/n
    total = f(lo)+f(hi)
    for j in range(1,n):
        total += (4 if j%2 else 2)*f(lo+j*h)
    return total*h/3

def area_closed(R,s,alpha):
    a=alpha/2
    h=sinh(s)*sin(a)
    d=asinh(h)
    if R <= d:
        return 2*pi*(cosh(R)-1)
    u=asin(h/sinh(R))
    theta=atan(cosh(R)*tan(u))
    if R < s:
        return 4*(cosh(R)*theta-u)
    B=atan(cosh(s)*tan(a))
    return 2*cosh(R)*(B+theta)-alpha-2*u

def area_independent(R,s,alpha):
    """Direct radial annular integration using angular sections; no closed formula."""
    a=alpha/2
    qmax=a if R>=s else min(a,asin(min(1.,sinh(R)/sinh(s))))
    def integrand(delta):
        k2=1+sinh(s)**2*sin(delta)**2
        if R < s:
            diff=max(0.,sinh(R)**2-sinh(s)**2*sin(delta)**2)
            return 4*sinh(s)*cos(delta)*sqrt(diff)/k2
        b=atanh(tanh(s)*cos(delta))
        u=acosh(cosh(R)/sqrt(k2))
        return 2*(cosh(b+u)-1)
    return simpson(integrand,0,qmax,24000)

def leading(s,alpha):
    return 2*atan(exp(s)*tan(alpha/4))

def recover(G,alpha):
    return log(tan(G/2)/tan(alpha/4))

for s,alpha in [(0.4,0.6),(1.2,1.5),(2.3,2.7),(3.0,0.2)]:
    d=asinh(sinh(s)*sin(alpha/2))
    G=leading(s,alpha)
    assert isclose(G,atan(cosh(s)*tan(alpha/2))+atan(sinh(d)),rel_tol=1e-13)
    assert isclose(recover(G,alpha),s,abs_tol=2e-13)
    for R in (d*0.8, (d+s)/2, s, s+1.0, s+3.0):
        expected=area_closed(R,s,alpha)
        actual=area_independent(R,s,alpha)
        assert abs(actual-expected)<3e-6*max(1.,expected),(s,alpha,R,actual,expected)
    for R in (s+6,s+9):
        assert abs(area_closed(R,s,alpha)-(G*exp(R)-alpha))<10.0*exp(-R),(s,alpha,R)
    if s-d>0.001:
        K=8./3*sqrt(2*tanh(d))
        eps=min(0.00025,(s-d)/20)
        D=2*pi*(cosh(d+eps)-1)-area_closed(d+eps,s,alpha)
        assert abs(D/eps**1.5-K)/K<0.002,(s,alpha,D,K)
print('HYPERBOLIC_CONE_BALL_VOLUME_AND_INVERSE_CHECKS_OK')
