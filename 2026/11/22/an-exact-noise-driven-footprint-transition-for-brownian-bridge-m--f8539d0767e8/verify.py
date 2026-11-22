"""Exact and numerical checks for a Brownian-bridge fixed-window sensing theorem.

Run: python verify.py
Requires Python 3, sympy, numpy, scipy.
These checks supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
import math
import numpy as np
import sympy as S
from scipy.optimize import minimize_scalar, brentq
from numpy.polynomial.legendre import leggauss

z,h,e,c=S.symbols('z h e c', real=True)
L=h*(2-h)/4
alpha=e-h/S.Integer(6)
F=(1-4*z)*(4*z-h*h)**2/(z+alpha)
N=8*(1-4*z)*(z+alpha)-4*(4*z-h*h)*(z+alpha)-(1-4*z)*(4*z-h*h)
assert S.simplify(S.diff(F,z)-((4*z-h*h)*N/(z+alpha)**2))==0
assert S.simplify(N.subs(z,L)-2*(1-h)/3*(12*e*(1-2*h)+h*(3*h*h-5*h+1)))==0
assert S.simplify(N.subs(z,S.Rational(1,4))+(1-h*h)*(12*e+3-2*h)/3)==0
assert S.simplify(S.diff(N,z).subs(z,L)-4*(1-6*h+4*h*h-12*e))==0
assert S.simplify(S.diff(N,z,2)+64)==0
p=c*(1-c)
G=(2*c-1)*(4*p-h*h)/24
V=p-h/6
assert S.simplify(G**2-(1-4*p)*(4*p-h*h)**2/576)==0
x=S.symbols('x',real=True)
g=x*(1-x)*(2*x-1)/6
assert S.integrate((2*x-1)*g,(x,0,1))==S.Rational(1,180)
assert S.simplify(S.integrate(g,(x,c-h/2,c+h/2))/h-G)==0
# Independent direct covariance checks using Gauss-Legendre integration of kernel.
nodes,wts=leggauss(320)
xs=(nodes+1)/2
ws=wts/2
K=lambda s,t: np.minimum(s,t)-s*t
checks=0
for hf,cf in [(.1,.12),(.1,.3),(.25,.125),(.3,.18),(.4,.2),(.6,.35),(.8,.4)]:
    l, r=cf-hf/2,cf+hf/2
    xx=l+(xs*hf);ww=ws
    # Direct covariance target with window, integrate target coordinate over whole interval
    # The integrand has a K-kink, so finite-resolution error is O(n^-2).
    directG=float(np.sum(((2*xs[:,None]-1)*ws[:,None])*K(xs[:,None],xx[None,:])*ww[None,:]))
    directV=float(np.sum((ww[:,None]*ww[None,:])*K(xx[:,None],xx[None,:])))
    analyticG=float(G.subs({h:hf,c:cf}));analyticV=float(V.subs({h:hf,c:cf}))
    assert abs(directG-analyticG)<1.5e-5,(hf,cf,'G',directG,analyticG)
    assert abs(directV-analyticV)<2.5e-6,(hf,cf,'V',directV,analyticV)
    checks+=2

h0=float((5-S.sqrt(13))/6)
def info(q, length, noise):
    zq=q*(1-q)
    cov=(2*q-1)*(4*zq-length**2)/24
    return cov**2/(zq-length/6+noise)

def Nnum(zz, hh, eta):
    aa=eta-hh/6
    return 8*(1-4*zz)*(zz+aa)-4*(4*zz-hh*hh)*(zz+aa)-(1-4*zz)*(4*zz-hh*hh)

def analytic_location(hh,eta):
    low=hh*(2-hh)/4
    if Nnum(low,hh,eta)<=0: return hh/2
    upper=.25
    zz=brentq(lambda v:Nnum(v,hh,eta),low,upper,xtol=5e-16)
    return (1-math.sqrt(1-4*zz))/2

for hh in [.03,.1,.2,h0,.24,.3,.4,.499,.5,.6,.8,.97]:
    for eta in [0.,1e-8,.0001,.003,.02,.09,.3,1.,20.,1e3]:
        xbest=analytic_location(hh,eta)
        assert hh/2-1e-12 <= xbest <.5
        fv=info(xbest,hh,eta)
        grid=np.linspace(hh/2,.5,1001)
        values=np.array([info(float(t),hh,eta) for t in grid])
        assert fv+2e-14>=values.max(),(hh,eta,xbest,fv,values.max())
        # Direct bounded optimizer checks (not proof of uniqueness)
        m=minimize_scalar(lambda q:-info(q,hh,eta),bounds=(hh/2,.5),method='bounded',options={'xatol':1e-12})
        assert fv +2e-14 >= info(m.x,hh,eta)
        if hh<h0-1e-8:
            assert xbest>hh/2
        if hh>=.5:
            assert abs(xbest-hh/2)<1e-12
        if h0+1e-8<hh<.5:
            etac=hh*(5*hh-3*hh*hh-1)/(12*(1-2*hh))
            if eta>etac+1e-10: assert xbest>hh/2
            elif eta<etac-1e-10:assert abs(xbest-hh/2)<1e-12
        checks+=2
# Asymptotic optimal location at very high noise for sub-half windows
for hh in [.05,.2,.3,.4,.49]:
    xbest=analytic_location(hh,1e6)
    limit=(1-math.sqrt((1-hh*hh)/3))/2
    assert abs(xbest-limit)<3e-7,(hh,xbest,limit)
    checks+=1
print('PASS symbolic covariance/derivative identities; exact prior target variance;')
print(f'PASS {checks} independent integral comparisons, optimizer and phase tests')
print(f'h0={(5-math.sqrt(13))/6:.12f}')
for hh in [.1,.25,.3,.4,.6]:
    for eta in [0.,.02,.2,10.]:
        t=analytic_location(hh,eta)
        gain=(info(t,hh,eta)/info(hh/2,hh,eta)-1)*100
        print(f'h={hh:.2f}, eta={eta:6.2f}: t_left={t:.10f}, information gain over endpoint={gain:.5f}%')
