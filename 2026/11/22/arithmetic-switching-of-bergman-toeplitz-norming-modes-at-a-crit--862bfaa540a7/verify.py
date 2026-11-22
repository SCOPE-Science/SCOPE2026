#!/usr/bin/env python3
"""Standalone symbolic and exact-rational checks for the critical-window theorem.

Requires Python 3 and SymPy. Symbolic checks verify algebra, not novelty or
independent mathematical validation. No network or data files are required.
"""
from fractions import Fraction
from math import floor
import sympy as S

m,n,k,r,b,ell,u=S.symbols('m n k r b ell u',real=True)
d=m-n
W=(k+1)*(k+d+1)/(k+m+1)**2
F=(k+1)*d*(k*(m+n)+m**2+m+n**2+n)/((k+m+1)**2*(k+n+1)**2)
assert S.factor(W-W.subs(k,k-d)-F)==0
assert S.factor(F.subs(k,d-1)-2*d**2/(2*m-n)**2)==0
Q=6*r**3-13*r**2+6*r-1
G=-(r-1)**2*(13*r**2-1)/(2*r**3*(2*r-1)**3)
L=-(r-1)*(18*r**2-26*r+6)/(r**2*(2*r-1)**3)
D=S.factor(F.subs(k,d-1+ell)-F.subs(k,d-1))
expr=S.cancel(D.subs({m:r/u+b,n:1/u}))
series=S.series(expr,u,0,3).removeO().expand()
c1=S.factor(series.coeff(u,1))
c2=S.factor(series.coeff(u,2))
assert S.factor(c1 + ell*(r-1)*Q/(r**2*(2*r-1)**3))==0
num=S.together(c2-(G*ell**2+L*b*ell)).as_numer_denom()[0]
assert S.rem(num,Q,r)==0
rho=float(S.nroots(Q,n=35,maxsteps=200)[0])
g=float(G.subs(r,rho)); lam=float(L.subs(r,rho));theta=g/lam
assert -0.134<g< -0.132 and -0.233<lam< -0.231
assert 0.573<theta<0.575 and 4*g-2*lam < -0.068

def eig(mm,nn,jj):
    dd=mm-nn
    if jj<dd:
        return Fraction((jj+1)*(jj+dd+1),(jj+mm+1)**2)
    return Fraction((jj+1)*dd*(jj*(mm+nn)+mm*mm+mm+nn*nn+nn),
                    (jj+mm+1)**2*(jj+nn+1)**2)

for nn in [70,100,101,133,200,300,501,1000,3000,5000]:
    mm=floor(rho*nn)
    dd=mm-nn
    vals=[eig(mm,nn,j) for j in range(0,dd+40)]
    actual=max(range(len(vals)),key=vals.__getitem__)
    assert actual in (dd-1,dd),(nn,mm,actual,dd)
    frac=rho*nn-mm
    if abs(frac-theta)>0.04 and nn>=1000:
        assert actual==(dd if frac>theta else dd-1)
    delta=float((eig(mm,nn,dd)-eig(mm,nn,dd-1))*nn**2)
    assert abs(delta-(g-lam*frac))<8/nn, (nn,delta,g-lam*frac)
print('PASS: exact weighted-shift and symbolic asymptotic identities;')
print('PASS: critical algebraic signs, exact-rational finite samples and lattice candidates')
