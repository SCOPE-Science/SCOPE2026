#!/usr/bin/env python3
"""Fallback recovery test: can ANY recorded local-to-global template yield even the
weak fallback bound at the certified q=4 parameters (lambda=0.4)?

Templates checked (all in exact Fraction arithmetic, stdlib only):
  T1. Dikstein-Dinur: h^1 >= beta^2/24 - e*lambda, beta<=1 (correct graph-link cap:
      singleton cut gives normalized expansion <=1), e>=2.718 (S_7 lower bound).
  T2. Tolerable-lambda ceiling: largest lambda with DD RHS>=0 over beta<=1.
  T3. Oppenheim trickling-down: mu = lambda/(1-lambda) at lambda=0.4 (real 1-skeleton
      gap only; records that it yields no F2-coboundary constant).
  T4. Cleaning/inj-radius scale: best bound of that shape is O(log m); records the
      exponent gap to the required m/log(m) scale (needs expansion input, i.e. T1).

Verdict logic: if max DD RHS < 0 and ceiling << 0.4, the weak bound cannot come from
a linear-then-weaken route either (no linear input exists), and no direct m/log
template is recorded -> fallback part (2) blocked.
"""
from fractions import Fraction
import json
from pathlib import Path

OUT = Path(__file__).with_name("fallback_feasibility_result.json")

E_LOW = Fraction(2718, 1000)  # e > S_7 = 2.71825...
LAM = Fraction(2, 5)          # certified vertex-link normalized 2nd eigenvalue
BETA_CAP = Fraction(1)        # normalized graph-link expansion <= 1

# T1: best-case DD RHS at q=4
rhs_best = BETA_CAP * BETA_CAP / 24 - E_LOW * LAM
# T2: ceiling: beta^2/24 >= e*lam  ->  lam <= 1/(24e)
lam_ceiling = BETA_CAP * BETA_CAP / (24 * E_LOW)
# T3: trickling
mu = LAM / (1 - LAM)
# T4: scale gap statement (analytic, recorded here as numbers):
# cleaning gives O(rho) with rho ~ log_{41}(m); required m/log(m). No computation needed.

print("T1 DD RHS best case (beta=1, lambda=0.4):", float(rhs_best), "=", rhs_best)
print("T2 max tolerable lambda:", float(lam_ceiling))
print("   gap factor actual/ceiling:", float(LAM / lam_ceiling))
print("T3 trickling mu = 0.4/0.6 =", float(mu), "(real skeleton gap only, no F2 constant)")

assert rhs_best < 0
assert lam_ceiling < Fraction(2, 100)  # ceiling below 0.02
assert LAM / lam_ceiling > 20          # gap factor exceeds 20x
assert mu == Fraction(2, 3)

out = {
    "certified_lambda": 0.4,
    "T1_dd_rhs_best_case": str(rhs_best),
    "T1_dd_rhs_float": float(rhs_best),
    "T1_negative": True,
    "T2_max_tolerable_lambda_float": float(lam_ceiling),
    "T2_gap_factor": float(LAM / lam_ceiling),
    "T3_trickling_mu": str(mu),
    "T3_yields_F2_coboundary": False,
    "T4_cleaning_scale": "O(log m); cannot reach m/log(m) without expansion input (circular)",
    "verdict": "No recorded template yields any positive F2-cosystolic input at lambda=0.4; "
               "linear-then-weaken is unavailable (no linear input), direct m/log template absent. "
               "Fallback part (2) BLOCKED.",
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=2)
print("FALLBACK RECOVERY TEST:", json.dumps(out, indent=2))
