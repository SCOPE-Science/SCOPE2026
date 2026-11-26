#!/usr/bin/env python3
from fractions import Fraction as F

beta = F(3, 1_000_000)
Lambda = F(5)
d = F(4, 100_000)
nu = F(2, 10)
alpha = F(1, 100_000)
lam = F(12, 1000)
lam0 = F(8, 1000)
p = F(1200)
M0 = F(500)

R0 = beta*Lambda/(d*(nu+alpha+d))
c = lam0+d
assert R0 == F(7500,4001)
assert c == F(201,25000)

def R1(M):
    return R0*c*(p+M)/(lam*M+c*(p+M))

# Strict derivative numerator is -R0*c*lam*p.
assert -R0*c*lam*p < 0

limit_R1 = R0*c/(lam+c)
barrier = (R0-1)*c
assert lam > barrier

Mcrit = (R0-1)*c*p/(lam-barrier)
assert R1(Mcrit) == 1
assert R1(F(500)) > 1
assert R1(F(2000)) < 1

lamcrit_500 = (R0-1)*c*(p+M0)/M0
assert lam < lamcrit_500

# Equality case: if lam_eq=(R0-1)c, every finite baseline remains above one.
lam_eq = barrier
def R1_eq(M):
    return R0*c*(p+M)/(lam_eq*M+c*(p+M))
for M in (F(0),F(1),F(500),F(10**9)):
    assert R1_eq(M) > 1

print("VERIFY_OK")
print("R0", float(R0))
print("floor_R1", float(limit_R1))
print("barrier_lambda", float(barrier))
print("M0_critical", float(Mcrit))
print("R1_at_500", float(R1(F(500))))
print("lambda_critical_at_500", float(lamcrit_500))
