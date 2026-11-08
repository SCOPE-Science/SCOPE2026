"""Exact identities and rational witness for a geometric-shift trial bound.

Requires SymPy (tested with SymPy 1.13.1). Run: python verify.py
"""
import sympy as s
z,v,a,b,c,d=s.symbols('z v a b c d')
P=1+a*z+b*z**2+c*z**3
G=s.expand((1-3*z)*P*(1-d*z**4)+2*z*(1-z)*s.diff(P,z)*(1-d*z**4)+8*d*z**4*(1-z)*P)
Q=s.Poly(s.cancel((1+v)**8*G.subs(z,v/(1+v))),v)
expected=[1,5+3*a,7+16*a+5*b,-7+33*a+23*b+7*c,
 -35+30*a+40*b+26*c+7*d,
 -49+(5+5*d)*a+30*b+34*c+23*d,
 -35+(12*d-12)*a+(5+3*d)*b+16*c+27*d,
 (d-1)*(13+9*a+5*b+c),2*(d-1)*(1+a+b+c)]
for i,expr in enumerate(expected):
 assert s.expand(Q.coeff_monomial(v**i)-expr)==0, ('coefficient',i)
assert s.expand(expected[4]-s.Rational(26,7)*expected[3]-
               (-9+7*d-s.Rational(648,7)*a-s.Rational(318,7)*b))==0
# Thus if the third coefficient is nonpositive the fourth is strictly negative.
values={a:s.Rational(1,1000),b:s.Rational(1,1000),c:s.Rational(73,100),d:s.Rational(49,50)}
G0=G.subs(values)
points=[s.Rational(1,3),s.Rational(1,2),s.Rational(3,5),s.Rational(3,4),s.Rational(9,10),s.Integer(1)]
expected_signs=[1,1,-1,1,-1,-1]
for point,sgn in zip(points,expected_signs):
 assert s.sign(G0.subs(z,point))==sgn, ('sign',point)
print('SHARP_THREE_CRITICAL_POINT_CEILING_VERIFIED: 9 symbolic coefficients, 1 symbolic inequality, 6 exact rational witness signs')
