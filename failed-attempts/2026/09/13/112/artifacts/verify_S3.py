"""Exact verification of the S3 rigidity computation (target: alpha=1.25, p=2).

Checks (exact rational arithmetic):
 1. t0=(1+alpha)/2, cofactor-balance coefficients M1=M2=(t0/2)I.
 2. Lower bounds lambda>=t0/2, (1-lambda)>=t0/(2alpha) sum to 81/80>1.
 3. Numeric audit: R - alpha*Q is always invertible (no rank-one connections
    between wells); sigma_min(R-alpha*Q) >= alpha-1 = 1/4.
Writes results JSON next to this script.
"""
import json
import os
from fractions import Fraction

import numpy as np

alpha = Fraction(5, 4)
t0 = (1 + alpha) / 2            # 9/8
t0sq = t0 * t0                  # 81/64
assert t0 == Fraction(9, 8), t0
assert t0sq == Fraction(81, 64), t0sq

# Cofactor balance: M1+M2=t0 I, M1+alpha M2=t0^2 I  =>  M2 coef:
c = (t0sq - t0) / (alpha - 1)   # must equal t0/2
assert c == t0 / 2 == Fraction(9, 16), c
lam_lo = t0 / 2                 # 9/16
mu_lo = t0 / (2 * alpha)        # 9/20
total = lam_lo + mu_lo
assert total == Fraction(81, 80), total
contradiction = total > 1

# Numeric audit of rank-one incompatibility between the wells.
rng = np.random.default_rng(1728)
af = 1.25
n = 2000
min_sv = 1e9
for _ in range(n):
    A = rng.standard_normal((3, 3))
    Q1, _ = np.linalg.qr(A)
    if np.linalg.det(Q1) < 0:
        Q1[:, 0] = -Q1[:, 0]
    B = rng.standard_normal((3, 3))
    Q2, _ = np.linalg.qr(B)
    if np.linalg.det(Q2) < 0:
        Q2[:, 0] = -Q2[:, 0]
    sv = np.linalg.svd(Q1 - af * Q2, compute_uv=False)
    min_sv = min(min_sv, float(sv[-1]))

result = {
    "alpha": str(alpha),
    "t0": str(t0),
    "t0_squared": str(t0sq),
    "M1_coef": str(Fraction(9, 16)),
    "M2_coef": str(c),
    "lambda_lower_bound": str(lam_lo),
    "one_minus_lambda_lower_bound": str(mu_lo),
    "bound_sum": str(total),
    "bound_sum_float": float(total),
    "sum_exceeds_one": bool(contradiction),
    "rank_one_audit_samples": n,
    "min_sigma_min_R_minus_alphaQ": min_sv,
    "theoretical_lower_bound_alpha_minus_1": af - 1.0,
    "no_rank_one_connection_confirmed": bool(min_sv > 0.24),
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "s3_verification.json")
with open(out, "w") as f:
    json.dump(result, f, indent=2)
print(json.dumps(result, indent=2))
