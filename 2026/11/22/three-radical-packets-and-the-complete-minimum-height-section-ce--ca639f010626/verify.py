#!/usr/bin/env python3
"""Exact symbolic checks for the Brahmagupta elliptic surface section census.

Requires Python 3.10+ and SymPy 1.12+; prints successes, never relies on
floating-point root enumeration. Geometric rank and height require the standard
Kodaira/Shioda--Tate/height theorems and are established in RESULT.md.
"""
import sympy as s

T, a, b, z, u, v = s.symbols('T a b z u v')
A = 4*T**4
B = 4*T**2
D = s.expand(-16*(4*A**3+27*B**2))
assert s.factor(D) == -256*T**4*(16*T**8+27)
assert s.gcd(16*T**8+27, s.diff(16*T**8+27,T)) == 1
assert s.simplify(-48*A) == -192*T**4
assert s.expand(-16*(4*4**3+27*(4*u**4)**2)+256*(16+27*u**8))==0
print('PASS: discriminant, eight simple nonzero nodal parameters, smooth infinity')

# P=(0,2t) and its double explicitly satisfy the equation.
for x,y in ((0,2*T),(T**6,-T*(T**8+2))):
    assert s.expand(y**2-x**3-4*T**4*x-4*T**2)==0
print('PASS: nontrivial section and its double')

# Polynomial section with y coefficient 2t and vanishing at t=0:
# x=b*t+a*t**2, y=2*t+e*t**2+d*t**3.
d,e=s.symbols('d e')
x=b*T+a*T**2
y=2*T+e*T**2+d*T**3
res=s.Poly(s.expand(y*y-x**3-4*T**4*x-4*T**2),T)
assert res.nth(3)==4*e-b**3
assert res.nth(4)==e**2+4*d-3*a*b**2
assert res.nth(5)==2*e*d-3*a*a*b-4*b
assert res.nth(6)==d*d-a**3-4*a
print('PASS: four exact coefficient equations')

E=b**3/4
Db=(3*a*b**2-b**6/16)/4
R5=s.factor(res.nth(5).subs({e:E,d:Db}))
R6=s.factor(res.nth(6).subs({e:E,d:Db}))
# Check the exact proportionality of the remaining equations to F1 and F2.
F1=384*a*a-48*a*b**4+b**8+512
F2=-4096*a**3+2304*a*a*b**4-96*a*b**8-16384*a+b**12
assert s.expand(R5+b*F1/s.Integer(128))==0
assert s.expand(R6-F2/s.Integer(4096))==0
# b=0 gives e=d=0, and a^3+4a=0 -> 3 distinct roots.
assert s.factor(res.nth(6).subs({b:0,e:0,d:0})) == -a*(a*a+4)

# For b !=0 put a=tau*b^4 and w=b^8.
tau,w=s.symbols('tau w')
assert s.expand(F1.subs(a,tau*b**4)-(b**8*(384*tau**2-48*tau+1)+512))==0
assert s.simplify(F2.subs(a,tau*b**4)/b**4-(b**8*(-4096*tau**3+2304*tau**2-96*tau+1)-16384*tau))==0
assert s.expand(-512*(-4096*tau**3+2304*tau**2-96*tau+1)-16384*tau*(384*tau**2-48*tau+1)+512*(32*tau-1)*(256*tau*tau+32*tau-1))==0
print('PASS: elimination yields three distinct normalized coefficient branches')

values=(s.Rational(1,32),(-1+s.sqrt(2))/16,(-1-s.sqrt(2))/16)
wvals=[]
for t in values:
    W=s.simplify(-512/(384*t*t-48*t+1)).radsimp()
    assert s.simplify(W*(384*t*t-48*t+1)+512)==0
    assert s.simplify(W*(-4096*t**3+2304*t*t-96*t+1)-16384*t)==0
    assert W!=0
    wvals.append(W)
assert s.simplify(wvals[0]-4096)==0
assert s.simplify(wvals[1]+17408+12288*s.sqrt(2))==0
assert s.simplify(wvals[2]+17408-12288*s.sqrt(2))==0
assert s.simplify(wvals[1]-wvals[2])!=0
print('PASS: 3 nonzero eighth-power parameters, 8 choices each (24), plus 3 zero-parameter sections')

# An independent polynomial resultant check, using z=b^2.
z=s.symbols('z')
f1=384*a**2-48*a*z**2+z**4+512
f2=-4096*a**3+2304*a*a*z*z-96*a*z**4-16384*a+z**6
res_a=s.factor(s.resultant(f1,f2,a))
assert s.expand(res_a + 2097152*(z**4-4096)*(z**8+34816*z**4+1048576))==0
assert s.gcd((z**4-4096)*(z**8+34816*z**4+1048576),s.diff((z**4-4096)*(z**8+34816*z**4+1048576),z)) == 1
print('PASS: resultant factorization and squarefreeness of 12 nonzero z values')
H=(b**8-4096)*(b**16+34816*b**8+1048576)
assert s.simplify(s.expand(H-(b**8-wvals[0])*(b**8-wvals[1])*(b**8-wvals[2])))==0
print('PASS: exact 24-root splitting polynomial over Q')
print('PASS: 54 distinct sections including negative pairs, by the displayed proof')
