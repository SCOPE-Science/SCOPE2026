#!/usr/bin/env python3
"""Exact sanity checks of spherical tangential-gradient moments, using only sympy."""
from itertools import product
from fractions import Fraction
import sympy as s

def sphere_monomial_average(powers,n):
    if any(e % 2 for e in powers): return s.S.Zero
    degree=sum(powers)//2
    val=s.S.One
    for e in powers:
        for j in range(1,e,2): val*=j
    for j in range(degree): val/= n+2*j
    return s.factor(val)

def integrate(poly,n):
    x=s.symbols('x:'+str(n))
    pol=s.Poly(poly,*x)
    return s.factor(sum(co*sphere_monomial_average(m,n) for m,co in pol.terms()))

def checks():
    n=s.symbols('n',positive=True,integer=True)
    a=n*n+6*n+12
    b=2*n*(n+2)
    # Gaussian to spherical radial calculations
    moment_s2=((n+4)*(n+6))*s.Symbol('T2')**2 + 2*(n+4)*(n+6)*s.Symbol('T4')
    moment_sq2=-2*(n+6)*(2*s.Symbol('T2')**2+8*s.Symbol('T4'))
    moment_q4=12*s.Symbol('T2')**2+48*s.Symbol('T4')
    assert s.expand(moment_s2+moment_sq2+moment_q4-a*s.Symbol('T2')**2-b*s.Symbol('T4'))==0
    print('SYMBOLIC_GENERAL_MOMENT_IDENTITY_OK')
    configurations=[(2,(1,-1)),(3,(1,-1,0)),(3,(2,-1,-1)),(4,(1,-1,0,0)),(4,(1,1,-1,-1)),(4,(3,-1,-1,-1)),(5,(3,3,-2,-2,-2)),(5,(4,-1,-1,-1,-1)),(6,(1,1,1,-1,-1,-1)),(6,(5,-1,-1,-1,-1,-1))]
    for N,L in configurations:
        x=s.symbols('x:'+str(N))
        q=sum(L[i]*x[i]**2 for i in range(N))
        v=sum(L[i]**2*x[i]**2 for i in range(N))
        M2=s.factor(4*integrate(v-q*q,N))
        M4=s.factor(16*integrate((v-q*q)**2,N))
        T2=sum(t*t for t in L);T4=sum(t**4 for t in L)
        assert M2==s.Rational(4*T2,N+2),(N,L,M2)
        expected=s.Rational(16*((N*N+6*N+12)*T2*T2+2*N*(N+2)*T4),N*(N+2)*(N+4)*(N+6))
        assert M4==expected,(N,L,M4,expected)
    print('DIRECT_EXACT_SPHERE_POLYNOMIAL_INTEGRATION_OK',len(configurations))
    for N in range(2,101):
        r=lambda k:s.Rational(N,k*(N-k))-s.Rational(3,N)
        rmin=s.Rational(1,N) if N%2==0 else s.Rational(N*N+3,N*(N*N-1))
        rmax=s.Rational(N*N-3*N+3,N*(N-1))
        assert r(N//2)==rmin and r(1)==rmax
        assert all(rmin<=r(k)<=rmax for k in range(1,N))
        C=lambda z: s.factor(s.Rational((N+2),N*(N+4)*(N+6))*(N*N+6*N+12+2*N*(N+2)*z))
        assert C(rmin)<=C(rmax)
        if N==2: assert C(rmin)==s.Rational(3,2)
        if N==3: assert C(rmin)==s.Rational(10,7)
        if N==4: assert C(rmin)==s.Rational(6,5) and C(rmax)==s.Rational(3,2)
    print('EXACT_TWO_LEVEL_SPECTRAL_ENDPOINTS_AND_PARITY_OK n=2..100')
    # On a unit norm sphere, the three-root Lagrange Hessian has a flat direction
    # with a nonzero cross term against a repeated-root antisymmetric direction.
    a,b=s.symbols('a b',real=True); c=-a-b; f=a*a+a*b+b*b
    E=lambda z:3*z*z-f
    tangent=[0,b-c,c-a,a-b]
    cross=s.factor(-E(a)*(b-c))
    flat=s.factor(E(a)*(b-c)**2+E(b)*(c-a)**2+E(c)*(a-b)**2)
    assert flat==0 and cross!=0
    assert s.factor(E(a))==s.factor(2*a*a-a*b-b*b)
    print('THREE_ROOT_HESSIAN_EXCLUSION_IDENTITY_OK')
    print('ALL_TANGENTIAL_GRADIENT_EXACT_CHECKS_OK')
if __name__=='__main__':checks()
