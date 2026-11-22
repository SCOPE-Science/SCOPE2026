"""Finite rational identities and scalar regularization checks for a 3-state driven ring."""
from fractions import Fraction as F
from math import asinh, sqrt, log
Q0 = [[F(-2),F(1),F(1)],[F(1),F(-2),F(1)],[F(1),F(1),F(-2)]]
Qp = [[F(-2),F(3,2),F(1,2)], [F(-1,2),F(0),F(1,2)], [F(1,2),F(-1,2),F(0)]]
p0 = [F(1,3)]*3
pd = [F(-2,9),F(1,9),F(1,9)]
assert all(sum(p0[i]*Q0[i][j] for i in range(3))==0 for j in range(3))
assert all(sum(pd[i]*Q0[i][j]+p0[i]*Qp[i][j] for i in range(3))==0 for j in range(3))
assert sum(pd)==0
for i in range(3):
    j=(i+1)%3
    flux_deriv = pd[i]*Q0[i][j]+p0[i]*Qp[i][j]-pd[j]*Q0[j][i]-p0[j]*Qp[j][i]
    assert flux_deriv == F(1,3), (i,j,flux_deriv)
score = [pd[i]/p0[i] for i in range(3)]
assert score == [F(-2,3), F(1,3), F(1,3)]
assert all(sum(Q0[i][j]*score[j] for j in range(3))==-3*score[i] for i in range(3))
zeta0 = sum(p0[i]*score[i]**2 for i in range(3))/3
assert zeta0==F(2,27)
# For exactly sigma=x^2, zeta=1, endpoints +/-1, budget B=2:
# J=a sqrt(a^2+eps^2)-eps^2 asinh(a/eps)
# K=a sqrt(a^2+eps^2)+eps^2 asinh(a/eps).
B=2.0; a=1.0; past_error=1.0
for eps in [0.2,0.1,0.05,0.02,0.01,0.005,0.002]:
    J=a*sqrt(a*a+eps*eps)-eps*eps*asinh(a/eps)
    K=a*sqrt(a*a+eps*eps)+eps*eps*asinh(a/eps)
    E=J*K/B
    T=(B/J)*2*asinh(a/eps)
    error=B*E-a**4
    assert 0<error<past_error
    assert abs(error-(a*a*eps*eps-eps**4*asinh(a/eps)**2))<1e-12
    assert T>0
    past_error=error
print('PASS: stationary perturbation, three edge currents, friction, regularized-bound approach')
print('exact equilibrium friction=',zeta0, 'smallest tested excess gap=',past_error/B)
