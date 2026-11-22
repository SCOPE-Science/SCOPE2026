"""Exact certificate for the two-notch circle support-gap theorem.
Run with Python 3 and SymPy, as listed in requirements.txt.
"""
import sympy as sp

x=sp.symbols('x')
y=(sp.Integer(2)+sp.sqrt(10))/12
b=sp.sqrt(y)
s=sp.sqrt(1-2*y)
c=s-b
e=-s-b
k=16*b*s**2
T4=8*x**4-8*x**2+1
P=sp.expand(T4+k*x)
assert sp.simplify(P-8*(x-b)**2*(x-c)*(x-e))==0
assert sp.simplify(24*y**2-8*y-1)==0
assert sp.simplify(P.subs(x,b))==0
assert sp.simplify(P.subs(x,c))==0

# Exact rational interval certificates. Since 3 < sqrt(10) < 10/3,
# 5/12 < y < 4/9, so 1/3 < y < 1/2 and y < 4/9.
assert 3**2 < 10 and 10*9 < 100
assert sp.simplify(y-sp.Rational(5,12)).is_positive
assert sp.simplify(sp.Rational(4,9)-y).is_positive
assert sp.simplify(y-sp.Rational(1,3)).is_positive
assert sp.simplify(sp.Rational(1,2)-y).is_positive
# b>s>0 and b+s>1; the latter is equivalent to 4*s**2>y.
assert sp.simplify(b*b-s*s).is_positive
assert sp.simplify(4*s*s-y).is_positive
# Consequently e<-1<c<0<b<1; x-e>0 on [c,1].
wc=b/(b-c)
wb=-c/(b-c)
assert sp.simplify(wc+wb-1)==0
assert sp.simplify(wc*c+wb*b)==0
assert sp.simplify(wc*(8*c**4-8*c**2+1)+wb*(8*b**4-8*b**2+1))==0

# The sine-moment system is nonsingular: U_3(c)>0 and U_3(b)<0.
U3=lambda z:4*z*(2*z*z-1)
assert sp.simplify(2*c*c-1).is_negative
assert sp.simplify(2*b*b-1).is_negative
# Actual values for independent numerical sanity (never proof).
import math
bn=float(b.evalf(18));cn=float(c.evalf(18))
A=math.acos(cn);B=math.acos(bn)
gap=2*math.pi-2*A
assert 2.5693<gap<2.5694
assert abs(math.sin(A)*math.sin(B)*(float(U3(c).evalf())-float(U3(b).evalf())))>1e-3
print('PASS: exact factorization, root ordering, weights, moments, rigidity')
print('b = %.12f; c = %.12f; sharp gap = %.12f radians' % (bn,cn,gap))
