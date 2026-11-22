"""Exact-state generator verification for a two-bee recruitment/service chain.
Run: python verify.py (requires sympy).
"""
from fractions import Fraction
import sympy as sp

u,v,z = sp.symbols('u v z', positive=True)
P=2*v*u*u+(v-1)*u+v
L=u*(1-v)-v
Q=4*(u-v)*z*z+4*L*z-P
W=(1+z)/(z+sp.Rational(1,2))
E=sp.factor((1+u*W+z*(1+1/v))/(u+z))
expected=(2*u*v*z+2*u*v+2*v*z*z+3*v*z+v+2*z*z+z)/(v*(u+z)*(2*z+1))
assert sp.simplify(E-expected)==0
assert sp.simplify(sp.diff(E,z)-Q/(v*(u+z)**2*(2*z+1)**2))==0
assert sp.simplify(E.subs(z,0)-(1/u+2))==0
assert sp.simplify(sp.limit(E,z,sp.oo)-1-1/v)==0
# Independently invert the transient-chain generator. H: a searcher and one fed scenter;
# A: a searcher without scenter; W: waiting hungry bee and one scenter;
# V: waiting hungry bee without scenter. Absorption occurs upon last feeding.
M=sp.Matrix([[u+z,-z,-u,0], [0,v,0,-v], [0,0,z+sp.Rational(1,2),-z], [0,0,0,1]])
T=M.inv()*sp.ones(4,1)
assert sp.simplify(T[0]-E)==0
assert sp.simplify(T[2]-W)==0
assert sp.simplify(T[1]-1/v-1)==0
# Sharp phase boundary and rational test regimes.
vc=1/(1+2*sp.sqrt(2))
assert sp.simplify(7*vc**2+2*vc-1)==0
vv=sp.Rational(1,4)
assert sp.simplify(P.subs(v,vv)-(u-sp.Rational(1,2))*(u-1)/2)==0
for uu, expected_mode in [(sp.Rational(3,8),'interior'), (sp.Rational(3,4),'zero'), (sp.Integer(2),'interior')]:
    pp=sp.factor(P.subs({u:uu,v:vv}))
    assert (pp>0)==(expected_mode=='interior')
    if expected_mode=='interior':
        ll=L.subs({u:uu,v:vv})
        root=sp.simplify((sp.sqrt(ll**2+(uu-vv)*pp)-ll)/(2*(uu-vv)))
        assert sp.simplify(Q.subs({u:uu,v:vv,z:root}))==0
        assert bool(root>0)
        assert float(E.subs({u:uu,v:vv,z:root})) < float(E.subs({u:uu,v:vv,z:0}))
    else:
        assert Q.subs({u:uu,v:vv,z:0})>0
# Independent rational linear-system checks over a fixed grid.
checks=0
for uu in [sp.Rational(3,8),sp.Rational(3,4),sp.Integer(2),sp.Rational(7,5),sp.Rational(3,2)]:
    for vv2 in [sp.Rational(1,8),sp.Rational(1,4),sp.Rational(1,3)]:
        for zz in [sp.Integer(0),sp.Rational(1,9),sp.Rational(3,4),sp.Integer(4)]:
            if uu<=vv2: continue
            tcalc=M.subs({u:uu,v:vv2,z:zz}).inv()*sp.ones(4,1)
            assert sp.simplify(tcalc[0]-E.subs({u:uu,v:vv2,z:zz}))==0
            checks+=1
print('PASS: symbolic derivative, generator inversion, boundary, radical optima,',checks,'exact rational cases.')
