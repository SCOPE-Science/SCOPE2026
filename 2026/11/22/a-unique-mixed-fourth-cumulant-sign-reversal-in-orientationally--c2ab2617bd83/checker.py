"""Standalone exact and spectral checks for a planar swimmer's mixed fourth cumulant.
Run: python orientation_mixed_checker.py. Dependencies: sympy, numpy.
"""
import math
import sympy as S
import numpy as np
q=S.symbols('q', positive=True)
u,w=S.symbols('u w', real=True)
P=461*q**5+6696*q**4+28515*q**3+30686*q**2-26586*q-9072
DEN=(q+1)**5*(q+4)**3*(q+9)**2*(q+16)
KXY=16*P/DEN
checks=0

def demand(x, desc):
    global checks
    assert bool(x), desc
    checks+=1

# A backward-eigenfunction bivariate Fourier expansion; all Laurent frequencies |n|<=4.
co=[{0:S.Integer(1)}]; L=[S.Integer(0)]
def vprod(c,n):
    return (u*(c.get(n-1,0)+c.get(n+1,0))+w*(c.get(n-1,0)-c.get(n+1,0))/S.I)/2
for d in range(1,5):
    cd={}
    for n in range(-d,d+1):
        if n==0:continue
        term=vprod(co[d-1],n)
        for j in range(1,d):term-=L[j]*co[d-j].get(n,0)
        cd[n]=S.cancel(term/(q+n*n))
    cd[0]=-sum(cd.values()); co.append(cd)
    term=q*sum(x for n,x in cd.items() if n!=0)+vprod(co[d-1],0)
    for j in range(1,d):term-=L[j]*co[d-j].get(0,0)
    L.append(S.factor(term))
    demand(S.expand(sum(cd.values()))==0,'normalized eigenfunction')
demand(S.factor(S.diff(L[4],u,2,w,2)-KXY)==0,'bivariate exact fourth cumulant')
demand(S.factor(S.diff(L[1],u)-q/(q+1))==0,'mean propulsion')
demand(S.factor(S.diff(L[2],u,2)-2*(2+5*q)/((q+1)**3*(q+4)))==0,'longitudinal diffusion check')
demand(S.factor(S.diff(L[2],w,2)-4/((q+1)*(q+4)))==0,'transverse diffusion check')

def projected_k4(a,b):
    """Independent one-variable angle-projection eigenvalue construction."""
    hi=(a-S.I*b)/2; lo=(a+S.I*b)/2
    c=[{0:S.Integer(1)}]; eig=[S.Integer(0)]
    for m in range(1,5):
        cc={}
        for n in range(-m,m+1):
            if n==0:continue
            t=hi*c[m-1].get(n-1,0)+lo*c[m-1].get(n+1,0)
            for j in range(1,m):t-=eig[j]*c[m-j].get(n,0)
            cc[n]=S.cancel(t/(q+n*n))
        cc[0]=-sum(cc.values());c.append(cc)
        t=q*sum(v for n,v in cc.items() if n)
        t+=hi*c[m-1].get(-1,0)+lo*c[m-1].get(1,0)
        for j in range(1,m):t-=eig[j]*c[m-j].get(0,0)
        eig.append(S.factor(t))
    return S.factor(24*eig[4])

kx=projected_k4(S.Integer(1),S.Integer(0))
ky=projected_k4(S.Integer(0),S.Integer(1))
kdiag=projected_k4(1/S.sqrt(2),1/S.sqrt(2))
demand(S.factor((4*kdiag-kx-ky)/6-KXY)==0,'independent projection polarization identity')
demand(S.factor(S.diff(L[4],u,4)-kx)==0,'x fourth identity')
demand(S.factor(S.diff(L[4],w,4)-ky)==0,'y fourth identity')
# Descartes gives one positive zero, and the exact rational brackets locate it.
coeff=S.Poly(P,q).all_coeffs()
demand(sum((a>0)!=(b>0) for a,b in zip(coeff,coeff[1:]))==1,'single Descartes sign change')
demand(P.subs(q,S.Rational(71687,100000))<0,'lower root bracket')
demand(P.subs(q,S.Rational(71688,100000))>0,'upper root bracket')
demand(S.limit(KXY,q,0)==S.Rational(-7,4),'slow reset boundary')
demand(S.limit(KXY*q**6,q,S.oo)==S.Integer(7376),'fast reset boundary')
for qq in [S.Rational(1,10),S.Rational(1,2),S.Rational(1),S.Rational(2),S.Rational(10)]:
    demand(S.sign(KXY.subs(q,qq))==(-1 if qq < S.Rational(71687,100000) else 1),'sample signs')

# Independently check analytic Taylor coefficient by a complex-Cauchy grid
# of the leading eigenvalue of the finite Fourier Galerkin generator.
# This is a numerical check, not a proof by angular truncation.
def numerical_kxy(Q,N=9,M=10,radius=0.035):
    ns=np.arange(-N,N+1)
    base=np.zeros((len(ns),len(ns)),dtype=complex)
    for j,n in enumerate(ns):
        if n:
            base[j,j]=-Q-n*n
            base[N,j]=Q
    theta=np.arange(M)*2*np.pi/M
    zz=radius*np.exp(1j*theta)
    out=0j
    for ia,a in enumerate(zz):
        for ib,b in enumerate(zz):
            op=base.copy()
            hp=(a-1j*b)/2;hm=(a+1j*b)/2
            for col in range(len(ns)):
                if col+1<len(ns):op[col+1,col]+=hp
                if col-1>=0:op[col-1,col]+=hm
            ev=np.linalg.eigvals(op)
            val=ev[np.argmin(abs(ev))]
            out+=val*np.exp(-2j*(theta[ia]+theta[ib]))
    return (4*out/(M*M*radius**4)).real
for Q in [0.2,0.6,0.8,1.0,3.0]:
    predicted=float(KXY.subs(q,S.Rational(str(Q))))
    measured=numerical_kxy(Q)
    demand(abs(predicted-measured)<1e-5*max(1,abs(predicted)),f'independent spectral check {Q}: {predicted} vs {measured}')

print(f'PASS {checks} checks; single positive zero at 0.716876436691030...')
print('mixed fourth cumulant slope:',S.factor(KXY))
