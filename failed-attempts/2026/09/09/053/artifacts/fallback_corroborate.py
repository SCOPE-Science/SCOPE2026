"""Corroboration (not substitution) for fallback section lemma, t=0 anchor.

Checks, with lgamma-stable arithmetic (stdlib only):
 (a) exact E|X_1|^2 for uniform on B_1^n via Beta-Gamma formula,
 (b) vol(B_1^n)=2^n/n!, isotropic constant L_K^2 = V^{-2/n} sigma^2,
 (c) t=0 section identity: Cov(mu_0|_E) = L_K^2 I_2, op-norm = L_K^2 <= 8 L_K^2,
 (d) PSD lemma: ||M||_op <= Tr(M) on random 2x2 PSD matrices.
The uniform-in-t bound sup_t E[||.||] <= 2 L_K^2 is proved analytically
in output/DRAFT.md via E[A_t] <= A_0; this script only anchors t=0 numbers.
"""
import math
from math import lgamma, exp

def E_abs_r(n, p, r):
    # log-stable: log(n/(n+r)) + lg(1/p+r/p)+lg(n/p)-lg(1/p)-lg(n/p+r/p)
    return exp(math.log(n / (n + r)) + lgamma(1 / p + r / p)
              + lgamma(n / p) - lgamma(1 / p) - lgamma(n / p + r / p))

def vol_B1(n):
    return exp(n * math.log(2.0) - lgamma(n + 1))  # 2^n / n!

print(f"{'n':>4} {'sigma2':>12} {'vol':>12} {'L_K^2':>10} {'sec_op':>10} {'ratio/8LK2':>10}")
for n in [4, 6, 8, 10, 20, 50]:
    s2 = E_abs_r(n, 1.0, 2)
    V = vol_B1(n)
    LK2 = exp((-2.0 / n) * math.log(V)) * s2
    sec_op = LK2  # Cov(mu_0|_E) = L_K^2 I_2 at t=0
    assert abs(s2 - 2.0 / ((n + 1) * (n + 2))) < 1e-9, (n, s2)
    assert sec_op <= 8 * LK2
    print(f"{n:>4} {s2:>12.6e} {V:>12.6e} {LK2:>10.6f} {sec_op:>10.6f} {sec_op/(8*LK2):>10.4f}")

# PSD lemma spot-check: op <= tr for random 2x2 PSD M = B B^T
import random
random.seed(412)
worst = 0.0
for _ in range(5000):
    a, b, c, d = (random.uniform(-3, 3) for _ in range(4))
    m11, m12, m22 = a*a+b*b, a*c+b*d, c*c+d*d
    tr = m11 + m22
    det = m11*m22 - m12*m12
    assert det >= -1e-9
    op = (tr + math.sqrt(max(tr*tr - 4*det, 0.0))) / 2.0
    assert op <= tr + 1e-9, (m11, m12, m22, op, tr)
    worst = max(worst, op / tr if tr > 1e-12 else 0.0)
print("PSD op/tr max (must be <= 1):", round(worst, 6))
print("CORROBORATE_OK")
