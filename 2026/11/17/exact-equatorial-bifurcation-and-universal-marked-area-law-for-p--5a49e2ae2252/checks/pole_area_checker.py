"""Numerical corroboration of the pinned-pole spherical triangle area law.

Uses independent spherical cosine/Girard calculations for the geometric
area, exact analytic CDF expressions, and deterministic mesh quadrature.
No external packages or network access are required.
"""
import math
from bisect import bisect_right

PI=math.pi

def angle_formula(theta,d):
    c=math.cos(theta)**2+math.sin(theta)**2*math.cos(d)
    c=max(-1.,min(1.,c))
    side=math.acos(c)
    cos_b=math.cos(theta)*(1.-c)/(math.sin(theta)*math.sin(side))
    return d+2.*math.acos(max(-1.,min(1.,cos_b)))-PI

def phase_formula(q,d):
    return 2.*math.atan2(q*math.sin(d),1.+q*math.cos(d))

def cdf(q,x):
    if x<=0.: return 0.
    if q<1.:
        top=2.*math.asin(q)
        if x>=top: return 1.
        return 2./PI*math.asin(math.sin(x/2.)/q)
    if q==1.:
        return min(1.,x/PI)
    if x>=2.*PI: return 1.
    return (x/2.+math.asin(math.sin(x/2.)/q))/PI

for theta in (.17,.71,1.41, PI/2,1.7,2.33,2.94):
    q=math.tan(theta/2.)**2
    for i in range(1,2000):
        d=PI*i/2000.
        x=angle_formula(theta,d)
        y=phase_formula(q,d)
        assert abs(x-y)<2e-9,(theta,d,x,y)
        if q!=1.:
            assert abs(y+phase_formula(1./q,d)-2*d)<2e-13
    grid=sorted(phase_formula(q,PI*(i+.5)/40000.) for i in range(40000))
    xmax=2.*math.asin(q) if q<1. else (PI if q==1. else 2*PI)
    for j in range(1,24):
        x=j*xmax/24.
        empirical=bisect_right(grid,x)/40000.
        assert abs(empirical-cdf(q,x))<5e-5,(q,x,empirical,cdf(q,x))

for u in (.1,.25,.5,.75,.9):
    errs=[]
    for q in (1.01,1.0001,1.000001):
        t=math.acos(1./q)
        val=(phase_formula(q,PI-t*u)-PI)/t
        expected=1./u-u
        errs.append(abs(val-expected))
        assert abs((1.-cdf(q,PI))-t/PI)<1e-12
    assert errs[0]>errs[1]>errs[2]
    assert errs[2]<2e-4

# Folded gap density for f(u)=(1+a cos u)/(2pi):
# h(d)=(1+a^2 cos d/2)/pi, and h(pi)>0.
a=0.6
hpi=(1.-a*a/2.)/PI
for q in (1.001,1.0001):
    t=math.acos(1/q)
    # exact tail via h(d)= (1+a^2*cos(d)/2)/pi integrated near pi
    mass=(t-a*a*math.sin(t)/2.)/PI
    assert abs(mass/(hpi*t)-1.)<0.0001

print('PINNED_POLE_SPHERICAL_AREA_CHECKS_OK')
