"""Exact algebra and numerical spot checks for a regularized logistic FBE theorem.

Run: python verify.py
Requires Python 3, sympy, and standard library. Finite tests illustrate,
but do not replace, the analytic all-parameter proof.
"""
from fractions import Fraction as F
import math
import random
import sympy as sp

p,q,l,g,x=sp.symbols('p q l g x',real=True)
a=p*(1-p)
b=a*(1-2*p)
D=sp.expand(a+(1-2*p)*(p-q-l))
r=sp.symbols('r',real=True)
p0=(1+r)/3
assert sp.simplify(D.subs(q,r-l).subs(p,p0)-(1-r+r*r)/3)==0
assert sp.simplify(D.subs(q,r-l)-( (1-r+r*r)/3 - 3*(p-(1+r)/3)**2 ))==0
assert sp.simplify(sp.diff(D,p).subs(q,r-l).subs(p,p0))==0
assert sp.simplify(p0-r)==(1-2*r)/3
assert sp.simplify(sp.Rational(3,4)+(sp.Rational(1,2)-r)**2-(1-r+r*r))==0

# Branch derivatives of E = f - gamma/2 (f')**2 + Moreau(L1)(x-gamma*f').
t=sp.Function('t')(x)
# symbolic differentiation using exact logistic derivative substitution
z=sp.symbols('z', real=True)
f=sp.log(1+sp.exp(z))-q*z
fp=sp.diff(f,z)
fpp=sp.diff(f,z,2)
fppp=sp.diff(f,z,3)
y=z-g*fp
EA=f-g*fp**2/2+l*y-g*l*l/2
EB=f-g*fp**2/2-l*y-g*l*l/2
EI=f-g*fp**2/2+y*y/(2*g)
for sign, expr in [(1,EA),(-1,EB)]:
    pred=sp.expand((fp+sign*l)*(1-g*fpp))
    assert sp.simplify(sp.diff(expr,z)-pred)==0
    pred2=fpp*(1-g*fpp)-g*fppp*(fp+sign*l)
    assert sp.simplify(sp.diff(expr,z,2)-pred2)==0
assert sp.simplify(sp.diff(EI,z)-z*(1/g-fpp))==0
assert sp.simplify(sp.diff(EI,z,2)-(1/g-fpp-z*fppp))==0

# Sharp explicit window where regularization restores convexity.
Q=F(1,10); L=F(1,10); gamma=F(7,2)
d0=abs(Q-F(1,2)); d1=max(F(0),d0-L)
g0=F(3,1)/(F(3,4)+d0*d0)
g1=F(3,1)/(F(3,4)+d1*d1)
assert g0==F(300,91) and g1==F(25,7)
assert g0<gamma<g1


def sig(z):
    return 1/(1+math.exp(-z)) if z>=0 else math.exp(z)/(1+math.exp(z))


def curvature(z,q,l,g):
    p=sig(z); a=p*(1-p); b=a*(1-2*p)
    y=z-g*(p-q)
    if y>g*l: return a*(1-g*(a+(1-2*p)*(p-q+l)))
    if y< -g*l: return a*(1-g*(a+(1-2*p)*(p-q-l)))
    return 1/g-a-z*b


def critical(q,l):
    d=max(0,abs(q-.5)-l)
    return 3/(.75+d*d)

rnd=random.Random(348714)
for _ in range(150):
    q0=rnd.uniform(.001,.999)
    l0=rnd.uniform(.001,.60)
    cut=critical(q0,l0)
    # Below cutoff, dense grid of all analytic branches must be nonnegative.
    gg=cut*rnd.uniform(.1,.999)
    assert min(curvature(j/12,q0,l0,gg) for j in range(-120,121))>-1e-10
    # Above cutoff, strict negativity has a mathematically known witness.
    gg=cut+rnd.uniform(.01,.4)
    if cut<4-1e-7:
        qq=min(q0,1-q0); rr=qq+l0
        if rr<.5:
            pp=(1+rr)/3
            z=math.log(pp/(1-pp))
            if q0>.5: z=-z
            assert curvature(z,q0,l0,gg)<0
    else:
        assert gg>4-1e-7
        # local negative curvature at x=0 off the piecewise boundary
        assert min(curvature(z,q0,l0,gg) for z in (-1e-6,1e-6))<0

print('PASS: exact symbolic branch identities, sharp maximum, rational restoration window, 150 parameter pairs.')
