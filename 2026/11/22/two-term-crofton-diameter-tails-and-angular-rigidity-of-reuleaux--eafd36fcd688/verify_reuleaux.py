#!/usr/bin/env python3
"""Independent disk-intersection quadrature for long invariant-line chords.

Requires Python 3 and scipy. Run: python verify_reuleaux.py
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq

PI = math.pi


def chord_length(n, phi, offset_from_vertex):
    """Exact interval intersection of all n generating unit disks."""
    rho = 1.0 / (2.0 * math.cos(PI / (2*n)))
    cs, sn = math.cos(phi), math.sin(phi)
    ux, uy, vx, vy = cs, sn, -sn, cs
    t = offset_from_vertex - rho*sn
    left, right = -math.inf, math.inf
    for j in range(n):
        theta = 2*PI*j/n
        x, y = rho*math.cos(theta), rho*math.sin(theta)
        a, b = x*ux+y*uy, x*vx+y*vy
        z = t-b
        if abs(z) > 1:
            return 0.0
        v = math.sqrt(max(0.0,1-z*z))
        left = max(left,a-v)
        right = min(right,a+v)
    return max(0.0,right-left)


def probability(n, eps):
    """Rotate a fundamental sector; integrate both transverse roots."""
    arc = PI/n
    phi0 = PI-arc/2
    bound = math.sqrt(2*eps-eps*eps)
    def width(u):
        phi = phi0+u
        total=0.0
        for sg in (-1,1):
            f=lambda t: chord_length(n,phi,sg*t)-(1-eps)
            assert abs(f(0)-eps)<2e-12, (n,eps,u,sg,f(0))
            assert f(bound)<0, (n,eps,u,sg,f(bound))
            total+=brentq(f,0,bound,xtol=2e-15)
        return total
    pts=[p for p in [math.sqrt(eps),arc-math.sqrt(eps)] if 0<p<arc]
    I,err=quad(width,0,arc,points=sorted(pts),epsabs=2e-10,limit=250)
    return n*I/PI


def asymptotic(n,eps):
    return eps*n/PI*(math.log(1/eps)+1+2*math.log(math.sin(PI/n)))


def main():
    checks=0
    for n in (3,5,7,9):
        prev=None
        for eps in (1e-3,1e-4,1e-5):
            p=probability(n,eps)
            prediction=asymptotic(n,eps)
            error=abs(p-prediction)/eps
            assert 0<p<1 and error<0.04
            if prev is not None:
                assert error<prev
            prev=error
            checks+=3 if eps==1e-3 else 4
            print('n=%d eps=%.0e exact=%.14g two_term=%.14g residual_over_eps=%.7g'%(
                 n,eps,p,prediction,error))
    # Jensen shape functional: sample unequal positive arc-angle vectors
    # to test algebra only; not to assert arbitrary angle lists are realizable.
    for n in (5,7,9):
        mean=PI/n
        for frac in (.03,.1,.2):
            angles=[mean]*n
            angles[0]+=frac*mean
            angles[1]-=frac*mean
            loss=n*math.log(math.sin(mean))-sum(math.log(math.sin(x)) for x in angles)
            assert loss>0
            checks+=1
    print('PASS:',checks,'independent deterministic assertions')

if __name__=='__main__':
    main()
