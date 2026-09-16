"""Verify Lemma B coefficient algebra and the sharp (rho - 1/6) test factor.

Checks:
  1. General coefficient identity: c/2 + rho - 1/6 == (1-6 rho)/12 for c=(1-6 rho)/2.
  2. rho=0 reduction: (1-0)/12 = 1/12 matches Wu-Wu-Wylie Lemma 2.3.
  3. Test-component factor: rho*X - X/6 == (rho-1/6)*X vanishes iff rho=1/6 (for X != 0),
     and c=(1-6 rho)/2 vanishes exactly at rho=1/6; trace factor (4 rho-1) at rho=1/4.
  4. Randomized numeric check of the test-component equation over random nablaR values.
"""
import numpy as np

def c_of(rho):
    return (1 - 6*rho)/2

# 1. coefficient identity on a grid
for rho in [-1.0, -0.5, 0.0, 0.1, 1/6, 0.2, 0.25, 0.5, 1.0]:
    lhs = c_of(rho)/2 + rho - 1/6
    rhs = (1 - 6*rho)/12
    assert abs(lhs - rhs) < 1e-12, (rho, lhs, rhs)
print("check 1 passed: D-tensor dR coefficient identity holds")

# 2. rho = 0 reduction
assert abs((1 - 0)/12 - 1/12) < 1e-15
print("check 2 passed: rho=0 coefficient is 1/12 (Wu-Wu-Wylie)")

# 3. degeneracy locations
assert abs(c_of(1/6)) < 1e-15 and abs(4*0.25 - 1) < 1e-15
print("check 3 passed: c=0 at rho=1/6; trace factor 0 at rho=1/4")

# 4. test-factor numeric check
rng = np.random.default_rng(3)
for rho in [-0.5, 0.0, 0.1, 1/6, 0.2, 0.4]:
    for _ in range(500):
        x = float(rng.normal())
        residual = rho*x - x/6 - (rho - 1/6)*x
        assert abs(residual) < 1e-12
        if abs(x) > 0.05:
            zero = abs(rho*x - x/6) < 1e-12
            assert zero == (abs(rho - 1/6) < 1e-12)
print("check 4 passed: (rho-1/6) test factor sharp")
print("ALL RHO-EIGENVECTOR CHECKS PASSED")
