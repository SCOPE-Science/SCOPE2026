---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The analytic proof is self-contained in `RESULT.md`. Its critical steps are Poisson zero-count multiplication, differentiating the bounded-preference Laplace transform, proving the signed derivative limits at both infinities, clipping a strictly convex minimizer, and applying beta endpoint Laplace asymptotics. These are infinite-domain proofs; finite numerical tests supply only supplementary checks.

Run `python3 verify.py` in a Python 3 installation. The checker uses only the standard library. In this verification run it returned `PASS: 17855 supplementary checks`, including the exact symbolic two-class threshold and optimal survival constant, 100-point effort-grid tests over multiple budgets, exhaustive rational-weight grid distributions, beta numerical integration and the minimax endpoint bound. The beta quadrature root is approximate and is not needed for the theorem.

Scope limits: the hazard intensities are exactly complementary; all efforts are expressed in calibrated, divisible common exposure units; traits are fixed; capture removes an individual; no density dependence or population replenishment is included. The result concerns *expected survivor fraction*. Independent external review has not been performed.
