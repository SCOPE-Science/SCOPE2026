"""Reproducibility tests for three smooth phase-aligned periodic curves.

The analytic proof in RESULT.md, rather than these finite tests, establishes
local minimality on the full Hilbert quotient and global nonuniqueness.
"""
import cmath
import math
from fractions import Fraction


def objective(shifts, u):
    z = sum(cmath.exp(1j * t) for t in shifts)
    w = sum(cmath.exp(1j * (2*t + 2*math.pi*j/3)) for j,t in enumerate(shifts))
    return (abs(z)**2 + u*abs(w)**2), z, w


def check():
    low = (5 - 2*math.sqrt(3))/4
    assert low < Fraction(2,5) < Fraction(1,2)
    assert (Fraction(2,5)*4 - 5 + 2*math.sqrt(3)) > 0
    for u in (0.384, 0.4, 0.425, 0.49):
        assert low < u < .5
        base,_,wbase = objective((0,0,0),u)
        shifted,z,w = objective((0,-math.pi/6,math.pi/6),u)
        assert abs(base-9)<1e-12
        assert abs(wbase)<1e-12
        assert abs(shifted-(4+2*math.sqrt(3)+4*u))<1e-11
        assert shifted>base
        assert abs(z-(1+math.sqrt(3)))<1e-12
        assert abs(w-2)<1e-12
        assert (4*u-5+2*math.sqrt(3))/9>0
        assert 1-2*u>0
    # Cyclic permutation changes only the relative second-harmonic phase.
    x=(.3,1.2,2.3)
    score,z,w=objective(x,.4)
    for shift in (x[1:]+x[:1],x[2:]+x[:2]):
        sc,zz,ww=objective(shift,.4)
        assert abs(sc-score)<1e-11 and abs(zz-z)<1e-11
        assert abs(abs(ww)-abs(w))<1e-11
    # Quadrature checks of the local Hessian against its Fourier formula.
    N=4096
    ts=[2*math.pi*k/N for k in range(N)]
    for u in (.2,.4,.48):
        for A,B,p in ((1,0,0),(0,1,0),(.4,-.5,.2)):
            h=[(-p*math.sin(t),p*math.cos(t),A*math.cos(2*t)+B*math.sin(2*t)) for t in ts]
            norm=sum(sum(k*k for k in v) for v in h)/N
            ip=[]
            for j in range(3):
                ph=2*math.pi*j/3
                ip.append(sum(hv[0]*(-math.sin(t))+hv[1]*math.cos(t)
                    +hv[2]*(-2*math.sqrt(2*u)*math.sin(2*t+ph)) for hv,t in zip(h,ts))/N)
            hess=2*norm-2*sum(q*q for q in ip)/3
            exact=(1-2*u)*(A*A+B*B)
            assert abs(hess-exact)<1e-10,(hess,exact)
    # Polynomial realization: differentiate graph profile along unit circle.
    for j in range(3):
        ph=2*math.pi*j/3
        a=math.sqrt(.8)
        for t in (.0,.4,2.,4.8):
            x,y=math.cos(t),math.sin(t)
            px=a*(2*x*math.cos(ph)-2*y*math.sin(ph))
            py=a*(-2*y*math.cos(ph)-2*x*math.sin(ph))
            assert abs(px*(-y)+py*x + 2*a*math.sin(2*t+ph))<1e-10
    print('VERIFY_OK interval=4 cyclic_shifts=2 hessian_cases=9 polynomial_flow_cases=12')


if __name__ == '__main__':
    check()
