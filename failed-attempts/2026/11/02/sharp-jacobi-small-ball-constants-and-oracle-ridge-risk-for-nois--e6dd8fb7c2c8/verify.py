"""Standalone reproducible algebraic and finite-sample checks of the stated affine fitting theorem.

Only Python's standard library is required. The analytic proof, not this checker,
establishes the general asymptotics and the limiting integral constants.
"""
from fractions import Fraction as Q
import math
import random

assert math.isclose(math.gamma(1.5) * math.sqrt(math.pi), math.pi/2, rel_tol=1e-14)
assert math.isclose(math.pi**1.5 / math.gamma(2.5), 4*math.pi/3, rel_tol=1e-14)
assert math.isclose(2 * (4*math.pi/3), 8*math.pi/3, rel_tol=1e-14)

# The exact derivative and minimizing identity for arbitrary rational S,b,var,lambda.
count = 0
for S in (Q(1,11),Q(2,7),Q(1),Q(9,2)):
    for b in (Q(1,3),Q(2),Q(-5,2)):
        for var in (Q(1,20),Q(3,2)):
            lamstar=var/(b*b)
            risk=(b*b*lamstar*lamstar+var*S)/(S+lamstar)**2
            assert risk==var/(S+lamstar)
            for lam in (lamstar/3,lamstar,lamstar*2):
                # Direct quotient-rule differentiation.
                direct=(2*b*b*lam*(S+lam)-2*(b*b*lam*lam+var*S))/(S+lam)**3
                factor=2*(b*b*lam-var)*S/(S+lam)**3
                assert direct==factor
                assert (direct<0 if lam<lamstar else direct>0 if lam>lamstar else direct==0)
                count+=1

# Exact homogeneity of centered sums; this is the source of endpoint scaling.
for seq in ([Q(1),Q(1,2),Q(3),Q(2)], [Q(1,5),Q(2),Q(1,7),Q(5,2)]):
    n=len(seq)
    def S(xs):
        mean=sum(xs)/len(xs)
        return sum((x-mean)**2 for x in xs)
    for scale in (Q(1,7),Q(2),Q(11,3)):
        assert S([scale*x for x in seq]) == scale**2*S(seq)
        count+=1

# Independent elementary calibration: two iid uniform draws have
# P(S<=eps)=2sqrt(2eps)-2eps, 0<eps<1/2.
for eps in (1e-7,1e-5,1e-4):
    formula=2*math.sqrt(2*eps)-2*eps
    leading=2*math.sqrt(2)*math.sqrt(eps)
    assert abs(formula/leading-1) < math.sqrt(eps)
    count+=1

# Separately implemented four-sample uniform-site simulation, not proof.
rng=random.Random(20261031)
N=200000
threshold=0.02
hits=0
for _ in range(N):
    xs=[rng.random() for j in range(4)]
    avg=sum(xs)/4
    hits += (sum((x-avg)**2 for x in xs) <= threshold)
emp=hits/N
leading=(8*math.pi/3)*threshold**1.5
assert 0.65*leading < emp < 1.1*leading, (emp, leading)
print('PASS:',count,'exact algebra/scaling tests; uniform four-site probability',emp,
      'versus first-order coefficient prediction',leading)
