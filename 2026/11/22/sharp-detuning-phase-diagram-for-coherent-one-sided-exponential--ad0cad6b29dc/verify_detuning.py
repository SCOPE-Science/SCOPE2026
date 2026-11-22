"""Independent finite diagnostics for critical two-tone exponential Gabor thresholds.

Run with Python 3: python verify_detuning.py.  Not a substitute for the proof.
"""
import cmath
import math

TAU = 2.0 * math.pi
checks = 0


def verify(cond, detail=''):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(detail)


def interval(r, h):
    theta = TAU * h
    q = 1 - r*r
    if h <= .5:
        delta = r*r - math.cos(math.pi*h)**2
        if delta < -1e-13:
            return None
        s = math.sqrt(max(0., delta))
        t = r*r - math.cos(theta)
        return ((t - 2*math.sin(math.pi*h)*s)/q,
                (t + 2*math.sin(math.pi*h)*s)/q)
    R = abs(1-r*r*cmath.exp(1j*theta))
    t = 2*r*math.sin(math.pi*h)
    return ((R-t)/q, (R+t)/q)


def phi_min(r,h):
    theta=TAU*h
    if h<=.5:
        return theta
    arg=math.atan2(-r*r*math.sin(theta),1-r*r*math.cos(theta))
    return math.pi+arg


def Q(r,h,c,phi):
    theta=TAU*h
    return (1-r*r)*(1+c*c)+2*c*(math.cos(phi)-r*r*math.cos(theta-phi))


def zak(r,h,c,x,y):
    theta=TAU*h
    z=cmath.exp(-1j*TAU*y)
    return (r**x)*(
        1/(1-r*z)+c*cmath.exp(-1j*theta*x)/(1-r*cmath.exp(-1j*theta)*z))


def zero_frequency(r,h,c,phi):
    theta=TAU*h
    d=r*(cmath.exp(-1j*theta)+c*cmath.exp(-1j*phi))
    if abs(d)<1e-13:
        raise ValueError('zero denominator')
    z=(1+c*cmath.exp(-1j*phi))/d
    y=(-cmath.phase(z)/TAU)%1
    return z,y


def bisect_cross(r,h,c,lo,hi,ascending=False):
    vlo=Q(r,h,c,lo)
    vhi=Q(r,h,c,hi)
    if ascending:
        verify(vlo < 1e-8 and vhi > -1e-8,(r,h,c,lo,hi,vlo,vhi))
    else:
        verify(vlo > -1e-8 and vhi < 1e-8,(r,h,c,lo,hi,vlo,vhi))
    for _ in range(75):
        mid=(lo+hi)/2
        vm=Q(r,h,c,mid)
        if (vm>0) == (not ascending):lo=mid
        else:hi=mid
    return (lo+hi)/2


for r in (.12, .42, .7, .93):
    for h in (.08, .22, .4, .49, .5, .51, .64, .8, .94):
        theta=TAU*h
        crit=interval(r,h)
        phis=[theta*i/12000 for i in range(12001)]
        minq_numeric=min(math.cos(t)-r*r*math.cos(theta-t) for t in phis)
        pm=phi_min(r,h)
        minq_formula=math.cos(pm)-r*r*math.cos(theta-pm)
        verify(abs(minq_formula-minq_numeric)<2e-7,(r,h,minq_formula,minq_numeric))
        if crit is None:
            verify(h<.5 and r<math.cos(math.pi*h))
            for c in (.12, .7, 1., 1.8, 9.):
                verify(min(Q(r,h,c,t) for t in phis)>0,(r,h,c))
        else:
            left,right=crit
            verify(left>0 and right>=left,(r,h,crit))
            verify(abs(left*right-1.)<1e-8,(r,h,left,right))
            for c in (left*.8, right*1.2):
                verify(min(Q(r,h,c,t) for t in phis)>0,(r,h,c))
            c=1.0
            verify(Q(r,h,c,pm)<1e-9,(r,h,c,pm))
            ph=bisect_cross(r,h,c,0,pm)
            z,y=zero_frequency(r,h,c,ph)
            verify(abs(abs(z)-1)<1e-8,(r,h,c,ph,z))
            verify(abs(zak(r,h,c,ph/theta,y))<1e-8,(r,h,c,ph,y))
            if h>.5 and Q(r,h,c,theta)>1e-7:
                ph2=bisect_cross(r,h,c,pm,theta,ascending=True)
                z2,y2=zero_frequency(r,h,c,ph2)
                verify(abs(abs(z2)-1)<1e-8 and abs(zak(r,h,c,ph2/theta,y2))<1e-8)
            for boundary in (left,right):
                verify(abs(Q(r,h,boundary,pm))<2e-8,(r,h,boundary,pm))
                z0,y0=zero_frequency(r,h,boundary,pm)
                verify(abs(abs(z0)-1)<2e-7,(r,h,boundary,z0))
                verify(abs(zak(r,h,boundary,pm/theta,y0))<2e-7)

# Independent geometric series comparison with finite partial sums.
for r,h,c,x,y in ((.3,.4,.7,.24,.11),(.8,.72,1.3,.6,.9),(.42,.51,.3,.8,.2)):
    exact=zak(r,h,c,x,y)
    partial=sum(r**(x+n)*(1+c*cmath.exp(-1j*TAU*h*(x+n)))
                *cmath.exp(-1j*TAU*y*n) for n in range(200))
    verify(abs(exact-partial)<1e-11)
print(f'PASS: {checks} supplementary assertions; analytic proof required for all parameters')
