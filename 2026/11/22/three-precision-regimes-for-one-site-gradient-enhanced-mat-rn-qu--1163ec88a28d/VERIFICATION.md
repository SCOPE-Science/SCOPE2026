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

The exact posterior-variance reduction and its two channel contributions are derived from the Matérn covariance, not fitted from simulated paths. The proof establishes exact global small-budget and high-budget allocation classes through compactness and strict derivative inequalities, and establishes the intermediate-budget mixed necessity using exact rational lower bounds.

To reproduce supplementary numerical checks, run `python verify.py` (Python 3 standard library only). It verifies the exact positive comparison margins with rational arithmetic, evaluates 48 direct numerical covariance integrals, compares 240 conditioning formulas, and checks monotonicity on finite grids. Those numerical checks are not substitutes for the continuum proofs.

Limits: no exact phase boundary, no closed form for the mixed optimum, no changing channel units/costs or separate-site derivative sensors. Independent validation has not been performed.
