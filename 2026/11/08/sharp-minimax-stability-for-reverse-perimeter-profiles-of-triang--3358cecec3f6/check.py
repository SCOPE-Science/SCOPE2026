"""Independent symbolic identity and numerical boundary checks for the triangle theorem.

Run: python check.py   (SymPy >= 1.12)
Finite sampling is corroboration only; the proof in RESULT.md is universal.
"""
from math import sqrt
import random
import sympy as s

z, r, u, v, w = s.symbols('z r u v w', real=True)
a, b, c = u + 2*v + w, u + v + w, v + w
q2 = s.expand((1-z)*a*a + z*b*b - z*(1-z)*c*c)
f = (1+z+r)/3
k = 2*(1-f)
d = (2-z+2*r)/3
L = u+d*v+r*w
expected = 2*(1-r)*u*w + s.Rational(2,3)*(2-z-r)*v*(2*u+(2-z+d)*v+(2-z)*w)

def relation_reduce(expr):
    return s.factor(s.rem(s.Poly(s.expand(expr),r), s.Poly(r*r-(1-z+z*z),r)).as_expr())

assert relation_reduce(q2-L*L-expected) == 0
assert relation_reduce((a+z*c+L)-(f*(a+b+c)+k*(a-c))) == 0
# The triangular cone parameterization must reproduce the ordered side gaps.
assert s.expand(a-b-v)==0
assert s.expand(b-c-u)==0
assert s.expand(b+c-a-w)==0

rng=random.Random(20261101)
checks=0
for _ in range(30000):
    zz=rng.random()*.999998+.000001
    uu,vv,ww=[rng.random()+.000001 for __ in range(3)]
    aa=uu+2*vv+ww;bb=uu+vv+ww;cc=vv+ww
    rr=sqrt(1-zz+zz*zz)
    ff=(1+zz+rr)/3
    kk=2*(1-ff)
    p=aa+bb+cc
    witness=aa+zz*cc+sqrt((1-zz)*aa**2+zz*bb**2-zz*(1-zz)*cc**2)
    assert witness >= ff*p+kk*(aa-cc)-1e-11
    checks += 1
# For a=b=1, c -> 0, triangle inequalities hold and the bound is sharp.
for zz in (.01,.2,.5,.8,.99):
    rr=sqrt(1-zz+zz*zz);ff=(1+zz+rr)/3;kk=2*(1-ff)
    for N in (100,1000,10000):
        cc=1/N;aa=bb=1
        witness=1+zz*cc+sqrt(1-zz*(1-zz)*cc**2)
        upper=2+cc  # Perimeter monotonicity for convex containment
        assert witness <= upper+1e-12
        lower_bound=(ff*(2+cc)+kk*(1-cc))
        assert witness >= lower_bound-1e-11
        checks += 1
print('SYMBOLIC_IDENTITY_OK; NUMERIC_CHECKS=',checks)
