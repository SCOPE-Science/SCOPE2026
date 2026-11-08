"""Reproducible numerical checks for vacuum--Hermite spectrogram critical-point transitions.

The proofs of existence, uniqueness, and classification are analytic; this script
checks their scalar consequences and independent Cartesian finite differences.
Requires only the Python standard library.
"""
import cmath
import math
import random

checks = 0

def verify(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def bisect(f, lo, hi, iterations=95):
    fl, fh = f(lo), f(hi)
    if not (fl * fh < 0):
        raise ValueError(('no bracket', lo, hi, fl, fh))
    for _ in range(iterations):
        mid = (lo + hi) * .5
        fm = f(mid)
        if fm * fl > 0:
            lo, fl = mid, fm
        else:
            hi = mid
    return (lo + hi) * .5

def fold(m):
    return 1 / (2 * (m - 2)**((m - 2)/2))

def star_t(m):
    return bisect(lambda t: math.log(m/(m-t))-t/2, m-2, m-1e-12)

def star(m):
    t=star_t(m)
    return 1/(t**((m-2)/2)*(m-t))

def equation(m, a, t, sign):
    # sign +1: constructive rays, sign -1: destructive rays.
    return a * t**((m-2)/2) * (m-t) - 1 if sign==1 else a*t**((m-2)/2)*(t-m)-1

def roots(m, a):
    ac=fold(m)
    plus=[]
    if a>ac:
        plus=[bisect(lambda t:equation(m,a,t,1), 1e-14, m-2),
              bisect(lambda t:equation(m,a,t,1), m-2, m-1e-14)]
    minus=bisect(lambda t:equation(m,a,t,-1), m, max(2*m, 2*a**(-2/m)+m))
    return plus, minus

def signal(m,a,z):
    return (abs(1+a*z**m)**2) * math.exp(-abs(z)**2)

def deriv(m,a,z):
    f=1+a*z**m
    d=m*a*z**(m-1)-z.conjugate()*f
    return (2*math.exp(-abs(z)**2)*(d*f.conjugate()).real,
            -2*math.exp(-abs(z)**2)*(d*f.conjugate()).imag)

random.seed(2026)
for m in range(3,18):
    ac=fold(m)
    astar=star(m)
    ts=star_t(m)
    verify(0<ac<astar, f'ordered thresholds {m}')
    verify(m-2<ts<m, f'star interval {m}')
    verify(abs(2*math.log(m/(m-ts))-ts)<1e-8, f'height crossing {m}')
    verify(abs((m/(m-ts))**2*math.exp(-ts)-1)<2e-8, f'crossing height {m}')
    for factor in [0.5,0.9,1.1, 1.5,2.0]:
        a=ac*factor
        plus,minus=roots(m,a)
        verify(len(plus)==(2 if factor>1 else 0), f'fold branch {m,factor}')
        verify(minus>m, f'destructive saddle radius {m,factor}')
        verify(abs(equation(m,a,minus,-1))<1e-8, f'saddle equation {m,factor}')
        verify(abs(deriv(m,a,cmath.rect(math.sqrt(minus),math.pi/m))[0])<1e-7,
               f'destructive Cartesian derivative {m,factor}')
        verify(abs(deriv(m,a,cmath.rect(math.sqrt(minus),math.pi/m))[1])<1e-7,
               f'destructive Cartesian derivative y {m,factor}')
        if plus:
            t1,t2=plus
            verify(0<t1<m-2<t2<m, f'constructive order {m,factor}')
            for t in plus:
                verify(abs(equation(m,a,t,1))<1e-8, f'constructive critical eq {m,factor}')
                for j in range(m):
                    z=cmath.rect(math.sqrt(t),2*math.pi*j/m)
                    dx,dy=deriv(m,a,z)
                    verify(math.hypot(dx,dy)<1e-7, f'constructive gradient {m,factor,j}')
            delta=1e-4
            for t,kind in [(t1,'min'),(t2,'max')]:
                rad=lambda tt: signal(m,a,math.sqrt(tt))
                u=rad(t)
                verify((u<min(rad(t-delta),rad(t+delta))) if kind=='min' else
                       (u>max(rad(t-delta),rad(t+delta))),f'radial {kind}: {m,factor}')
        # zero roots are nondegenerate minima; one ring of destructive saddles.
        z=cmath.rect(a**(-1/m),math.pi/m)
        verify(signal(m,a,z)<1e-22, f'zero {m,factor}')
        verify(signal(m,a,0)==1, f'center {m,factor}')
    for fac in [.96,1.0,1.04]:
        a=astar*fac
        plus,minus=roots(m,a)
        t2=plus[1]
        maxheight=signal(m,a,math.sqrt(t2))
        verify(maxheight<1+1e-8 if fac<1 else
               abs(maxheight-1)<2e-8 if fac==1 else maxheight>1-1e-8,
               f'global height transition {m,fac}')

for m in range(3,10):
    for _ in range(32):
        a=math.exp(random.uniform(-3,1))
        z=complex(random.uniform(-2,2),random.uniform(-2,2))
        h=1e-5
        dx,dy=deriv(m,a,z)
        dxf=(signal(m,a,z+h)-signal(m,a,z-h))/(2*h)
        dyf=(signal(m,a,z+1j*h)-signal(m,a,z-1j*h))/(2*h)
        verify(abs(dx-dxf)<1e-7*(1+abs(dx)),f'cartesian dx {m}')
        verify(abs(dy-dyf)<1e-7*(1+abs(dy)),f'cartesian dy {m}')

for m in [25,30,35,40]:
    r=star(m)/fold(m)
    approx=2*math.exp(m/2-1)/m
    verify(abs(r/approx-1)<.05, f'asymptotic ratio {m}')
print('HUSIMI_TWO_THRESHOLD_CHECKS_PASS',checks)
