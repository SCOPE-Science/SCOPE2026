"""Standalone exact-algebra and finite illustrative checks for the cubic quadrature theorem.

Run: python checker.py. Finite tests do not replace the proof in RESULT.md.
"""
import itertools
import math
import random
import sympy as s

x,a,b,c,t,v,z = s.symbols('x a b c t v z', real=True)
g=s.sqrt(3)/3
avg=lambda p:s.integrate(s.expand(p),(x,-1,1))/2
assert all(s.simplify(avg(x**k) - (g**k+(-g)**k)/2)==0 for k in range(4))
assert s.simplify(avg((x+g)**2*(g-x)))==0
assert s.simplify(avg((x-a)*(x-b)*(x-c))+(a+b+c+3*a*b*c)/3)==0
G=-t+2*b+v-3*t*b*(b+v)
max_G=s.simplify(G.subs(b,1/(3*t)-v/2))
assert s.simplify(max_G-(-t+1/(3*t)+3*t*v**2/4))==0
assert s.simplify((-t+1/(3*t)+3*t*(t**2-g**2)/4) - ((3*t*t-1)*(t*t/4-s.Rational(1,3))/t))==0
al,be,mid,half=s.symbols('al be mid half',real=True)
q=(x-(mid-half))*(x-(mid+half))*(al+be*x)
assert s.simplify(avg(q)-(al*(s.Rational(1,3)+mid**2-half**2)-s.Rational(2,3)*be*mid))==0
assert s.simplify((s.Rational(1,3)+mid**2-s.Rational(2,3)*abs(mid))-( (abs(mid)-s.Rational(1,3))**2+s.Rational(2,9)))==0

# Numerical finite stress test of the sharp support lemma on 20,000 random cubics.
rng=random.Random(261032699)
for _ in range(20000):
    roots=sorted(rng.uniform(-3,3) for _ in range(3))
    m=-(sum(roots)+3*math.prod(roots))/3
    if abs(m)<1e-10: continue
    boundaries=[-1.0]+[r for r in roots if -1<r<1]+[1.0]
    negative_length=0.0
    for left,right in zip(boundaries[:-1],boundaries[1:]):
        y=(left+right)/2
        poly=(y-roots[0])*(y-roots[1])*(y-roots[2])
        # Multiply by -sign(m), obtaining nonpositive mean.
        if poly*m>0: negative_length+=right-left
    assert negative_length+1e-9>=1-1/math.sqrt(3)
print('PASS: exact Gauss quadrature, barrier and case identities; 20,000 finite sign-profile checks')
