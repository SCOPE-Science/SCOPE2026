"""Verify sharpness lower bound: optimal universal thin-shell constant C* >= 8.

Witness: X in R^n with i.i.d. coordinates X_i = Y_i - 1, Y_i ~ Exp(1) i.i.d.
Checks (exact integer arithmetic where possible):
 - E[Y^k] = k! for Y ~ Exp(1)
 - E[X_1] = 0, Var(X_1) = 1  -> product law isotropic
 - E[X_1^4] = 9 -> Var(X_1^2) = 8 -> Var(|X|^2) = 8n by independence
 - log-concavity: qualitative (density exp(-(x+1)) on [-1,inf), log-linear
   on convex support; product preserves log-concavity) -- stated, not computed.
 - Gaussian (C=2) and cube (C=4/5) sanity checks.
"""
from math import comb, factorial

def exp_raw(m):
    return factorial(m)  # E[Y^m] for Y ~ Exp(1)

# E[(Y-1)^4] by binomial expansion, exact integers
E4 = sum(comb(4, j) * ((-1) ** (4 - j)) * exp_raw(j) for j in range(5))
mean = exp_raw(1) - 1
var = exp_raw(2) - 2 * exp_raw(1) + 1 - mean ** 2  # E[(Y-1)^2]
var_X1sq = E4 - 1  # (E X_1^2)^2 = 1 since Var(X_1)=1, mean 0
print("E[(Y-1)^4] =", E4)
print("mean(X1) =", mean)
print("Var(X1) =", var)
print("Var(X1^2) =", var_X1sq)
assert E4 == 9
assert mean == 0
assert var == 1
assert var_X1sq == 8

# Gaussian and cube sanity
print("Gaussian Var(Z^2) =", 3 - 1)
a2 = 3  # cube half-side squared; E X^4 = a^4/5 = 9/5
print("cube Var(X1^2) =", 9 / 5 - 1, "= 4/5:", 9 / 5 - 1 == 4 / 5)

print("OK: product of shifted exponentials gives Var(|X|^2) = 8n exactly.")
print("Hence any universal upper bound Var <= C n must have C >= 8.")
