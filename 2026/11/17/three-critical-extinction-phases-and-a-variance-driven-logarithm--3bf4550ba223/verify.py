#!/usr/bin/env python3
"""Exact identity checks and independent finite-orbit diagnostics for the stated rational map."""
import math
import sympy as sp

x, y, t, eta, a, b, z = sp.symbols('x y t eta a b z', real=True)
f = lambda u: eta/(1+a*u)+(1-eta)/(1+b*u)
fx = x*f(x+t*y)
fy = y*f(t*x+y)
factor = eta*(1+a*t*(x+y))/((1+a*(x+t*y))*(1+a*(t*x+y))) + (1-eta)*(1+b*t*(x+y))/((1+b*(x+t*y))*(1+b*(t*x+y)))
assert sp.cancel(fx-fy-(x-y)*factor)==0
c=eta*a+(1-eta)*b
v=eta*(1-eta)*(a-b)**2
s=eta*a*a+(1-eta)*b*b
assert sp.cancel(s-c*c-v)==0
assert sp.cancel(sp.series(1/f(z),z,0,3).removeO() -(1+c*z-v*z*z))==0

E, A, B = .4, 2., .5
C=E*A+(1-E)*B
V=E*(1-E)*(A-B)**2
results={}
for tau in (.4,1.,1.8,2.5):
    xx,yy=.42,.15
    samples={}
    for n in range(1,200001):
        u=xx+tau*yy; w=tau*xx+yy
        xx *= E/(1+A*u)+(1-E)/(1+B*u)
        yy *= E/(1+A*w)+(1-E)/(1+B*w)
        assert xx>0 and yy>0 and xx>yy
        if n in (20000,200000):
            if tau<1: samples[n]=(n*xx,n*yy,(xx-yy)*n**(2/(1+tau)))
            elif tau==1: samples[n]=(n*(xx+yy),1/(xx+yy)-C*n+(V/C)*math.log(n),xx/yy)
            else: samples[n]=(n*xx,yy*n**tau)
    results[tau]=samples
    end=samples[200000]
    if tau<1:
        assert abs(end[0]-1/(C*(1+tau)))<.025
        assert abs(end[1]-1/(C*(1+tau)))<.025
        assert end[2]>0
    elif tau==1:
        assert abs(end[0]-1/C)<.025
        assert abs(end[2]-.42/.15)<1e-8
        assert abs(samples[20000][1]-end[1])<.01
    else:
        assert abs(end[0]-1/C)<.025
        assert end[1]>0
        assert abs(end[1]-samples[20000][1])/(1+abs(end[1]))<.02
print('VERIFY_OK: symbolic identities and four finite parameter regimes')
for tau,samples in results.items(): print(tau,samples)
