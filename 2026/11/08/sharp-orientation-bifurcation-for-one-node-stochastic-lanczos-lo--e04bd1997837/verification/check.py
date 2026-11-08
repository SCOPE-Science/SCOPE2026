"""Supplementary exact-arithmetic checks for the rank-one log-SLQ orientation result.

Run: python check.py. Requires SymPy 1.14.0, plus the Python standard library.
Finite tests supplement, and do not replace, the analytic minimization proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
import sympy as sp

assertions = 0

def check(condition, label):
    global assertions
    assert condition, label
    assertions += 1

alpha, X, Y, Z, z = sp.symbols('alpha X Y Z z', real=True)
# The four squared sign sums depend on only pair products and the squared norm.
a = 2 * alpha * X * Y
b = 2 * alpha * X * Z
c = 2 * alpha * Y * Z
d = 1 + alpha * (X**2 + Y**2 + Z**2)
prod = (d+a+b+c)*(d+a-b-c)*(d-a+b-c)*(d-a-b+c)
q = X**2*Y**2 + X**2*Z**2 + Y**2*Z**2
r = X**2*Y**2*Z**2
candidate = (d*d-4*alpha**2*q)**2 + 64*alpha**3*r*(d-alpha*(X**2+Y**2+Z**2))
check(sp.expand(prod-candidate) == 0, 'four-sign product identity')
check(sp.factor(candidate.subs(Z,0).subs(Y**2,1-X**2)) != 0, 'nontrivial boundary expression')

qz=(1+2*z-3*z*z)/4
rz=z*(1-z)**2/4
Pz=sp.expand(((1+alpha)**2-4*alpha**2*qz)**2+64*alpha**3*rz)
check(sp.simplify(Pz - (1+alpha*z)**2 * (9*alpha**2*z*z-12*alpha**2*z+4*alpha**2-2*alpha*z+4*alpha+1))==0,'slice factorization')
check(sp.factor(sp.diff(Pz,z)-4*alpha**2*(3*z-1)*(1+alpha*z)*(3*alpha*z-2*alpha+1))==0,'critical derivative')
P3=(1+alpha/3)**3*(1+3*alpha)
P2=(1+2*alpha)**2
check(sp.factor(P3-P2-alpha**2*(3*alpha**2+28*alpha-18)/27)==0,'endpoint comparison')
check(sp.factor(Pz.subs(z,sp.Rational(0))-P2)==0,'pair endpoint')
check(sp.factor(Pz.subs(z,sp.Rational(1,3))-P3)==0,'triple endpoint')
root=(-14+5*sp.sqrt(10))/3
check(sp.simplify(3*root**2+28*root-18)==0,'threshold root')
check(bool(root>sp.Rational(1,2) and root<sp.Integer(1)),'threshold interval')

# Exact product comparison across many rational probe orientations.
def exact_p(v, s):
    norm2=sum(x*x for x in v)
    if not norm2: return None
    value=F(1)
    for signs in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]:
        w=sum(v[i]*signs[i] for i in range(3))
        value*=1+s*F(w*w,norm2)
    return value

def exact_qpr(v,s):
    norm2=sum(t*t for t in v)
    squares=[F(t*t,norm2) for t in v]
    q0=sum(squares[i]*squares[j] for i in range(3) for j in range(i+1,3))
    r0=squares[0]*squares[1]*squares[2]
    return ((1+s)**2-4*s*s*q0)**2+64*s**3*r0

rng=Random(20261105)
for _ in range(8000):
    v=tuple(rng.randint(-30,30) for _ in range(3))
    if v==(0,0,0): continue
    s=F(rng.randint(1,60),rng.randint(1,35))
    p=exact_p(v,s)
    p3=(1+s/F(3))**3*(1+3*s)
    p2=(1+2*s)**2
    check(p==exact_qpr(v,s),'identity rational replay')
    check(p>=min(p2,p3),'sharp lower bound')
    check(p<=(1+s)**4,'Jensen upper bound')

# All integer triples up to 8, check every rational alpha 1/10,...,30/10.
for v in product(range(9),repeat=3):
    if v==(0,0,0): continue
    for j in range(1,31):
        s=F(j,10)
        check(exact_p(v,s)>=min((1+2*s)**2,(1+s/F(3))**3*(1+3*s)), 'exhaustive grid comparison')

# Sharp equality witnesses checked for low and high spikes.
for s in [F(1,100),F(1,2),F(3,5),F(1),F(7),F(100)]:
    check(exact_p((1,1,1),s)==(1+s/F(3))**3*(1+3*s),'uniform witness')
    check(exact_p((1,1,0),s)==(1+2*s)**2,'pair witness')
    check(exact_p((1,0,0),s)==(1+s)**4,'axis witness')
print('PASS:',assertions,'exact assertions')
print('Threshold alpha =',sp.N(root,20))
print('Threshold spike =',sp.N(3*root,20))
