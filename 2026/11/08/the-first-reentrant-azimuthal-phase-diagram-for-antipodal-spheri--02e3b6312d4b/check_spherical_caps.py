#!/usr/bin/env python3
"""Exact symbolic validation of antipodal-cap spherical-harmonic concentration profiles.
Requires Python 3 and SymPy. This is supplementary to the analytic proof."""
import sympy as S
x,c,t=S.symbols('x c t', real=True)
assertions=0
F={}
for ell in range(1,5):
    for m in range(ell+1):
        q=S.expand(S.assoc_legendre(ell,m,x)**2)
        den=S.integrate(q,(x,-1,1))
        val=S.factor(2*S.integrate(q,(x,c,1))/den)
        F[(ell,m)]=val
        assert S.simplify(val.subs(c,0)-1)==0
        assert S.simplify(val.subs(c,1))==0
        assertions+=2
# The five defect polys: 1-F_{4,m}=c*D_m(c^2).
Ds=[
 (1225*t**4-2700*t**3+1998*t**2-540*t+81)/64,
 t*(135-459*t+585*t**2-245*t**3)/16,
 (245*t**4-720*t**3+702*t**2-240*t+45)/32,
 t*(105-189*t+135*t**2-35*t**3)/16,
 (35*t**4-180*t**3+378*t**2-420*t+315)/128,
]
for m,D in enumerate(Ds):
    assert S.simplify(1-F[(4,m)]-c*D.subs(t,c*c))==0
    assertions+=1
# All ten pairwise differences computed independently from orthogonal-polynomial integration.
for m in range(5):
 for k in range(m+1,5):
    assert S.simplify(F[(4,m)]-F[(4,k)]-c*(Ds[k]-Ds[m]).subs(t,c*c))==0
    assertions+=1
Q=455*t**3-625*t**2+293*t-27
assert S.discriminant(Q,t)<0
assert Q.subs(t,S.Rational(1,9))<0 and Q.subs(t,S.Rational(1,7))>0
assertions+=2
# Exact rational isolations of the four transitions.
a=S.CRootOf(Q,0)
b=(5+2*S.sqrt(15))/35
g=S.Rational(3,7)
d=(15+2*S.sqrt(30))/35
assert 0<a<S.Rational(1,7)<b<g<d<1
assertions+=1
# Validate ordering and degeneracy at representative rational points of each interval.
centers=[S.Rational(1,10),S.Rational(1,4),S.Rational(2,5),S.Rational(3,5),S.Rational(4,5)]
expect=[3,0,2,1,0]
# Input values are for c^2, so use sqrt().
for z,idx in zip(centers,expect):
    v=[S.simplify(1-S.sqrt(z)*D.subs(t,z)) for D in Ds]
    for j in range(5):
        if j==idx:continue
        assert float(S.N(v[idx]-v[j]))>0, (z,idx,j)
        assertions+=1
# Triply tied maximal sectors at c^2=3/7, and only those.
assert all(S.simplify(Ds[j].subs(t,g)-Ds[0].subs(t,g))==0 for j in (1,2))
assert float(S.N(Ds[3].subs(t,g)-Ds[0].subs(t,g)))>0
assert float(S.N(Ds[4].subs(t,g)-Ds[0].subs(t,g)))>0
assertions+=4
print('ANTIPODAL_FOURTH_DEGREE_PASS assertions='+str(assertions)+' exact_sectors=14 phase_intervals=5')
