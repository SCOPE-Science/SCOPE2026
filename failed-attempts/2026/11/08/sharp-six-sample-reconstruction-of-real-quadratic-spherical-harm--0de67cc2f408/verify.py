#!/usr/bin/env python3
"""Exact finite-reduction checks for quadratic spherical-harmonic sampling.

Requires SymPy. The proof of global angular optimality is analytic, not
an inference from the sample checks in this script.
"""
import sympy as s

T = s.symbols('T', nonnegative=True, real=True)
x,y,z=s.symbols('x y z',real=True)
H=[s.sqrt(15)*x*y,s.sqrt(15)*x*z,s.sqrt(15)*y*z,
   s.sqrt(15)/2*(x*x-y*y),s.sqrt(5)/2*(x*x+y*y-2*z*z)]

def expected(t):
    return s.Matrix([
      [s.Rational(45,32)*(1-t*t),0,0,0,0],
      [0,s.Rational(15,16)*(1-t),0,0,0],
      [0,0,s.Rational(15,16)*(1+t),0,0],
      [0,0,0,s.Rational(45,32)*t*t,-5*s.sqrt(3)*t/32],
      [0,0,0,-5*s.sqrt(3)*t/32,s.Rational(55,32)]])

def direct_triangle_frame(t,phase0,phase1):
    c=s.sqrt((1+t)/2); d=s.sqrt((1-t)/2)
    cols=[]
    for sign,phase in ((1,phase0),(-1,phase1)):
        for j in range(3):
            u=phase+2*s.pi*j/3
            pt={x:-sign*d*s.sin(u),y:c*s.sin(u),z:s.cos(u)}
            cols.append(s.Matrix([s.trigsimp(expr.subs(pt, simultaneous=True))
                                  for expr in H]))
    return s.simplify(sum((v*v.T for v in cols),s.zeros(5))/6)

cases=[(s.S(0),s.S(0),s.S(0)),(s.Rational(1,3),s.pi/6,s.pi/4),
       (s.Rational(5,9),s.S(0),s.pi/6),
       (s.Rational(3,4),s.pi/4,s.S(0)),(s.S(1),s.pi/6,s.pi/6)]
for t,a,b in cases:
    gram=direct_triangle_frame(t,a,b)
    for i in range(5):
        for j in range(5):
            assert s.simplify(gram[i,j]-expected(t)[i,j])==0,(t,i,j,gram[i,j])
print('EXACT_THREE_PER_CIRCLE_QUADRATURE_AND_GRAM_OK',len(cases), 'angles',len(cases)*2)

# Independently derive the formula for the single-circle fourth tensor
# and average across the pair; this is algebraically distinct from
# the equilateral-triple sampling used above.
A=[s.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
   s.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
   s.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
   s.diag(1,-1,0),s.diag(1,1,-2)]
norm=[s.sqrt(s.Rational(15,4))]*4+[s.sqrt(s.Rational(5,4))]
c=s.sqrt((1+T)/2);d=s.sqrt((1-T)/2)
def pair_moment(i,j):
    acc=0
    for sign in (1,-1):
        n=s.Matrix([c,sign*d,0]);P=s.eye(3)-n*n.T
        # E[(u^T Au)(u^T Bu)] = (tr(PA)tr(PB)+2tr(PAPB))/8
        acc+=(s.trace(P*A[i])*s.trace(P*A[j])+2*s.trace(P*A[i]*P*A[j]))/16
    return s.simplify(norm[i]*norm[j]*acc)
for i in range(5):
    for j in range(5):
        assert s.simplify(pair_moment(i,j)-expected(T)[i,j])==0,(i,j)
print('INDEPENDENT_CIRCLE_FOURTH_MOMENT_TENSOR_OK',25)

M=expected(T)[3:5,3:5]
b=s.Rational(15,16)*(1-T)
assert s.factor((M-b*s.eye(2)).det())==75*(T+1)**2*(9*T-5)/512
assert s.simplify(M.det()-s.Rational(75,32)*T*T)==0
assert s.simplify(s.trace(M)-(45*T*T+55)/32)==0
star=s.Rational(5,9)
E=expected(star)
assert sorted(E.eigenvals().items(),key=lambda q:q[0])==[
    (s.Rational(5,12),2),(s.Rational(35,36),1),
    (s.Rational(35,24),1),(s.Rational(125,72),1)]
# Sharp equality directions are e2 and the specified diagonal combination.
vec=s.Matrix([0,0,0,5*s.sqrt(3),1])
assert E*vec==s.Rational(5,12)*vec
assert E*s.eye(5)[:,1]==s.Rational(5,12)*s.eye(5)[:,1]
assert s.Rational(35,36)-s.Rational(5,12)==s.Rational(5,9)
print('EXACT_OPTIMAL_ANGLE_EIGENSPACE_AND_STABILITY_GAP_OK',star,'value',s.Rational(5,12))

# The least eigenvalue from the 2x2 block is strictly increasing because
# 0<=lambda_-<=45/32<5/3; the decreasing scalar branch crosses it once.
assert s.Rational(45,32)<s.Rational(5,3)
assert s.simplify(M.subs(T,0).det())==0
assert E.is_symmetric()
print('ALL_TWO_GREAT_CIRCLE_SAMPLING_CHECKS_OK')
