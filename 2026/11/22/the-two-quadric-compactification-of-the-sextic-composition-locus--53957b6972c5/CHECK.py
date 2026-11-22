"""Reproduce exact polynomial identities for the projective sextic composition locus.
The general algebraic-geometric proof is in RESULT.md; these checks are supplementary.
"""
from sympy import symbols, expand, Poly, binomial, simplify, Matrix

h,A,B,C,D,a,b,t = symbols('h A B C D a b t')
F = A**2 - 4*h*C
Q1 = A*B - 2*h*D
Q2 = 2*B*C - A*D
assert expand(A*Q1 - 2*h*Q2 - B*F) == 0
assert expand(2*C*Q1 - A*Q2 - D*F) == 0

f = expand((t**3+b*t)**2 + a*(t**3+b*t))
assert f == t**6 + 2*b*t**4+a*t**3+b*b*t**2+a*b*t
assert expand(Q1.subs({h:1,A:2*b,B:a,C:b**2,D:a*b})) == 0
assert expand(Q2.subs({h:1,A:2*b,B:a,C:b**2,D:a*b})) == 0
assert expand(F.subs({h:1,A:2*b,B:a,C:b**2,D:a*b})) == 0

# Local complete-intersection identities at the finite part and at infinity.
assert expand((2*Q2).subs({h:1,D:A*B/2})-B*(4*C-A**2))==0
assert expand((2*Q1).subs({C:1,B:A*D/2})-D*(A**2-4*h))==0

# Jacobian rank at the representative conic point [1:0:0:0:0] and
# the unique infinity point [0:0:0:1:0]. Both are singular points.
var = [h,A,B,C,D]
Jac = Matrix([[z.diff(v) for v in var] for z in [Q1,Q2]])
for pt in [{h:1,A:0,B:0,C:0,D:0},{h:0,A:0,B:0,C:1,D:0}]:
    assert Jac.subs(pt).rank() == 1
# In a CI of two quadrics in P4, section ring Hilbert coefficients
# from (1+t)^2/(1-t)^3 agree with Hilbert polynomial 2n^2+2n+1.
for n in range(15):
    hco = binomial(n+2,2)+2*binomial(n+1,2)+(binomial(n,2) if n>=2 else 0)
    assert simplify(hco - (2*n*n+2*n+1)) == 0
print('PASS: coefficient maps, two syzygies, both crossing charts, singular witnesses, Hilbert coefficients')
