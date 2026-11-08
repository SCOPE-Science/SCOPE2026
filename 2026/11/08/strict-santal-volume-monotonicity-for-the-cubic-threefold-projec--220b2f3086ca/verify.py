#!/usr/bin/env python3
"""Independent exact and quadrature checks for the cubic support-body volume product.
Scientific formulae and proof are given in RESULT.md; this is supplementary evidence.
Requires only Python 3 standard library.
"""
from fractions import Fraction
from math import cos, sin, sqrt, pi


def odd_double_factorial(n):
    t=1
    for j in range(1,n+1,2):t*=j
    return t

def a(k):
    # Coefficient of s^k in E(1+sqrt(s)*XYZ)^(-3)
    return Fraction((k+1)*(2*k+1)*odd_double_factorial(2*k-1)**3,
                    odd_double_factorial(6*k+1))

for k in range(1,121):
    r = Fraction((k+1)*(2*k+1)*(2*k-1)**2,
                k*(6*k-3)*(6*k-1)*(6*k+1))
    assert a(k)/a(k-1)==r
    assert 7*a(k) < a(k-1)
assert a(0)==1
assert a(1)==Fraction(2,35)
assert a(2)==Fraction(3,1001)
assert a(1)-a(0)/7==-Fraction(3,35)
assert a(2)-a(1)/7==-Fraction(181,35035)

# Independent Gauss-Legendre quadrature for both primal support volume and polar integral.
def gauss_legendre(n):
    out=[]
    for i in range(1,n+1):
        z=cos(pi*(i-.25)/(n+.5))
        for _ in range(25):
            p0,p1=1.,z
            for j in range(2,n+1):p0,p1=p1,((2*j-1)*z*p1-(j-1)*p0)/j
            if n==1:p1=z;p0=1.
            pp=n*(z*p1-p0)/(z*z-1)
            new=z-p1/pp
            if abs(new-z)<2e-15:break
            z=new
        w=2/((1-z*z)*pp*pp)
        out.append((z,w))
    return out

def hessian_bilinear(v,w,x,y,z):
    return z*(v[0]*w[1]+v[1]*w[0])+y*(v[0]*w[2]+v[2]*w[0])+x*(v[1]*w[2]+v[2]*w[1])

def volumes(eps,n=64,m=240):
    primal=polar=0.
    for z,w in gauss_legendre(n):
        rr=sqrt(1-z*z)
        for j in range(m):
            phi=2*pi*j/m;c=cos(phi);s=sin(phi)
            x,y=rr*c,rr*s
            f=x*y*z
            e=(-s,c,0.);v=(-z*c,-z*s,rr)
            q11=hessian_bilinear(e,e,x,y,z)-2*f
            q22=hessian_bilinear(v,v,x,y,z)-2*f
            q12=hessian_bilinear(e,v,x,y,z)
            det=1+eps*(q11+q22)+eps**2*(q11*q22-q12*q12)
            primal+=w*(1+eps*f)*det
            polar+=w/(1+eps*f)**3
    weight=2*pi/(3*m)
    return primal*weight,polar*weight

vball=4*pi/3
for eps in (0.,.2,.5,.8):
    v,p=volumes(eps)
    assert abs(v/vball - (1-eps**2/7))<1e-10,(eps,v/vball)
    s=eps*eps
    mseries=sum(float(a(k))*s**k for k in range(25))
    assert abs(p/vball-mseries)<1e-10,(eps,p/vball,mseries)
    assert v*p<=vball**2*(1-Fraction(3,35)*s)+1e-10
    print('eps=',eps,'V=',format(v,'.12f'),'Vpolar=',format(p,'.12f'),'normalized Mahler=',format(v*p/vball**2,'.12f'))
print('PASS: 120 exact coefficient inequalities, 120 exact ratio identities, 4 independent 2-volume quadratures, sharp coefficients')
