"""Finite symbolic and numerical checks for a Bergman Toeplitz Jacobi jet law.
The infinite-dimensional theorem uses the proof in RESULT.md, not this checker.
"""
from fractions import Fraction
import math
import sympy as sp

x,z,a=sp.symbols('x z a',positive=True)
f=a*x*sp.sqrt((x+1)*(x+2))/((x+a)*(x+a+1))
series=sp.series(f.subs(x,1/z),z,0,3).removeO().expand()
assert sp.simplify(series.coeff(z,0)-a)==0
assert sp.simplify(series.coeff(z,1)-a*(sp.Rational(1,2)-2*a))==0
# Independent beta-moment expansion using boundary derivatives of g(t)=t^a.
g1=a; g2=a*(a-1); g3=a*(a-1)*(a-2)
c1=-sp.Rational(3,2)*g1-2*g2
c2=sp.Rational(19,8)*g1+9*g2+3*g3
assert sp.simplify(series.coeff(z,1)-c1)==0
assert sp.simplify(series.coeff(z,2)-c2)==0
assert sp.simplify(c1.subs(a,sp.Rational(1,4)))==0
assert sp.simplify(c2.subs(a,sp.Rational(1,4))+sp.Rational(7,64))==0

# Exact moment identity for g=t^a from d_k=(k+1)/(k+1+a).
for aa in (sp.Rational(1,4), sp.Rational(2,3),sp.Rational(1,1), sp.Rational(3,2)):
    for n in range(35):
        l=sp.Integer(n+1)
        d0=l/(l+aa)
        d1=(l+1)/(l+1+aa)
        weight=sp.simplify(l*sp.sqrt((l+1)*(l+2))*(d1-d0))
        direct=aa*l*sp.sqrt((l+1)*(l+2))/((l+aa)*(l+aa+1))
        assert sp.simplify(weight-direct)==0

# Beta expectation for a general cubic polynomial.
t=sp.symbols('t',real=True)
g=sp.Rational(2,3)*t + sp.Rational(5,4)*t**2-sp.Rational(1,7)*t**3
for n in range(12):
    l=sp.Integer(n+1)
    d0=l*sp.integrate(t**(l-1)*g,(t,0,1))
    d1=(l+1)*sp.integrate(t**l*g,(t,0,1))
    beta=sp.integrate(t**l*(1-t)*sp.diff(g,t),(t,0,1))
    assert sp.simplify(d1-d0-beta)==0

# Direct finite-matrix singular-value consistency: these checks are samples only.
import numpy as np
for aa in (0.25,0.4,1.,2.):
    for N in (40,80,160):
        l=np.arange(1,N,dtype=float)
        j=aa*l*np.sqrt((l+1)*(l+2))/((l+aa)*(l+aa+1))
        b=j-aa
        K=np.diag(b,1)+np.diag(b,-1)
        assert np.max(np.abs(K-K.T))<1e-13
        assert np.isfinite(np.linalg.svd(K,compute_uv=False)).all()
# Higher-index asymptotics are checked independently of small finite truncations.
for aa in (0.25,0.4,1.,2.):
    ll=10000.
    ww=aa*ll*math.sqrt((ll+1)*(ll+2))/((ll+aa)*(ll+aa+1))-aa
    if aa==0.25:
        assert abs(ww*ll**2+7/64)<.001
    else:
        assert abs(ww*ll-aa*(.5-2*aa))<.02
print('PASS: symbolic jets, moment identities, 140 exact power checks, 12 polynomial checks, 12 finite matrix checks')
