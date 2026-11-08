#!/usr/bin/env python3
"""Exact, standalone checks of the odd Hermite two-band norm formula.

Requires Python 3 and SymPy. All universal polynomial comparisons, root counts,
and signs use rational arithmetic; floating calculations are diagnostics only.
"""
from fractions import Fraction
import sympy as S

x,r,t,z=S.symbols('x r t z',real=True)
h1=x
h3=x**3-3*x

def gaussian_moment(expression):
    polynomial=S.Poly(S.expand(expression),x)
    return sum(coefficient * S.factorial2(power[0]-1)
               for power, coefficient in polynomial.terms() if power[0]%2==0)

moments=[gaussian_moment(h1**(4-k)*h3**k) for k in range(5)]
assert moments==[3,6,42,324,3348]
assert gaussian_moment(h1*h3)==0
assert gaussian_moment(h1*h1)==1 and gaussian_moment(h3*h3)==6
print('EXACT_GAUSSIAN_MOMENTS_OK',moments)

N=3+24*r*t+252*r**2*t**2+1296*r**3*t**3+3348*r**4*t**4
assert S.expand(gaussian_moment((h1+r*t*h3)**4)-N)==0
D=(1+6*t*t)**2-r*r*N
q=558*r**4*t**3-324*r**3*t**4+162*r**3*t**2-126*r**2*t**3+21*r**2*t-18*r*t**2+r-3*t
assert S.expand(S.diff(N,t)*(1+6*t*t)-24*t*N-24*q)==0
print('EXACT_QUARTIC_NORM_AND_STATIONARY_EQUATION_OK')

P6=961*z**6-1212*z**5+1359*z**4-56*z**3+39*z**2-12*z+1
assert S.expand(S.discriminant(q,t)+110224800*r**6*P6.subs(z,r*r))==0

def signs_at(seq,v):
    return tuple(int(S.sign(f.subs(z,v))) for f in seq)

def variations(sig):
    clean=[a for a in sig if a]
    return sum(a!=b for a,b in zip(clean,clean[1:]))

st6=S.sturm(P6,z)
s0=signs_at(st6,0)
sinf=tuple(int(S.sign(S.LC(S.Poly(f,z)))) for f in st6)
assert s0==(1,-1,-1,-1,1,-1,-1)
assert sinf==(1,1,-1,-1,1,1,-1)
assert variations(s0)==variations(sinf)==3
assert P6.subs(z,0)>0
print('EXACT_POSITIVE_DISCRIMINANT_FACTOR_STURM_OK')

A=2883*z**4-12*z**3+198*z**2-52*z+3
B=(1984500*z**10-3061800*z**9+1457865*z**8-191979*z**7+
   56574*z**6-48015*z**5+6108*z**4-417*z**3+342*z**2-61*z+3)
assert S.expand(S.resultant(D,q,t)-419904*A.subs(z,r*r)*B.subs(z,r*r))==0
for poly,left,right in [(A,2,2),(B,6,5)]:
    st=S.sturm(poly,z)
    vl=variations(signs_at(st,S.Rational(1,9)))
    vr=variations(signs_at(st,S.Rational(1,4)))
    assert (vl,vr)==(left,right)
print('EXACT_THRESHOLD_ELIMINATION_AND_STURM_ROOT_COUNT_OK')

L=S.Rational(413963,1000000)
U=S.Rational(413964,1000000)
assert B.subs(z,L**2)>0 and B.subs(z,U**2)<0
assert S.expand(D.subs(r,S.Rational(1,3))-(
    S.Rational(2,27)*(424*t**4-72*t**3+120*t**2-12*t+9)))==0
assert S.factor(D.subs({r:S.Rational(1,2),t:S.Rational(1,3)}))==-S.Rational(413,144)
# Positive quadratic decomposition at the full Nelson radius.
assert S.expand((424*t*t-72*t+4)*t*t+116*t*t-12*t+9-
                (424*t**4-72*t**3+120*t*t-12*t+9))==0
assert (-72)**2-4*424*4<0
assert (-12)**2-4*116*9<0
print('EXACT_STRICT_IMPROVEMENT_AND_ROOT_BRACKET_OK')

for rr in [S.Rational(1,10),S.Rational(1,3),S.Rational(2,5),S.Rational(1,2),S.Rational(1,1)]:
    roots=S.polys.polytools.intervals(S.Poly(q.subs(r,rr),t),eps=S.Rational(1,100000))
    assert len(roots)==2, (rr,roots)
    assert roots[0][0][1]<0<roots[1][0][0]
print('RATIONAL_SAMPLE_ROOT_ISOLATIONS_OK')
print('ALL_ODD_HERMITE_CONTRACTIVITY_CHECKS_PASSED')
