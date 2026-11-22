"""Supplementary reproducibility checks of the periodic Gaussian ecological linear spectrum.
No finite sample establishes the all-parameter theorem; that follows from the written proof.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, pi, ceil
def brentq(f, a, b):
    """Sign-bracketed bisection on a continuous scalar function."""
    fa, fb = f(a), f(b)
    assert fa * fb < 0, (a, b, fa, fb)
    for _ in range(90):
        m = (a+b)/2
        fm = f(m)
        if fm == 0 or m == a or m == b:
            return m
        if fa*fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a+b)/2

# Example is reduced to lambda(k)/[C/458752] = 2039-458752*2^(-k*k)-127*k*k.
assert 2039-F(458752,2**9)-127*9==0
assert 2039-F(458752,2**16)-127*16==0
assert 2039-F(458752,2**10)-127*10==321
r=F(2039,458752)
alpha=r/(2*(1-r))
beta=(1-r)/2
u=F(1,2)
C=u*u/(u+alpha)
A=alpha*beta/(u+alpha)
D=C*F(127,458752)
sigma=log(2)
assert u*(1-u) == beta*(u+alpha)
assert A/C == r
assert D/C==F(127,458752)
assert F(0)<r<F(1)

def growth(k, diff=D):
    return float(A)-float(C)*exp(-sigma*k*k)-float(diff)*k*k

for multiple, sgn in [(0.3,-1),(0.6,1),(0.8,-1),(1.1,1),(1.4,-1),(1.7,1),(2.1,1)]:
    L=multiple*pi
    eigenvalues=[growth(2*pi*j/L) for j in range(31)]
    assert (max(eigenvalues)>0) == (sgn>0),(multiple,max(eigenvalues))
    assert max(eigenvalues[20:])<0

# General normalized Gaussian instability bands: use A=r,C=1,sigma=1.
# Critical ratio D_c and fold k_c, including near-onset gap divergence.
for q in [0.025,0.1,0.3,0.6,0.95]:
    fun=lambda t: t*(1-log(t))-q
    t=brentq(fun,1e-15,1-1e-12)
    Dc=t
    zc=log(1/t)
    assert abs(q-t*(1-log(t)))<1e-12
    for eps in [0.03,0.005,0.0005,0.00005]:
        if eps>=Dc:continue
        d=Dc-eps
        fun2=lambda z:q-exp(-z)-d*z
        zmax=log(1/d)
        zlo=brentq(fun2,0,zmax)
        zhi=brentq(fun2,zmax,q/d+1)
        klo,khi=sqrt(zlo),sqrt(zhi)
        rr=klo/(khi-klo)
        count=max(0,ceil(rr)-1)
        for j in range(1,min(count+3,120)):
            has_gap=(j<rr)
            assert has_gap == (j/klo < (j+1)/khi)
        if eps<=0.00005:
            prediction=sqrt(Dc*zc/(2*eps))
            assert abs(rr/prediction-1)<0.05,(q,rr,prediction)
        assert klo<sqrt(zc)<khi if eps<0.03 else klo<khi
print('PASS: exact rational roots, ecological admissibility, finite ring modes, critical diffusion bands, gap count, and near-fold asymptotics')
