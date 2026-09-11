#!/usr/bin/env python3
"""Route-B recovery test: can the Dikstein-Dinur local-to-global step yield c=0.01 at q=4?

Recorded DD formula (admission review): h^k >= beta^{k+1}/((k+2)!*4) - e*lambda.
For k=1: h^1 >= beta^2/24 - e*lambda.

Inputs:
  * lambda >= 0.4: certified vertex-link normalized 2nd eigenvalue (=2/5, see
    link_cert_q4.py: NN^T = 4I+J exactly, Spec = {5,-5}x1, {2,-2}x20).
    lambda_actual = max over links >= vertex-link value 0.4 (lower bound suffices).
  * beta <= 2 (universal cap, proved below for regular-graph links; 0-dim links trivially <=2).

Rigorous lower bound e >= 2.718 via partial sum S_7 of exp(1) series (lower bound).
Stdlib only, exact Fraction arithmetic.
"""
from fractions import Fraction
import json
from pathlib import Path

OUT = Path(__file__).with_name("dd_block_result.json")

# e > S_7 = sum_{k=0}^{7} 1/k!  (partial sums of exp(1) are strict lower bounds)
S7 = sum(Fraction(1, __import__("math").factorial(k)) for k in range(8))
assert S7 > Fraction(2718, 1000), S7  # S_7 = 2.71825... > 2.718
E_LOW = Fraction(2718, 1000)

LAM = Fraction(2, 5)   # certified lower bound on DD lambda input
BETA_CAP = Fraction(2)  # universal cap on link coboundary input (lemma below)

# Best case for the DD right-hand side: largest beta, smallest lambda.
rhs_best = BETA_CAP * BETA_CAP / 24 - E_LOW * LAM
print("DD RHS best case (beta=2, lambda=0.4):", float(rhs_best), "=", rhs_best)
assert rhs_best < 0

# To reach target c=0.01 at lambda=0.4 would need beta^2/24 >= 0.01 + e*0.4.
need = Fraction(1, 100) + E_LOW * LAM
beta_needed_sq = 24 * need
print("beta^2 needed for c=0.01 at lambda=0.4: >=", float(beta_needed_sq))
assert beta_needed_sq > 25  # beta > 5, but beta <= 2 -> impossible
print("beta needed: >", float(beta_needed_sq) ** 0.5, " vs universal cap 2")

# Largest lambda DD could tolerate even with beta maxed: lambda < beta^2/(24e).
lam_max = BETA_CAP * BETA_CAP / (24 * E_LOW)
print("max tolerable lambda (beta=2):", float(lam_max), " vs actual >= 0.4")
assert lam_max < Fraction(1, 16)  # < 0.0625 << 0.4

out = {
    "dd_rhs_best_case": str(rhs_best),
    "dd_rhs_best_case_float": float(rhs_best),
    "negative": True,
    "beta_squared_needed_for_c001": float(beta_needed_sq),
    "beta_cap": 2,
    "max_tolerable_lambda": float(lam_max),
    "certified_lambda_lower_bound": 0.4,
    "e_lower_bound_used": 2.718,
    "conclusion": "DD step structurally non-positive at q=4; reaching c=0.01 would need beta>5 > cap 2.",
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=2)
print("DD BLOCK CONFIRMED:", json.dumps(out, indent=2))
print()
print("Lemma (beta<=2): for a d-regular graph link with normalized norms")
print("||dS||=|E(S,Sc)|/|E|, dist(S)=min(|S|,|Sc|)/|V|, a singleton gives")
print("|V|*d/((|V|d/2)*1)=2, and h^0 is a minimum, so h^0<=2.")
