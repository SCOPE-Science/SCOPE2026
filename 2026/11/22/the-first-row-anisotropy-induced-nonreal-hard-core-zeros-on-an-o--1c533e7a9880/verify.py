#!/usr/bin/env python3
"""Exact finite-ladder hard-core zero calculation; requires SymPy >= 1.10.
Run: python verify.py
"""
from itertools import product
from sympy import (symbols, Poly, Integer, Rational, expand, factor,
                   discriminant, simplify, count_roots, nroots)

z,t,y,v=symbols('z t y v')
E,U,D=Integer(1),Integer(0),Integer(0)
P=[Integer(1)]
for n in range(1,6):
    E,U,D=expand(E+U+D),expand(z*(E+D)),expand(t*z*(E+U))
    P.append(expand(E+U+D))

# Independently count hard-core configurations by direct mask enumeration.
def brute(n,ratio):
    weights=[Rational(0)]*(n+1)
    for bits in product((0,1),repeat=2*n):
        if any(bits[2*j] and bits[2*j+1] for j in range(n)):
            continue
        if any(bits[2*j+row] and bits[2*(j+1)+row]
               for j in range(n-1) for row in (0,1)):
            continue
        k=sum(bits)
        weights[k]+=ratio**sum(bits[2*j+1] for j in range(n))
    return sum(weights[k]*z**k for k in range(n+1))
for n in range(1,6):
    for ratio in (Rational(1),Rational(2),Rational(5),Rational(11,3)):
        assert expand(P[n].subs(t,ratio)-brute(n,ratio))==0

# Row-exchange duality: P(z;t)=P(t*z;1/t), substitution simultaneous.
for n in range(1,6):
    assert simplify(P[n]-P[n].subs({z:t*z,t:1/t},simultaneous=True))==0

D2=factor(discriminant(P[2],z))
D3=factor(discriminant(P[3],z))
D4=factor(discriminant(P[4],z))
D5=factor(discriminant(P[5],z))
assert simplify(D2-4*(t*t+1))==0
assert simplify(D3-t**3*(5*(t+1/t)**3+81*(t+1/t)-54))==0
J=lambda x:27*x**4-54*x**3+117*x**2-108*x+20
assert simplify(D4-16*t**6*J(t+1/t))==0
assert expand(J(2+v))==27*v**4+162*v**3+441*v**2+576*v+272
H=lambda x: (196*x**7-1568*x**6+24976*x**5-154252*x**4+344136*x**3-415301*x**2+263692*x-54228)
assert simplify(D5+t**10*H(t+1/t))==0
G=expand(H(2+v))
assert G==196*v**7+1176*v**6+22624*v**5+56308*v**4-31960*v**3-299061*v**2-419112*v-179024
assert G.subs(v,0)<0
assert count_roots(G,0,1000)==1

# Certify at least n real roots at isotropic ratio by disjoint rational signs.
intervals={
  1:[(-Rational(3,5),-Rational(2,5))],
  2:[(-2,-Rational(3,2)),(-Rational(2,5),-Rational(1,5))],
  3:[(-Rational(16,5),-3),(-Rational(4,5),-Rational(3,5)),(-Rational(1,4),-Rational(1,5))],
  4:[(-4,-Rational(39,10)),(-Rational(3,2),-Rational(13,10)),(-Rational(9,20),-Rational(2,5)),(-Rational(11,50),-Rational(1,5))],
  5:[(-5,-4),(-Rational(5,2),-2),(-1,-Rational(1,2)),(-Rational(2,5),-Rational(3,10)),(-Rational(1,4),-Rational(1,5))]
}
for n,ranges in intervals.items():
    f=P[n].subs(t,1)
    assert len(ranges)==n
    assert all(f.subs(z,a)*f.subs(z,b)<0 for a,b in ranges), (n,[(a,b,f.subs(z,a),f.subs(z,b)) for a,b in ranges])

# Sharp unique threshold, reciprocal; numeric values only supplemental.
positive=[complex(q) for q in nroots(G,maxsteps=300) if abs(complex(q).imag)<1e-10 and complex(q).real>0]
assert len(positive)==1
u_star=positive[0].real
y_star=u_star+2
t_star=(y_star+(y_star*y_star-4)**0.5)/2
assert 4<t_star<4.1
assert D5.subs(t,1)>0 and D5.subs(t,5)<0
print('ALL_EXACT_CHECKS_PASSED')
print('direct enumerations:',5*4,'root brackets:',sum(len(x) for x in intervals.values()))
print('u_star=',u_star,'t_star=',t_star,'t_star_reciprocal=',1/t_star)
