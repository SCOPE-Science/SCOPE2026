"""Reproduce the exact polynomial and interval certificates for two sensor modalities.

Run: python verification.py
Requires SymPy, SciPy and NumPy.
"""
from __future__ import annotations
from math import comb
import sympy as sp

s,t,z,eta=sp.symbols('s t z eta',real=True)
Q=sp.Rational

# A standard Brownian bridge has covariance min(u,v)-u*v.
# The time-integrated bridge has covariance below for s <= t and s >= t.
Cp_lo=s**2*(3*t-s)/6-s**2*t**2/4
Cp_hi=t**2*(3*s-t)/6-s**2*t**2/4
# Its cross-covariance with B(t) for s <= t and s >= t:
Cv_lo=s**2*(1-t)/2
Cv_hi=t*s-t**2/2-t*s**2/2

Jp=sp.factor(sp.integrate(Cp_lo**2,(s,0,t))+sp.integrate(Cp_hi**2,(s,t,1)))
Jv=sp.factor(sp.integrate(Cv_lo**2,(s,0,t))+sp.integrate(Cv_hi**2,(s,t,1)))
Vp=t**3*(4-3*t)/12
Vv=t*(1-t)
assert sp.simplify(Jp+t**4*(7*t**4+8*t**3-140*t**2+280*t-168)/5040)==0
assert sp.simplify(Jv-t**2*(1-t)**2*(8-4*t-t**2)/60)==0
assert sp.integrate(Vp,(t,0,1)) == Q(1,30)
assert sp.simplify(sp.diff(Vp,t)-t*t*(1-t))==0

A=2016-2184*t+336*t**2+168*t**3
B=21*t**4+4*t**3-238*t**2+392*t-168
D=sp.factor(sp.diff(Jp,t)*(Vp+eta)-Jp*sp.diff(Vp,t))
assert sp.simplify(D-t**3*(1-t)*(eta*A-t**3*B)/15120)==0
assert A.subs(t,1)==336 and B.subs(t,1)==11
assert sp.factor(sp.diff(A,t).subs(t,1))==-1008
assert sp.factor(sp.diff(B,t).subs(t,1))==12
assert sp.factor(sp.diff(B,t,2).subs(t,1))==-200
assert sp.Poly(B,t).count_roots(Q(74,100),Q(75,100))==1

b=4*t**3+9*t**2-24*t+8
jvr=sp.factor(Jv/Vv)
assert sp.simplify(sp.diff(jvr,t)-b/60)==0
assert sp.simplify(sp.diff(Jv,t)-t*(1-t)*(3*t-4)*(t**2+4*t-2)/30)==0
assert sp.Poly(b,t).count_roots(Q(2,5),Q(45,100))==1
assert b.subs(t,Q(2,5))>0 and b.subs(t,Q(1,2))<0
assert sp.simplify(b.subs(t,sp.sqrt(6)-2))<0

# The velocity optimum at eta_p lies strictly between 41/100 and 42/100.
eta_p=Q(11,336)
Dv=sp.factor(sp.diff(Jv,t)*(Vv+eta)-Jv*sp.diff(Vv,t))
assert Dv.subs({t:Q(41,100),eta:eta_p})>0
assert Dv.subs({t:Q(42,100),eta:eta_p})<0
assert (Jv.subs(t,Q(42,100))/(eta_p+Vv.subs(t,Q(41,100)))) < Q(1,45)
assert sp.factor((Jp.subs(t,1)/(eta_p+Vp.subs(t,1)))) == Q(1,45)
assert Jp.subs(t,Q(3,4))/Vp.subs(t,Q(3,4)) > Q(13,500)
assert Jv.subs(t,Q(2,5)) > Jp.subs(t,1)
# Strict opposite modality preference at eta = 1/25, past the endpoint threshold.
eta_hi=Q(1,25)
assert Jv.subs(t,Q(5,12))/(eta_hi+Vv.subs(t,Q(5,12))) > Jp.subs(t,1)/(eta_hi+Vp.subs(t,1))
assert Dv.subs({t:Q(42,100),eta:eta_hi})<0

# Eliminate eta from the velocity first-order condition and equality
# with the position endpoint's gain.
A0=sp.factor(Jp.subs(t,1));V0=sp.factor(Vp.subs(t,1))
eta_equal=sp.factor((Jv*V0-A0*Vv)/(A0-Jv))
eta_stat=sp.factor(Jv*sp.diff(Vv,t)/sp.diff(Jv,t)-Vv)
P=336*t**7+84*t**6-3150*t**5+5530*t**4-3780*t**3+1092*t**2-138*t+13
num=sp.together(eta_equal-eta_stat).as_numer_denom()[0]
assert sp.rem(num,P,t)==0
assert sp.Poly(P,t).count_roots(Q(41,100),Q(42,100))==1
assert P.subs(t,Q(41,100))>0 and P.subs(t,Q(42,100))<0

# Exact Bernstein certificate: P'(t)<-52 on the interval [0.41,0.42].
f=sp.expand(sp.diff(P,t).subs(t,Q(41,100)+z/100))
coeff=[f.coeff(z,k) for k in range(7)]
bern=[sp.factor(sum(coeff[k]*Q(comb(i,k),comb(6,k)) for k in range(i+1))) for i in range(7)]
assert all(Q(-53)<q<Q(-52) for q in bern)

# The prior derivative sign certificate makes this a complete root enclosure.
lo=Q('0.41546852003567848322183923811836')
hi=Q('0.41546852003567848322183923811838')
assert Q(41,100)<lo<hi<Q(42,100)
assert P.subs(t,lo)>0>P.subs(t,hi)
# Jv and Vv are increasing throughout the interval. Use positive numerator
# and denominator bounds for (A0*Vv−V0*Jv)/(Jv−A0).
jlo,jhi=Jv.subs(t,lo),Jv.subs(t,hi)
vlo,vhi=Vv.subs(t,lo),Vv.subs(t,hi)
assert jlo>A0 and A0*vlo>V0*jhi
elo=(A0*vlo-V0*jhi)/(jhi-A0)
ehi=(A0*vhi-V0*jlo)/(jlo-A0)
e_print_lo=Q('0.03486395077318212468')
e_print_hi=Q('0.03486395077318212469')
assert e_print_lo<elo<ehi<e_print_hi
etastar=float((elo+ehi)/2)
assert float(eta_p)< etastar < float(eta_hi)
assert 0.03486 < etastar < 0.03487
print('Exact formulas, monotonicity boundaries, endpoint comparison: PASS')
print('Bernstein bound of P derivative on [0.41,0.42]:',float(min(bern)),float(max(bern)))
print('Crossing time:', sp.N((lo+hi)/2,28))
print('Crossing noise lies between', sp.N(e_print_lo,19), 'and', sp.N(e_print_hi,19))

# Independent numerical quadrature of the original kernels and selected optima.
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
import numpy as np

def cp(sval,tval):
    return float(Cp_lo.subs({s:sval,t:tval})) if sval<=tval else float(Cp_hi.subs({s:sval,t:tval}))
def cv(sval,tval):
    return float(Cv_lo.subs({s:sval,t:tval})) if sval<=tval else float(Cv_hi.subs({s:sval,t:tval}))
fp=sp.lambdify(t,Jp,'numpy');fv=sp.lambdify(t,Jv,'numpy')
vp=sp.lambdify(t,Vp,'numpy');vv=sp.lambdify(t,Vv,'numpy')

points=[Q(i,17) for i in range(1,17)]
for rat in points:
    ti=float(rat)
    for fun,f in [(cp,fp),(cv,fv)]:
        j=quad(lambda u:fun(u,ti)**2,0,ti,epsabs=2e-12)[0]+quad(lambda u:fun(u,ti)**2,ti,1,epsabs=2e-12)[0]
        assert abs(j-f(ti)) < 1e-12
print('32 independent covariance-integral quadrature checks: PASS')
for noise in [1e-6,1e-3,eta_p-0.0001,float(eta_p),0.033,etastar,0.04,0.1,1.,100.]:
    ep=float(noise)
    op=minimize_scalar(lambda v:-fp(v)/(vp(v)+ep),bounds=(1e-10,1),method='bounded',options={'xatol':1e-13})
    ov=minimize_scalar(lambda v:-fv(v)/(vv(v)+ep),bounds=(0.4,0.45),method='bounded',options={'xatol':1e-13})
    pgain=max(-op.fun,fp(1)/(vp(1)+ep))
    vgain=-ov.fun
    if ep<etastar-2e-9: assert pgain>vgain
    if ep>etastar+2e-9: assert vgain>pgain
    assert 0.4<ov.x<0.45
print('10 global modality comparisons and velocity localization: PASS')
print('ALL CHECKS PASS')
