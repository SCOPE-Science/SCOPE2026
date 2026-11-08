#!/usr/bin/env python3
"""Exact rational branch and orbit checks; numerical sector-area check.
No finite test is a proof of the universal statements in the accompanying note.
"""
from fractions import Fraction as Q
from math import acos, sqrt, sin, pi, cos, isclose, gcd


def mu(s,t,p,q):
    return -s + q*max(t + p*max(s,0),0), -t - p*max(s,0)


def phi(s,t,p,q):
    return p*s*s + (-1 if s<0 and t>0 else 1)*p*q*s*t + q*t*t


def area_integral(p,q,steps=20000):
    # Midpoint quadrature on the polar-angle radial formula.
    d=2*pi/steps
    return sum(1/phi(cos(d*(i+.5)),sin(d*(i+.5)),p,q) for i in range(steps))*d/2


def run():
    checks=0
    examples=[(Q(1),Q(1),5),(Q(1),Q(2),3),(Q(1),Q(3),4),
              (Q(2),Q(1),3),(Q(3),Q(1),4),
              (Q(1,2),Q(2),5),(Q(3,2),Q(2),4)]
    for p,q,period in examples:
        # All sufficiently generic sample points, including both axes,
        # with exact rational arithmetic, all signs, varied denominators.
        for a in range(-9,10):
            for b in range(-9,10):
                s,t=Q(a,5),Q(b,7)
                if s==0 and t==0:
                    continue
                val=phi(s,t,p,q)
                assert val>0
                first=(s,t)
                for j in range(1,period+1):
                    s,t=mu(s,t,p,q)
                    assert phi(s,t,p,q)==val, (p,q,a,b,j)
                    if j<period:
                        assert (s,t)!=first, (p,q,a,b,j)
                    checks+=2
                assert (s,t)==first, (p,q,a,b,period,(s,t))
                checks+=1
    # Degree-one homogeneous map and determinant-one branch checks.
    for p,q in [(1.0,3.0),(1.2,1.7),(.7,1.2),(.25,.5),(.7,4.6)]:
        kap=sqrt(p*q); theta=acos(kap/2)
        analytic=(pi+2*theta)/(2*kap*sin(theta))
        quadrature=area_integral(p,q)
        assert abs(analytic-quadrature)<4e-6, (p,q,analytic,quadrature)
        checks+=1
        for s,t in [(2.3,-1.4),(-2,1),(1,0),(-1,-.9),(.1,.5)]:
            A=mu(s,t,p,q)
            B=mu(2*s,2*t,p,q)
            assert all(abs(2*x-y)<1e-12 for x,y in zip(A,B))
            assert isclose(phi(*A,p,q),phi(s,t,p,q),rel_tol=1e-12,abs_tol=1e-12)
            checks+=2
    # Sector area fraction is 2 theta / (pi + 2 theta); checking the
    # linear image angle of the distinguished ray is a separate identity.
    for n,d in [(1,3),(1,4),(1,6),(2,7),(2,9),(3,8),(1,7)]:
        theta=pi*n/d; p=1.0;q=4*cos(theta)**2
        s,t=mu(1.0,0.0,p,q)
        u=s+cos(theta)*sqrt(q)*t
        v=sin(theta)*sqrt(q)*t
        assert abs(u-cos(2*theta))<1e-12
        assert abs(v+sin(2*theta))<1e-12
        expected=(d+2*n)//gcd(2*n,d)
        z=(1.234,-0.987)
        x=z
        for _ in range(expected):
            x=mu(*x,p,q)
        assert max(abs(x[i]-z[i]) for i in range(2))<1e-9, (n,d,expected)
        checks+=3
    print(f'TROPICAL_ROTATION_EXACT_AND_AREA_CHECK_OK {checks}')


if __name__ == '__main__':
    run()
