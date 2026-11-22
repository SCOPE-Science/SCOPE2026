#!/usr/bin/env python3
"""Supplementary algebraic and high precision tests of the near-infinity theorem.
All constants and equations are public mathematical definitions.
Requires sympy, mpmath.
"""
import sympy as s
import mpmath as mp

k, m, u=s.symbols('k m u', positive=True)
z=1/(1+m*m)
X=z*(1+k)/k
Y=z*(1+k)
B=X*X+Y*Y-X*Y
H=s.factor(X*Y/B)
beta=2*m*z
c=s.factor(H*(2*m*(X*X-Y*Y)-beta*(X-Y))/B)
ctr=2*k*m*(1-k)*(k*k+k+1)/((1+k)*(k*k-k+1)**2)
assert s.simplify(c-ctr)==0
K=2*(1+k)*(k*k-k+1)/(k*(1-k))
trace1=s.factor(-c*(1/k+k*k)-2*m*H*k*k-beta*(1+k)*(1-H*k)/X)
lprime=s.factor((trace1+2*m*k)/(1-k))
assert s.simplify(lprime+2*m*(k*k+k+1)/(k*k-k+1))==0
assert s.simplify(-2*lprime/c-K)==0
Ax=s.factor(X*c)
Ay=s.factor(Y*c)
assert s.simplify(Ax-2*m*(1-k)*(k*k+k+1)/((1+m*m)*(1-k+k*k)**2))==0
assert s.simplify(Ay-k*Ax)==0
print('Symbolic derivative and sharp constants: PASS')

mp.mp.dps=85
for mm in ['0.3','1','2']:
    mu=mp.mpf(mm); kk=mp.e**(-mp.pi*mu); zz=1/(1+mu**2); bet=2*mu*zz
    HH=kk/(1-kk+kk**2)
    cc=2*kk*mu*(1-kk)*(kk**2+kk+1)/((1+kk)*(1-kk+kk**2)**2)
    AA=2*mu*(1-kk)*(kk**2+kk+1)/((1+mu**2)*(1-kk+kk**2)**2)
    KK=2*(1+kk)*(1-kk+kk**2)/(kk*(1-kk))
    def vals(eps):
        t=mp.pi+eps
        yy=zz*((mp.cos(t)-mp.e**(-mu*t))/mp.sin(t)-mu)
        xx=zz*(mu-(mp.e**(mu*t)-mp.cos(t))/mp.sin(t))
        ee=mp.e**(-2*mu*t)
        hh=(xx*yy+zz)/(xx*xx+yy*yy-xx*yy-bet*(xx-yy)+zz)
        rho=yy/xx
        q=xx**2-bet*xx+zz
        tr=hh*(rho/ee+ee)-bet*(1+rho)*(xx-hh*yy)/q
        lam=(tr+mp.sqrt(tr**2-4*rho))/2
        return xx,yy,hh,lam*lam,2*t
    for ex in ['0.0001','0.00001','0.000001']:
        e=mp.mpf(ex)
        xx,yy,hh,M,T=vals(e)
        delta=HH-hh
        assert delta>0
        rel=[abs(delta*xx/AA-1),abs(delta*yy/(kk*AA)-1),abs((1-M)/(KK*delta)-1),abs((T-2*mp.pi)/(2*delta/cc)-1)]
        assert max(rel)<mp.mpf('0.025'), (mm,ex,rel)
        if ex=='0.000001': print('mu',mm,'asymptotic normalized error',*[mp.nstr(v,9) for v in rel])
print('High-precision amplitude/period/Floquet critical tests: PASS')

# Full limiting cycle geometry: the homogeneous upper flight closes under S.
# Compare the affine orbit at a nearby parameter with the rescaled profile.
for mm in ['0.3','1','2']:
    mu=mp.mpf(mm); kk=mp.e**(-mp.pi*mu); zz=1/(1+mu**2)
    Hs=kk/(1-kk+kk**2)
    AA=2*mu*(1-kk)*(kk**2+kk+1)/((1+mu**2)*(1-kk+kk**2)**2)
    P=mp.matrix([AA, kk*AA, 0])
    S=mp.matrix([[0,-1,0],[-1,0,0],[0,0,-1]])
    def Amat(h):
        return mp.matrix([[-2*mu,0,-h*(9*mu**2+1)], [0,2*mu,-(1+mu**2)], [0,1,0]])
    A0=Amat(Hs)
    target=mp.expm(A0*mp.pi)*P
    assert max(abs(target[i]-(S*P)[i]) for i in range(3))<mp.mpf('1e-60')
    for theta in [mp.mpf('.2'),mp.mpf('.5'),mp.mpf('.8')]:
        u=mp.mpf('0.0000001')
        t=mp.pi+u
        x=zz*(mu-(mp.e**(mu*t)-mp.cos(t))/mp.sin(t))
        y=zz*((mp.cos(t)-mp.e**(-mu*t))/mp.sin(t)-mu)
        hh=(x*y+zz)/(x*x+y*y-x*y-(2*mu*zz)*(x-y)+zz)
        d=Hs-hh
        # Exact affine solution via augmented homogeneous 4x4 matrix exponential.
        AA4=mp.matrix([[ -2*mu,0,-hh*(9*mu**2+1),hh], [0,2*mu,-(1+mu**2),1], [0,1,0,0], [0,0,0,0]])
        p=mp.expm(AA4*t*theta)*mp.matrix([x,y,0,1])
        q=mp.expm(A0*mp.pi*theta)*P
        assert max(abs(d*p[i]-q[i]) for i in range(3))<mp.mpf('0.000003'), (mm,theta)
print('Normalized periodic profile and homogeneous closure: PASS')
