"""Reproducible exact checks for a radial-law circulation envelope.

Analytical proofs of the general theorem are given in RESULT.md; numerical
checks in this file do not substitute for those proofs.
"""
from fractions import Fraction as F
import sympy as sp

# Exact covariance balancing for the two radial laws in the example:
low_weight, high_weight = F(9, 10), F(1, 10)
low_radius2, high_radius2 = F(1), F(9)
assert low_weight*low_radius2 == high_weight*high_radius2
m = (low_weight*low_radius2+high_weight*high_radius2)/2
assert m == F(9, 10)
angular_envelope = low_weight - high_weight
assert angular_envelope == F(4, 5)

# The sharp dual expression min_{a>=0} E|1-aS| is flat on [1/9,1].
for a in [F(1, 9), F(1, 7), F(1, 2), F(1)]:
    dual = low_weight*abs(1-a*low_radius2)+high_weight*abs(1-a*high_radius2)
    assert dual == F(4, 5)
for a in [F(0), F(1, 20), F(7, 5)]:
    dual = low_weight*abs(1-a*low_radius2)+high_weight*abs(1-a*high_radius2)
    assert dual > F(4, 5)

# Symbolic stationary second-moment solution and eigenvalue stability.
r,u,tx,ty,mv=sp.symbols('r u tx ty mv', positive=True)
a,b,c=sp.symbols('a b c', real=True)
sol=sp.solve([
 (r+2)*a+2*u*c-r*mv-2*tx,
 (r+2)*b+2*u*c-r*mv-2*ty,
 (r+2)*c+u*(a+b)
], [a,b,c], dict=True)[0]
assert sp.simplify(sol[b]-sol[a]-2*(ty-tx)/(r+2)) == 0

# Full stationary lag covariance is exactly matrix-valued exp(-(K+rI)tau)
# because the centered reset law makes the conditional future mean linear.
# Here a finite-dimensional exact generator check at generic rational parameters.
K=sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]])
r0=sp.Rational(5)
C=sp.Matrix([[sol[a],sol[c]],[sol[c],sol[b]]]).subs({r:r0,u:sp.Rational(1,2),tx:1,ty:3,mv:sp.Rational(9,10)})
C=sp.simplify(C)
D=sp.diag(1,3)
assert K*C+C*K+r0*C == r0*sp.Rational(9,10)*sp.eye(2)+2*D
assert C.det()>0 and C[0,0]>0

# Rigorous explicit r=5000 angular sign certificate:
# |E g(Z_r)-E g(R)| <= 8 [(1+u)*3/r + sqrt(4Ty/r)]
# < 8(9/10000+1/20) = 509/1250 < 4/5,
# since sqrt(12/5000) < 1/20.
rate = F(5000)
assert F(12,5000) < F(1,20)**2
bound=8*(F(9,10000)+F(1,20))
assert bound == F(509,1250) and bound < F(4,5)
assert F(4,5)-bound == F(491,1250)
print('PASS: exact reset-radius balancing, dual envelope, covariance, and finite-rate angular sign bound')
