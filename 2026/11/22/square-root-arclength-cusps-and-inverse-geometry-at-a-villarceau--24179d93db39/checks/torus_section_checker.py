"""Deterministic numerical diagnostics for the Villarceau section-length cusps.

All analytic assertions are motivated by, but do not replace, the proof in RESULT.md.
Requires numpy and scipy. Run: python checks/torus_section_checker.py.
"""
from math import asin, cos, hypot, pi, sin, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk, ellipe


def F(k):
    return ellipe(k*k) - (1-k*k)*ellipk(k*k)


def predicted(R, r):
    a = sqrt(R*R-r*r)
    common = 8*R/r*sqrt(2*r*a)
    return common*F(r/R), common*F(a/R)


def L_exact(R, r, beta):
    s2=sin(beta)**2
    top=pi/2 if R*sqrt(s2)<=r else asin(r/(R*sqrt(s2)))
    def density(phi):
        sn=sin(phi);cs=cos(phi)
        B=sqrt(max(0.0,1-s2*sn*sn))
        D=sqrt(max(0.0,r*r-R*R*s2*sn*sn))
        Bp=-s2*sn*cs/B
        Dp=-R*R*s2*sn*cs/D if D>1e-12 else -1e16
        return hypot(R*B+D,R*Bp+Dp)+hypot(R*B-D,R*Bp-Dp)
    if R*sqrt(s2)<=r:
        return 4*quad(density,0,top,epsabs=3e-8,epsrel=1e-10,limit=400)[0]
    return 4*quad(lambda t: 2*top*t*density(top*(1-t*t)) if t else 0.0,
                  0,1,epsabs=3e-8,epsrel=1e-10,limit=400)[0]


def L_chords(R,r,beta,n=20000):
    """An independent projected-coordinate polyline estimate, not a quadrature."""
    S=sin(beta);s2=S*S
    top=pi/2 if R*S<=r else asin(r/(R*S))
    intervals=[(-pi,pi)] if R*S<r else [(-top,top),(pi-top,pi+top)]
    total=0.
    for lo,hi in intervals:
        phi=np.linspace(lo,hi,n+1)
        q=np.sqrt(np.maximum(0,1-s2*np.sin(phi)**2))
        w=np.sqrt(np.maximum(0,r*r-R*R*s2*np.sin(phi)**2))
        for sg in (1,-1):
            rho=R*q+sg*w
            x=rho*np.cos(phi)
            y=rho*np.sin(phi)
            total+=np.hypot(np.diff(x),np.diff(y)).sum()
    return float(total)


def main():
    count=0
    shapes=[(1.25,1.0),(sqrt(2),1.0),(2.0,1.0),(3.0,1.0),(5.0,2.0)]
    for R,r in shapes:
        critical=asin(r/R)
        Cminus,Cplus=predicted(R,r)
        assert Cminus>0 and Cplus>0; count+=2
        assert abs(L_exact(R,r,0)-4*pi*R)<3e-7;count+=1
        assert abs(L_exact(R,r,pi/2)-4*pi*r)<3e-7;count+=1
        if abs(R/r-sqrt(2))<1e-12:
            assert abs(Cplus/Cminus-1)<1e-12;count+=1
        else:
            assert (Cplus>Cminus)==(R/r>sqrt(2)); count+=1
        for e,tol in [(1e-3,.09),(1e-4,.04),(1e-5,.018)]:
            for sign,C in ((-1,Cminus),(1,Cplus)):
                val=L_exact(R,r,critical+sign*e)
                ratio=(4*pi*R-val)/(C*sqrt(e))
                assert abs(ratio-1)<tol,(R,r,sign,e,ratio,tol)
                count+=1
        for theta in (critical*.45,critical*.85,
                      .55*critical+.45*pi/2, .15*critical+.85*pi/2):
            actual=L_exact(R,r,theta)
            approx=L_chords(R,r,theta)
            assert abs(actual-approx)/actual<0.00045, (R,r,theta,actual,approx)
            count+=1
    # Explicit monotonicity of the ratio as a function of shape.
    ratios=[]
    for t in np.linspace(.08,.97,100):
        ratios.append(F(sqrt(1-t*t))/F(t))
    assert all(a>b for a,b in zip(ratios,ratios[1:]));count+=99
    print('PASS:',count,'deterministic assertions across cusp sides, endpoint lengths, independent polygonal contours and inverse monotonicity')

if __name__=='__main__': main()
