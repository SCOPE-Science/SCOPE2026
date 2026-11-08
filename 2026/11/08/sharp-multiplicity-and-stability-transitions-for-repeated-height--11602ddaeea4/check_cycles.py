#!/usr/bin/env python3
"""Independent symbolic and exact arithmetic checks for repeated-height cycles.
Requires SymPy. All assertions are exact algebraic identities or rational inequalities.
The general infinite-degree root count is established in RESULT.md, not by this script.
"""
import sympy as S
x,y,z,t,k = S.symbols('x y z t k', real=True)
P=lambda v: k*v*(v-1)
h=y+x*x
F=S.Matrix([P(h),z-2*x*P(h),P(h)**2])
Jac=F.jacobian([x,y,z]); assert S.expand(Jac.charpoly().as_expr())==S.Symbol('lambda')**3
# Direct conjugacy of nilpotent-Jacobian map to reduced recurrence.
X,Y,Z=S.symbols('X Y Z',real=True)
p=P(Y)
Psi={x:X+p,y:Y-(X+p)**2,z:Z+p*(p+2*X)}
Fp=F.subs(Psi, simultaneous=True)
newY=S.expand(Fp[1]+Fp[0]**2)
newX=S.expand(Fp[0]-P(newY))
newZ=S.expand(Fp[2]-P(newY)*(P(newY)+2*newX))
assert S.simplify(newY-Z)==0
assert S.simplify(newX-(P(Y)-P(Z)))==0
assert S.simplify(newZ-(P(Y)-P(Z))**2)==0
# Exact triple-cycle relation and nonzero eigenvalue of the third return.
a,b,c=S.symbols('a b c')
M0=S.Matrix([[0,b,-c],[0,0,1],[0,2*a*b,-2*a*c]])
M1=S.Matrix([[0,c,-b],[0,0,1],[0,-2*a*c,2*a*b]])
M2=S.Matrix([[0,b,-b],[0,0,1],[0,0,0]])
M=S.simplify(M2*M1*M0)
assert S.simplify(M.charpoly().as_expr()-S.Symbol('lambda')**2*(S.Symbol('lambda')-4*a*a*b*b))==0
# Two exact transition parameters and one superattracting value.
assert S.factor(S.Rational(27,4)*t*(t-1)**2-1)==(3*t-4)*(3*t-1)**2/4
assert S.factor(8*t*(t-1)**2-1)==(2*t-1)*(4*t*t-6*t+1)
assert S.factor(S.Rational(125,12)*t*(t-1)**2-1)==(5*t-3)*(25*t*t-35*t+4)/12
assert S.simplify(4*((2*t-1)/(t-1))**2-1-(3*t-1)*(5*t-3)/(t-1)**2)==0
assert S.simplify(4*((2*S.Rational(1,2)-1)/(S.Rational(1,2)-1))**2)==0
# Polynomial of degree d has sharp 2d-1 simple positive roots for kappa=2^(d+3).
# Prove existence in every bounded gap with midpoint rational signs, then use exact degree bound.
for d in range(1,12):
    kap=2**(d+3)
    q=S.prod(t-j for j in range(1,d))
    f=S.expand(kap**2*t*q*q-1)
    assert S.degree(f,t)==2*d-1
    for j in range(1,d):
        assert S.expand(f).subs(t,S.Rational(2*j-1,2))>0
        assert f.subs(t,j-1)==-1
        assert f.subs(t,j)==-1
    assert f.subs(t,d-1)==-1
    assert f.subs(t,d)>0
# One-dimensional exact inequalities for the quadratic phase diagram.
assert S.factor(S.diff(t*(t-1)**2,t))==(t-1)*(3*t-1)
assert S.factor(4*(2*t-1)**2-(t-1)**2)==(3*t-1)*(5*t-3)
print('NILPOTENT_REPEATED_HEIGHT_MULTIPLICITY_AND_PHASE_OK degrees=1..11')
