"""Exact-rational checks for a single Bass adoption impulse.

Run with Python 3 (standard library only). The general result is analytic;
these checks test independent algebraic identities and finite instances.
"""
from fractions import Fraction as F
from random import Random

CHECKS = 0

def ck(condition, msg):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(msg)


def baseline_y(x, p, q):
    return (p + q*x)/(1-x)


def from_y(y, p, q):
    return (y-p)/(y+q)


def flow(x, h, p, q):
    return from_y(h*baseline_y(x,p,q),p,q)


def pulse_y(y,p,q,a):
    lam=p+q
    return ((lam+a*q)*y+a*q*q)/(lam-a*(y+q))


def terminal_add(p,q,x0,a,h,r):
    x=flow(x0,r,p,q)
    xp=min(F(1),x+a)
    return F(1) if xp==1 else flow(xp,h/r,p,q)


def terminal_prop(p,q,x0,theta,h,r):
    x=flow(x0,r,p,q)
    xp=x+theta*(1-x)
    return flow(xp,h/r,p,q)


def thresholds(p,q,x0,a):
    lam=p+q
    y=baseline_y(x0,p,q)
    hc=(lam/a-q)/y
    hs=q*q*(lam-a*(q+y))/(y*(a*q*(q+y)+lam*y))
    return hs,hc


def predict_add(p,q,x0,a,h):
    hs,hc=thresholds(p,q,x0,a)
    if h>=hc: return 'saturated'
    if hs>1 and h<hs: return 'early'
    if hs>1 and h==hs: return 'both'
    return 'late'

# An exact witness: the horizon threshold h*=45 precedes saturation h_c=100.
p=F(1,10); q=F(1); x0=F(0); a=F(1,10)
hs,hc=thresholds(p,q,x0,a)
ck((hs,hc)==(45,100),'exact switch and saturation')
ck(terminal_add(p,q,x0,a,hs,F(1))==F(9,10),'early tie at 9/10')
ck(terminal_add(p,q,x0,a,hs,hs)==F(9,10),'late tie at 9/10')
ck(terminal_add(p,q,x0,a,F(100),F(100))==F(1),'saturating at final time')
ck(terminal_add(p,q,x0,a,F(100),F(1))<F(1),'early non-saturation')

rng=Random(20261121)
for k in range(12000):
    p=F(rng.randint(1,19),rng.randint(2,31))
    q=F(rng.randint(1,29),rng.randint(1,23))
    x0=F(rng.randint(0,8),10)
    a=(1-x0)*F(rng.randint(1,9),10)
    y=baseline_y(x0,p,q)
    hs,hc=thresholds(p,q,x0,a)
    ck(hc>1 and hc>hs,'ordered finite thresholds')
    ck((hs>1)==(q-p-2*q*x0>q*a),'phase positivity equivalence')
    # Choose a rational total exponential amplification h>1; r enumerates pulse positions.
    h=F(rng.randint(11,200),10)
    if k%17==0: h=hc
    if k%23==0 and hs>1: h=hs
    original=terminal_add(p,q,x0,a,h,F(1))
    end=terminal_add(p,q,x0,a,h,h)
    state=predict_add(p,q,x0,a,h)
    if state=='early': ck(original>end, 'early wins')
    elif state=='late': ck(end>original, 'late wins')
    elif state=='both': ck(original==end,'equal endpoints')
    else:
        ck(end==1,'saturated late')
        ck(original<=end,'saturated dominance')
    # Exhaust rational grid of 0,1/4,1/2,3/4,1 relative to transformed clock r.
    for i in range(5):
        r=1+(h-1)*F(i,4)
        v=terminal_add(p,q,x0,a,h,r)
        ck(v<=max(original,end),'no interior improvement')
        if h<hc:
            ck(v<max(original,end) or i in (0,4), 'strict interior unless endpoint')
        else:
            if r>=hc: ck(v==1,'saturation plateau')
            if r<hc: ck(v<1,'strict below cap')
    theta=F(rng.randint(1,9),10)
    best=terminal_prop(p,q,x0,theta,h,F(1))
    for i in range(1,5):
        r=1+(h-1)*F(i,4)
        ck(best>terminal_prop(p,q,x0,theta,h,r),'percentage pulse must be early')
    # Check exact projective conjugation formula in unsaturated portion.
    if h<hc:
        ye=h*pulse_y(y,p,q,a)
        yl=pulse_y(h*y,p,q,a)
        ck(from_y(ye,p,q)==original, 'early projective conjugation')
        ck(from_y(yl,p,q)==end, 'late projective conjugation')
        expr= -a*(h-1)*(h*y*(a*q*(q+y)+(p+q)*y)-q*q*((p+q)-a*(q+y)))
        denom=((p+q)-a*(q+y))*((p+q)-a*(h*y+q))
        ck(ye-yl==expr/denom,'projective difference identity')

print('CHECKS:', CHECKS)
print('VERIFY_OK')
