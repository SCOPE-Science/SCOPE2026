#!/usr/bin/env python3
"""Independent exact-algebra and numerical tests for a spherical kernel classification."""
import sympy as S
import numpy as np
from numpy.polynomial.legendre import leggauss,legval

r,n=S.symbols('r n', positive=True)
b,c=S.symbols('b c', real=True)

def A(n): return (n/r+(n+1)*r)/(2*n+1)
def B(n):
    return S.factor(S.Rational(3,2)*(n*(n-1)/((2*n-1)*(2*n+1)*r*r) + (n+1)**2/((2*n+1)*(2*n+3)) + n*n/((2*n+1)*(2*n-1)) +(n+1)*(n+2)*r*r/((2*n+1)*(2*n+3))) - S.Rational(1,2))
a0=r; a1=A(S.Integer(1)); ai=(r+r**-1)/2
b0=r*r; b1=B(S.Integer(1)); bi=S.factor((3*ai*ai-1)/2)
den=(2*n-1)*(2*n+1)*(2*n+3)*(r*r+15)
w0=3*(n-1)*((10-2*r*r)*n+r*r+15)/den
w1=15*n*((2*n-1)*r*r+6*n+9)/den
wi=4*n*(n-1)*((2*n-1)*r*r+30*n+45)/den
checks=0
for e in [w0+w1+wi-1, w0*a0+w1*a1+wi*ai-A(n),w0*b0+w1*b1+wi*bi-B(n)]:
    assert S.factor(e)==0; checks+=1
# Independently reconstruct the coefficients by multiplication and Legendre recurrences.
A_rec=S.factor((n*r**(n-1)+(n+1)*r**(n+1))/((2*n+1)*r**n))
B_rec=S.factor(S.Rational(3,2)*(n*(n-1)*r**(n-2)/((2*n-1)*(2*n+1)*r**n) + ((n+1)**2/((2*n+1)*(2*n+3))+n*n/((2*n+1)*(2*n-1))) + (n+1)*(n+2)*r*r/((2*n+1)*(2*n+3)))-S.Rational(1,2))
assert S.factor(A_rec-A(n))==0;checks+=1
assert S.factor(B_rec-B(n))==0;checks+=1
for k in [0,1,2,3,4,7,12,31]:
    nk=S.Integer(k)
    if k==0: assert S.factor(A(nk)-a0)==0 and S.factor(B(nk)-b0)==0
    if k==1: assert S.factor(A(nk)-a1)==0 and S.factor(B(nk)-b1)==0
    if k>=2:
        assert S.factor((w0+w1+wi-1).subs(n,nk))==0
    checks+=1
assert S.limit(A(n),n,S.oo)==ai; checks+=1
assert S.factor(S.limit(B(n),n,S.oo)-bi)==0; checks+=1
assert S.factor(S.det(S.Matrix([[1,1,1],[a0,a1,ai],[b0,b1,bi]]))-(r*r-1)**2*(r*r+15)/(120*r**3))==0; checks+=1
p=S.solve([1+b*a0+c*b0,1+b*a1+c*b1],(b,c))
assert S.factor(p[b]+6/r)==0 and S.factor(p[c]-5/r**2)==0; checks+=2
q=S.solve([1+b*a1+c*b1,1+b*ai+c*bi],(b,c))
assert S.factor(q[b]+9*r*(3*r*r+5)/(6*r**4+31*r*r+15))==0;checks+=1
assert S.factor(q[c]-20*r*r/(6*r**4+31*r*r+15))==0;checks+=1
# Independent high-degree coefficient comparison by Gauss-Legendre quadrature.
xs, ws=leggauss(650)
for rv in (0.19,0.34,0.57,0.82):
    for bv,cv in ((0,0),(0.2,-0.3),(-0.7,1.9),(-6/rv,5/rv**2),(-9*rv*(3*rv**2+5)/(6*rv**4+31*rv**2+15),20*rv**2/(6*rv**4+31*rv**2+15))):
        K=(1-rv**2)/(1-2*rv*xs+rv**2)**1.5*(1+bv*xs+cv*(3*xs**2-1)/2)
        for j in range(10):
            actual=(2*j+1)*np.dot(ws,K*legval(xs,[0]*j+[1]))/2
            an=float(A(S.Integer(j)).subs(r,rv))
            bn=float(B(S.Integer(j)).subs(r,rv))
            expect=(2*j+1)*rv**j*(1+bv*an+cv*bn)
            assert abs(actual-expect)< 3e-8*max(1.0,abs(expect)),(rv,bv,cv,j,actual,expect)
            checks+=1
print(f'PASS: {checks} exact and independent numerical assertions')
