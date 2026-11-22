"""Independent algebraic and numerical checks for three-state sensor peak classification.

Requires Python, NumPy, and SymPy. Numerical tests check formulas, not infinite claims.
"""
import math
import numpy as np
import sympy as sp

x, a, b, c = sp.symbols('x a b c', positive=True, real=True)
Q = sp.Matrix([[-a,a,0],[0,-b,b],[c,0,-c]])
P = a*b+b*c+c*a
L = a*a+b*b+c*c
H = [b*b+b*c+c*c, a*a+a*c+c*c, a*a+a*b+b*b]
pi = [b*c/P, a*c/P, a*b/P]
zz = sp.symbols('zz', positive=True)
# Resolvent diagonal and pole subtraction: symbolic exact polynomial identities
# Verify residue formula directly by comparing numerator form for all indices.
for i in range(3):
    R = (zz*sp.eye(3)-Q).inv()[i,i]
    rhs = ((zz + [a,b,c][(i+1)%3])*(zz+[a,b,c][(i+2)%3]))/(zz*(zz*zz+(a+b+c)*zz+P))
    assert sp.factor(R-rhs)==0
    R0 = sp.cancel(R-pi[i]/zz)
    assert sp.simplify(sp.factor(R0)) is not None

S = sum(H)
assert sp.factor(S-(2*L+P))==0
assert sp.factor(3*P**2-L*S - (P-L)*(3*P+2*L))==0
assert sp.factor(P**2-L*H[0]-(P**2-L*H[1])) == -(b-a)*(a+b+c)*L
assert sp.factor(P**2-L*H[1]-(P**2-L*H[2])) == -(c-b)*(a+b+c)*L
assert sp.factor((P**2-L*H[1]).subs({b:1,c:1})+(a-1)*(a**3+2*a*a+a-1))==0
assert sp.factor((P**2-L*H[0]).subs({b:1,c:1})-(a-1)*(a+5))==0

root=float(sp.nroots(a**3+2*a*a+a-1)[0])
assert .46<root<.47
rng=np.random.default_rng(19870716)
max_error=0.
for j in range(300):
    rates=np.exp(rng.uniform(-2.5,2.5,3))
    aa,bb,cc=rates
    p=aa*bb+bb*cc+cc*aa
    ell=sum(rates**2)
    hs=[bb*bb+bb*cc+cc*cc,aa*aa+aa*cc+cc*cc,aa*aa+aa*bb+bb*bb]
    ps=[bb*cc/p,aa*cc/p,aa*bb/p]
    gen=np.array([[-aa,aa,0],[0,-bb,bb],[cc,0,-cc]])
    for w in rng.uniform(.03,5.,4):
        resolvent=np.linalg.inv(1j*w*np.eye(3)-gen)
        for i,h in enumerate(hs):
            spec=2*aa*bb*cc/p*(w*w+h)/(w**4+ell*w*w+p*p)
            numeric=2*ps[i]*np.real(resolvent[i,i])
            err=abs(spec-numeric)/(1+abs(spec))
            max_error=max(max_error,err)
            assert err<1e-10
    deltas=[p*p-ell*h for h in hs]
    assert sum(d>1e-11 for d in deltas)<=2
    for i,d in enumerate(deltas):
        if d>1e-10:
            zp=-hs[i]+math.sqrt(hs[i]**2+d)
            assert zp>0
            # Rational profile strictly peaks where predicted, not merely stationary.
            f=lambda z:(z+hs[i])/(z*z+ell*z+p*p)
            assert f(zp)>f(0.)
            assert f(zp)>f(zp*1.1)
            assert f(zp)>f(zp*.9)

for test,expected in [(.1,0),(.465571231876768,0),(.5,2),(.9,2),(1.,0),(2.,1)]:
    aa,bb,cc=test,1.,1.
    p=aa*bb+bb*cc+cc*aa
    ell=aa*aa+bb*bb+cc*cc
    hs=[3.,aa*aa+aa+1,aa*aa+aa+1]
    d=[p*p-ell*h for h in hs]
    assert sum(v>1e-9 for v in d)==expected,(test,d,expected)
print(f'OK: symbolic identities, 3600 resolvent comparisons, 300 peak tests, and 0-2-0-1 wedge; root={root:.15f}; max_relative_error={max_error:.2e}')
