"""Algebraic and finite-trajectory checks for a two-habitat Allee--logistic system.

Run: python verify.py
Requires: Python 3.10+, SymPy, SciPy, NumPy.
Numerical integrations supplement, but do not replace, the mathematical proof.
"""
from fractions import Fraction
import sympy as S
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root

e, s, h, m, d, u, v = S.symbols('e s h m d u v', positive=True)
A = S.Matrix([[-e-d, d], [d, s-d]])
assert S.simplify(A.det()-(d*(e-s)-e*s))==0
assert S.simplify(A.trace()-(s-e-2*d))==0
assert S.simplify(A.charpoly().discriminant()-((e+s)**2+4*d**2))==0
crit = e*s/(e-s)
a = s/e
r = S.Matrix([a, 1]); q = S.Matrix([1,-a])
assert S.simplify(A.subs(d,crit)*r)==S.zeros(2,1)
kappa = e-s+2*crit
assert S.simplify(A.subs(d,crit)*q+kappa*q)==S.zeros(2,1)
N2 = S.Matrix([(1/m-h)*a*a, -s])
k = S.factor(-r.dot(N2)/r.dot(r))
alpha = S.factor(-r.dot(A.diff(d)*r)/r.dot(r))
assert S.simplify(k-(s+a**3*(h-1/m))/(1+a*a))==0
assert S.simplify(alpha-(1-a)**2/(1+a*a))==0
assert S.factor(alpha/k-(1-a)**2/(s+a**3*(h-1/m)))==0
F = S.Matrix([u*(u/(m+u)-e-h*u)+d*(v-u), s*v*(1-v)+d*(u-v)])
assert S.simplify(F.jacobian([u,v]).subs({u:0,v:0})-A)==S.zeros(2,2)
assert S.simplify(F-S.Matrix([A[0,0]*u+A[0,1]*v,A[1,0]*u+A[1,1]*v])-S.Matrix([u*u*(1/(m+u)-h),-s*v*v]))==S.zeros(2,1)
params={e:S.Rational(3,4),s:S.Rational(1,2),h:S.Integer(1),m:S.Integer(2)}
dstar = S.factor(crit.subs(params))
assert dstar==S.Rational(3,2)
assert S.factor(a.subs(params))==S.Rational(2,3)
assert S.factor(k.subs(params))==S.Rational(35,78)
assert S.factor(alpha.subs(params))==S.Rational(1,13)
assert S.factor((1/k).subs(params))==S.Rational(78,35)
assert S.factor((a/k).subs(params))==S.Rational(52,35)
assert S.factor((alpha/k).subs(params))==S.Rational(6,35)
assert S.factor((a*alpha/k).subs(params))==S.Rational(4,35)

# Independent exact equilibrium elimination in the concrete example.
ue, ve, de = S.symbols('ue ve de')
fe=F[0].subs({u:ue,v:ve,d:de,**params})
ge=F[1].subs({u:ue,v:ve,d:de,**params})
assert S.factor(ge-(de*ue+(S.Rational(1,2)-de)*ve-S.Rational(1,2)*ve**2))==0
# Differentiate the stationary equations along a positive branch born at the origin.
# The first-order direction is the null vector (2/3,1) and the second order
# solvability condition yields the above 4/35, 6/35 slopes.
T=S.symbols('T',positive=True)
c_u,c_v,c2_u,c2_v=S.symbols('c_u c_v c2_u c2_v')
series=F.subs({**params,d:dstar-T,u:c_u*T+c2_u*T*T,v:c_v*T+c2_v*T*T})
coeff2=S.Matrix([S.expand(S.series(expr,T,0,3).removeO()).coeff(T,2) for expr in series])
subslinear={c_u:S.Rational(2,3)*c_v}
sol=S.solve([S.factor(z.subs(subslinear)) for z in coeff2],[c2_u,c2_v,c_v],dict=True)
# This is rank-deficient at order 2 without the projection; eliminate c2 via left Perron vector.
weighted=S.factor((S.Rational(2,3)*coeff2[0]+coeff2[1]).subs(subslinear))
assert S.simplify(weighted.subs({c_v:S.Rational(6,35)}))==0
assert S.simplify(weighted/c_v-S.Rational(13,9)*(S.Rational(1,13)-S.Rational(35,78)*c_v))==0

E=float(dstar)
def fun(t,y,dd):
    uu,vv=y
    return [uu*(uu/(2+uu)-.75-uu)+dd*(vv-uu), .5*vv*(1-vv)+dd*(uu-vv)]

def eq_at(dd):
    x=root(lambda y:fun(0,y,dd),[.11*(E-dd),.17*(E-dd)],tol=1e-12)
    assert np.linalg.norm(fun(0,x.x,dd)) < 1e-10
    assert min(x.x)>0
    return x.x
for dd in (1.3, 1.49, 1.499):
    uu,vv=eq_at(dd)
    assert abs(vv/(E-dd)-6/35) < 0.03
    assert abs(uu/(E-dd)-4/35) < 0.03
for y0 in ([.2, .8], [1.5, .1], [0.02,0.05]):
    sol=solve_ivp(fun,[0,12000],y0,args=(E,),rtol=1e-11,atol=1e-13,method='DOP853')
    assert sol.success
    uu,vv=sol.y[:,-1]
    print('critical sample',y0,'t*u',12000*uu,'t*v',12000*vv)
    assert abs(12000*vv-78/35) < 0.03
    assert abs(12000*uu-52/35) < 0.025
for dd in (1.6,2.):
    sol=solve_ivp(fun,[0,3000],[.3,.7],args=(dd,),rtol=1e-10,atol=1e-12)
    assert sol.success and max(sol.y[:,-1])<1e-5
print('VERIFY_OK: exact linearization/center coefficients, branch and finite trajectories')
