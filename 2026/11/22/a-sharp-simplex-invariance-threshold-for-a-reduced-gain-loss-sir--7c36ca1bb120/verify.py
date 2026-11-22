"""Exact-rational diagnostics for the SIR simplex-invariance theorem.

This verifies finite symbolic identities and sampled witnesses, not universal
quantifiers. The latter are supplied by the mathematical proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def step(s, i, rho, tau):
    s_new = s / (1 + tau * rho * i)
    i_new = i * (1 + tau * rho * s) / (1 + tau)
    return s_new, i_new, 1 - s_new - i_new


def boundary_expression(i, rho, tau):
    return tau * i * (1 + tau * rho - tau * rho * rho * i * (1-i)) / ((1+tau)*(1+tau*rho*i))


def criterion(rho, tau):
    return tau * rho * (rho-4) <= 4

checks = 0
# The rational boundary identity, including normalized simplex sum.
for rho, tau, i in product([F(1,2),F(1),F(4),F(9,2),F(5),F(7)],
                            [F(1,10),F(1,2),F(1),F(2),F(5)],
                            [F(0),F(1,8),F(1,3),F(1,2),F(3,4),F(1)]):
    s1, i1, r1 = step(1-i, i, rho, tau)
    assert r1 == boundary_expression(i, rho, tau)
    assert s1 + i1 + r1 == 1
    checks += 2

# Global sharp classification on exact finite rational simplex grids.
fractions = [F(k,24) for k in range(25)]
for rho, tau in product([F(1,2),F(1),F(2),F(4),F(9,2),F(5),F(6),F(10)],
                        [F(1,20),F(1,4),F(1,2),F(1),F(2),F(4)]):
    for i in fractions:
        for s in fractions:
            if s+i > 1:
                continue
            sp, ip, rp = step(s,i,rho,tau)
            assert sp >= 0 and ip >= 0 and sp+ip+rp == 1
            if criterion(rho,tau):
                assert rp >= 0
            checks += 1
    if not criterion(rho,tau):
        assert step(F(1,2),F(1,2),rho,tau)[2] < 0
        checks += 1

assert step(F(1,2),F(1,2),F(5),F(1)) == (F(1,7),F(7,8),F(-1,56))
checks += 1
# At rho=5 the critical tau is 4/5: equality but no negative value.
assert step(F(1,2),F(1,2),F(5),F(4,5))[2] == 0
checks += 1
assert step(F(1,2),F(1,2),F(4),F(100))[2] > 0
checks += 1

# Exact unsafe boundary interval at rho=8, tau=1/4:
# its discriminant is 1/4 and the endpoints are i=1/4,3/4.
rho, tau = F(8), F(1,4)
disc = 1 - F(4)/rho - F(4)/(tau*rho*rho)
assert disc == F(1,4)
for i in (F(1,4), F(3,4)):
    assert step(1-i, i, rho, tau)[2] == 0
    checks += 1
assert step(F(1,2), F(1,2), rho, tau)[2] < 0
checks += 2

print(f"PASS: {checks} exact-rational assertions; universal claims rest on the proof")
