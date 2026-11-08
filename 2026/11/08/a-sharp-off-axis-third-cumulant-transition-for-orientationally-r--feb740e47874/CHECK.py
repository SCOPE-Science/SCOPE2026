#!/usr/bin/env python3
"""Checks for oblique third-cumulant transport in planar orientational resetting.
Requires Python 3 with sympy and mpmath. Run: python CHECK.py
This program checks identities and finite cases; the infinite-parameter proof is in RESULT.md.
"""
import sympy as S
import mpmath as M

r, d, v, c, s = S.symbols('r d v c s', positive=True)
a1, a2 = r+d, r+4*d
m = lambda n: r/(r+n*n*d)
V = (1+m(2))/2-m(1)**2
C12 = (m(1)+m(3))/2-m(1)*m(2)
A = 12*d**3*r*v**3*(67*d**2+191*d*r+52*r**2)/((r+d)**5*(r+4*d)**2*(r+9*d))
B = 12*d**2*r*v**3*(23*d+7*r)/((r+d)**3*(r+4*d)**2*(r+9*d))
checks=0
# Two independent Poisson-resolvent paths for cubic tensor components.
Kxxx_from_resolvent=6*v**3/a1*(C12/(2*a2)-2*m(1)*V/a1)
Kxyy_from_resolvent=2*v**3*(-C12/(2*a1*a2)+2/a1*((m(1)-m(3))/(4*a2)-m(1)*(1-m(2))/(2*a1)))
for residual in (Kxxx_from_resolvent+A,Kxyy_from_resolvent+B):
    assert S.cancel(residual)==0
    checks+=1
# The angular critical polynomial comes from A/B-2, with no positive denominators suppressed.
z=S.symbols('z',positive=True)
ratio=(67+191*z+52*z*z)/((1+z)**2*(23+7*z))
pol=14*z**3+22*z**2-85*z-21
assert S.cancel((ratio-2)+pol/((1+z)**2*(23+7*z)))==0
checks+=1
positive_root=[a for a in S.nroots(pol) if abs(S.im(a))<1e-12 and S.re(a)>0]
assert len(positive_root)==1
checks+=1
root=float(S.re(positive_root[0]))
assert 1.94<root<1.95
checks+=1
# An unrelated Fourier-matrix eigenvalue perturbation check at high precision.
M.mp.dps=48

def principal_eig(rr,dd,vv,xx,yy,k,N=4):
    ns=list(range(-N,N+1)); mat=M.matrix(len(ns)); p=N
    for j,n in enumerate(ns):
        if n:
            mat[j,j]=-(rr+dd*n*n)
            mat[p,j]+=rr
        if n<N:
            mat[j+1,j]+=k*vv*(xx-1j*yy)/2
        if n>-N:
            mat[j-1,j]+=k*vv*(xx+1j*yy)/2
    eig=M.eig(mat,left=False,right=False)
    return min(eig,key=lambda w: abs(w))

def eigen_third(rr,dd,vv,xx,yy):
    def diff(h):
        return M.re((principal_eig(rr,dd,vv,xx,yy,2*h)-2*principal_eig(rr,dd,vv,xx,yy,h)+2*principal_eig(rr,dd,vv,xx,yy,-h)-principal_eig(rr,dd,vv,xx,yy,-2*h))/(2*h**3))
    h=M.mpf('0.0004')
    return (4*diff(h/2)-diff(h))/3

for ir in ('0.2','0.8','1.5','3.0','10.0'):
    rr=M.mpf(ir); dd=M.mpf('1.3'); vv=M.mpf('2.1')
    for xs,ys in (('1','0'),('0','1'),('0.6','0.8')):
        xx=M.mpf(xs); yy=M.mpf(ys)
        aa=12*dd**3*rr*vv**3*(67*dd**2+191*dd*rr+52*rr**2)/((dd+rr)**5*(4*dd+rr)**2*(9*dd+rr))
        bb=12*dd**2*rr*vv**3*(23*dd+7*rr)/((dd+rr)**3*(4*dd+rr)**2*(9*dd+rr))
        expected=-aa*xx**3-3*bb*xx*yy**2
        observed=eigen_third(rr,dd,vv,xx,yy)
        assert abs(observed-expected)<M.mpf('0.00000003')*max(1,abs(expected)),(ir,xs,ys,observed,expected)
        checks+=1
# Global angular maximizer and critical boundary checks at rational rates.
for q in (S.Rational(1,8),S.Rational(1),S.Rational(2),S.Rational(3),S.Rational(20)):
    R=float(ratio.subs(z,q)); qb=float(q)
    if qb<root:
        assert R>2
        c2=1.0
    else:
        assert R<2
        c2=1/(3-R)
        assert 1/3 < c2 < 1
    # Differentiate cubic angular objective, and check its value vs the axis.
    C=c2**.5
    F=R*C**3+3*C*(1-C**2)
    assert F>=R-1e-12
    checks+=1
print('PASS',checks,'checks; critical ratio',format(root,'.14f'))
