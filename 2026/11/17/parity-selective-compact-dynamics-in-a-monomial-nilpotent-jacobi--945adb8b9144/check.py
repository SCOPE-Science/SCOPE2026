#!/usr/bin/env python3
"""Supplemental finite checks for a monomial skew Hamiltonian (stdlib only).

Analytical arguments in RESULT.md, not these finite checks, prove the all-degree assertions.
"""
from math import sqrt, sin, cos, pi, isfinite
from fractions import Fraction


def potential(v, m):
    return v - v**(2*m+1)/(2*m+1)


def turning_points(energy, m):
    f = lambda v: potential(v,m)-energy
    l, r = -3.0, -1.0
    assert f(l)>0 and f(r)<0
    for _ in range(100):
        mid=(l+r)/2
        if f(mid)>0: l=mid
        else: r=mid
    a=(l+r)/2
    l,r=-1.0,1.0
    assert f(l)<0 and f(r)>0
    for _ in range(100):
        mid=(l+r)/2
        if f(mid)<0: l=mid
        else: r=mid
    return a,(l+r)/2


def integrals(energy,m,steps=8000):
    assert steps%2==0
    a,b=turning_points(energy,m)
    vprime=lambda v: 1-v**(2*m)
    def g(theta):
        if theta==0:
            return 2*sqrt((b-a)/(-vprime(a)))
        if theta==pi/2:
            return 2*sqrt((b-a)/vprime(b))
        s,c=sin(theta),cos(theta)
        v=a+(b-a)*s*s
        residual=energy-potential(v,m)
        if residual<=0: # near endpoint only; avoid cancellation with endpoint limit
            if theta<pi/4: return 2*sqrt((b-a)/(-vprime(a)))
            return 2*sqrt((b-a)/vprime(b))
        return 2*(b-a)*s*c/sqrt(residual)
    period_total=0.0
    drift_total=0.0
    for i in range(steps+1):
        theta=(pi/2)*i/steps
        vv=a+(b-a)*sin(theta)**2
        base=g(theta)
        wt=1 if i==0 or i==steps else (4 if i%2 else 2)
        period_total+=wt*base
        drift_total+=wt*base*vv**m
    factor=sqrt(2)*(pi/2)/(3*steps)
    return period_total*factor,drift_total*factor


def exact_vector_field(x,y,z,m):
    v=y+x*x
    return v**m, z-2*x*v**m, v**(2*m)-1


def exact_jacobian(x,y,z,m):
    v=y+x*x
    a=m*v**(m-1)
    b=2*m*v**(2*m-1)
    return [[2*x*a,a,0],[-2*v**m-4*x*x*a,-2*x*a,1],[2*x*b,b,0]]


def mul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def check_jacobians():
    for m in (1,2,3,4,5,7):
        for x,y in ((Fraction(0),Fraction(0)),(Fraction(1,3),Fraction(-2,5)),(Fraction(-3,4),Fraction(1,2))):
            J=exact_jacobian(x,y,Fraction(1,7),m)
            assert mul(mul(J,J),J)==[[0]*3 for _ in range(3)]
    print('EXACT_JACOBIAN_CUBE_ZERO_ON_TEST_POINTS_OK',flush=True)


def check_integrals():
    for m in (1,2,3,4,5):
        lower=-2*m/(2*m+1)
        upper=-lower
        for theta in (0.10,0.50,0.9):
            E=lower+(upper-lower)*theta
            T,D=integrals(E,m,steps=4000)
            assert T>0 and isfinite(T) and isfinite(D)
            if m%2==0: assert D>0
        if m%2==1:
            t0,d0=integrals(0.0,m,steps=8000)
            t1,d1=integrals(upper-1.e-6,m,steps=8000)
            assert d0<0 and d1>0,(m,d0,d1)
            lo,hi=0.0,upper-1.e-6
            for _ in range(30):
                mid=(lo+hi)/2
                if integrals(mid,m,steps=4000)[1]<0:lo=mid
                else:hi=mid
            root=(lo+hi)/2
            residual=integrals(root,m,steps=10000)[1]
            assert abs(residual)<3.e-4,(m,residual)
            print('ODD_ROOT_CHECK',m,'E=',round(root,11),'drift_error=',round(residual,8),flush=True)
    print('FINITE_QUADRATURE_CROSSCHECK_OK',flush=True)


if __name__=='__main__':
    check_jacobians()
    check_integrals()
