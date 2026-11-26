#!/usr/bin/env python3
"""Supplementary algebraic and numerical checks of a signed spherical Poisson kernel.
Requires SymPy and mpmath. The infinite argument is given in RESULT.md.
"""
import sympy as s
import mpmath as mp

n, t = s.symbols('n t', positive=True)
A = 3*n*(n-1)/(2*(2*n-1)*(2*n+1))
B = n*(n+1)/((2*n-1)*(2*n+3))
C = 3*(n+1)*(n+2)/(2*(2*n+1)*(2*n+3))
R = A/t + B + C*t
Rinf = (3+2*t+3*t**2)/(8*t)
Delta = 3*(1-t)*(2*n**2*(1+t)+n*(3*t+5)-2*t)/(t*(2*n-1)*(2*n+1)*(2*n+3)*(2*n+5))
Gap = 3*(1-t)*(8*n**2*(1+t)+n*(6*t+10)-5*t-3)/(8*t*(2*n-1)*(2*n+1)*(2*n+3))
assert s.cancel((R.subs(n,n+1)-R)-Delta)==0
assert s.cancel((Rinf-R)-Gap)==0
assert s.simplify(s.limit(n*(Rinf-R),n,s.oo)-3*(1-t)*(1+t)/(8*t))==0
assert s.simplify(R.subs(n,0)-t)==0
assert s.simplify(R.subs(n,1)-(s.Rational(2,5)+s.Rational(3,5)*t))==0
count = 5

# Exact triple-product expansion and Legendre moments via rational integration.
x = s.symbols('x')
for ell in range(0,20):
    p=s.legendre(ell,x)
    product=s.expand((3*x*x-1)*p/2)
    reconstructed=s.Integer(0)
    for j in [ell-2,ell,ell+2]:
        if j<0:continue
        coeff=s.integrate(product*s.legendre(j,x),(x,-1,1))*s.Rational(2*j+1,2)
        reconstructed+=coeff*s.legendre(j,x)
    assert s.expand(product-reconstructed)==0
    count+=1

# Exact formula against actual truncated Poisson/Legendre convolution sums.
for rad in (s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)):
    for degree in range(0,18):
        a=s.Rational(0)
        for ell in (degree-2,degree,degree+2):
            if ell<0:continue
            coeff=s.integrate((3*x*x-1)*s.legendre(ell,x)*s.legendre(degree,x)/2,(x,-1,1))*s.Rational(2*degree+1,2)
            a+=(2*ell+1)*rad**ell*coeff
        calc=s.cancel(a/((2*degree+1)*rad**degree))
        assert s.simplify(calc-R.subs({n:degree,t:rad**2}))==0
        count+=1

mp.mp.dps=65
for rstr in ('0.2','0.4','0.7'):
    r=mp.mpf(rstr)
    for ell in range(0,13):
        ps=lambda xx:mp.legendre(ell,xx)
        P=lambda xx:(1-r*r)/(1-2*r*xx+r*r)**mp.mpf('1.5')
        integrand=lambda xx:P(xx)*(3*xx*xx-1)/2*ps(xx)
        direct=(2*ell+1)/2*mp.quad(integrand,[-1,0,1])
        a=mp.mpf(3*ell*(ell-1))/(2*(2*ell-1)*(2*ell+1)) if ell>=2 else mp.mpf(0)
        b=mp.mpf(ell*(ell+1))/((2*ell-1)*(2*ell+3)) if ell>=1 else mp.mpf(0)
        c=mp.mpf(3*(ell+1)*(ell+2))/(2*(2*ell+1)*(2*ell+3))
        target=(2*ell+1)*r**ell*(a/r**2+b+c*r**2)
        assert mp.almosteq(direct,target,rel_eps=mp.mpf('1e-42'),abs_eps=mp.mpf('1e-42')),(r,ell,direct,target)
        count+=1

# Check all finite positive ratios are below the limiting obstruction,
# and convergence is of exactly first inverse-degree order.
for rad in (s.Rational(1,10),s.Rational(1,2),s.Rational(3,4),s.Rational(9,10)):
    rat=rad**2
    prev=None
    for k in range(0,400):
        val=R.subs({t:rat,n:k})
        inf=Rinf.subs(t,rat)
        assert val<inf
        if prev is not None:assert val>prev
        prev=val
        count+=2

print(f'PASS: {count} verified exact or numerical assertions')
