#!/usr/bin/env python3
"""Exact rational checks for quadratic spherical Poisson modulation.

This is a finite consistency test, not a substitute for the infinite identity
or the analytic positive-definiteness argument in RESULT.md.
"""
from fractions import Fraction as F
from math import comb


def poladd(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out


def polmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return out


def pscale(a,c):return [x*c for x in a]


def legendre(N):
    p=[[F(1)],[F(0),F(1)]]
    for n in range(1,N):
        xpn=[F(0)]+p[n]
        p.append(pscale(poladd(pscale(xpn,2*n+1),pscale(p[n-1],-n)),F(1,n+1)))
    return p[:N+1]


def S(n,r):return (F(n)/r+(n+1)*r)/(2*n+1)


def T(n,r):
    return F(3,2)*(F(n*(n-1),(2*n-1)*(2*n+1))/r**2
      +F(n*n,(2*n-1)*(2*n+1))
      +F((n+1)**2,(2*n+1)*(2*n+3))
      +F((n+1)*(n+2),(2*n+1)*(2*n+3))*r**2)-F(1,2)


def lims(r):return ((1+r*r)/(2*r),(3*r**4+2*r*r+3)/(8*r*r))


def weights(n,r):
    d=(2*n-1)*(2*n+1)*(2*n+3)*(r*r+15)
    return (3*(n-1)*((10-2*r*r)*n+r*r+15)/d,
       15*n*((2*r*r+6)*n+9-r*r)/d,
       4*n*(n-1)*((2*r*r+30)*n+45-r*r)/d)


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
      -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
      +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def check():
    tests=0
    for r in (F(1,10),F(1,3),F(1,2),F(3,4),F(9,10),F(99,100)):
        s0,t0=S(0,r),T(0,r)
        s1,t1=S(1,r),T(1,r)
        si,ti=lims(r)
        assert det3([[1,s0,t0],[1,s1,t1],[1,si,ti]]) == (1-r*r)**2*(r*r+15)/(120*r**3)
        tests+=1
        for n in range(2,201):
            w0,w1,wi=weights(n,r)
            assert min(w0,w1,wi)>0
            assert w0+w1+wi==1
            assert S(n,r)==w0*s0+w1*s1+wi*si
            assert T(n,r)==w0*t0+w1*t1+wi*ti
            tests+=4
        av,bv=-6/r,5/r**2
        assert 1+av*s0+bv*t0==0 and 1+av*s1+bv*t1==0
        assert 1+av*si+bv*ti>0
        den=6*r**4+31*r*r+15
        av,bv=-9*r*(3*r*r+5)/den,20*r*r/den
        assert 1+av*s1+bv*t1==0 and 1+av*si+bv*ti==0
        assert 1+av*s0+bv*t0>0
        tests+=2
        # Cross-check exact Legendre coefficients via polynomial multiplication.
        N=12
        ps=legendre(N+2)
        base=[F(0)]
        for k in range(N+3):base=poladd(base,pscale(ps[k],(2*k+1)*r**k))
        for a,b in ((F(1,2),F(-1,3)),(F(-2),F(3)),(F(5),F(7))):
            product=polmul(base,poladd([1],poladd(pscale(ps[1],a),pscale(ps[2],b))))
            # coefficient = (2n+1)/2 * integral_{-1}^1 product * Pn
            for n in range(N+1):
                pol=polmul(product,ps[n])
                integral=sum((pol[k]*F(2,k+1) for k in range(0,len(pol),2)),F(0))
                coeff=F(2*n+1,2)*integral
                expected=(2*n+1)*r**n*(1+a*S(n,r)+b*T(n,r))
                assert coeff==expected,(r,a,b,n,coeff,expected)
                tests+=1
    print('CHECK_OK rational_identities_and_legendre_coefficients',tests)


if __name__=='__main__': check()
