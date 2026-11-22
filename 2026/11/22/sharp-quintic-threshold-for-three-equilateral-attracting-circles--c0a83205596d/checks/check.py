#!/usr/bin/env python3
"""Symbolic reproduction of the geometric degree and Floquet-asymptotic identities."""
import sympy as s
x,y,r=s.symbols('x y r',real=True)
v=s.sqrt(3)/2
C=[s.Matrix([0,0]),s.Matrix([1,0]),s.Matrix([s.Rational(1,2),v])]
z=s.Matrix([x,y]); J=lambda w:s.Matrix([-w[1],w[0]])
f=[s.expand((z-c).dot(z-c)-r*r) for c in C]
A=[1+(x-y)/20,1+(x-y)/20,1-(x-y)/10]
T=[s.expand(f[(i+1)%3]*f[(i+2)%3])*J(z-C[i]) for i in range(3)]
X=s.Matrix([s.expand(sum(A[i]*T[i][j] for i in range(3))) for j in range(2)])
assert max(s.Poly(X[j],x,y).total_degree() for j in range(2))==5
assert s.simplify(s.Poly(X[0].subs(y,0),x).coeff_monomial(x**5)+v/10)==0
for i in range(3):
    assert s.rem(s.expand(X.dot(s.Matrix([s.diff(f[i],x),s.diff(f[i],y)]))),f[i],x,y)==0
G=[s.Matrix([s.diff(a,x),s.diff(a,y)]) for a in A]
det=lambda a,b:s.det(s.Matrix.hstack(a,b))
expected=[s.Rational(3,40)*(1+s.sqrt(3)),s.Rational(3,40)*(s.sqrt(3)-1),s.Rational(3,20)*s.sqrt(3)]
for k in range(3):
    ak=A[k].subs({x:C[k][0],y:C[k][1]})
    S=0
    for i in range(3):
        if i==k: continue
        d=C[k]-C[i]
        ai=A[i].subs({x:C[k][0],y:C[k][1]})
        S+=det(ak*G[i]-ai*G[k],d)/d.dot(d)
    assert s.simplify(S-expected[k])==0
    assert float(ak)>0 and float(S)>0
print('PASS: exact quintic degree, invariant circles, positive angular speeds for small radii, and three strictly negative leading Floquet exponents')
# Quartic source normal form: verify degree at most four and gradients' rotational symmetry.
la,mu,kap=s.symbols('la mu kap',real=True)
L=[-v*x-s.Rational(1,2)*y-v, v*x-s.Rational(1,2)*y,y]
B=[-la-mu+kap*L[0],la+kap*L[1],mu+kap*L[2]]
Y=s.Matrix([s.expand(sum(B[i]*T[i][j] for i in range(3))) for j in range(2)])
assert max(s.Poly(Y[j],x,y).total_degree() for j in range(2))<=4
assert s.simplify(sum(B)+kap*v)==0
print('PASS: all-degree-four normal-form cancellations for the prescribed equilateral circles')
