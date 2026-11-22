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

# Reproducibility

Run `python check_ferrers_three_step.py` with Python 3.9 or newer (standard library only). The checker enumerates all six positive integer group sizes in \(\{1,2,3,4\}\), computes each multiplier using exact rational arithmetic, and checks positivity, the two KKT complementarity conditions, the exact center norm, the affine coordinate sums, every edge-cell squared-distance clearance, and all four possible multiplier-support phases. It separately checks the worked example. Its expected completion message is `THREE_STEP_FERRERS_EXACT_PASS 4096 regimes 4`.

A preliminary separate floating-point enumeration tested every tuple in \(\{1,2,3,4,5\}^6\), with 15625 cases; that computation is not required for reproduction and is not a substitute for the all-parameter proof. The analytic proof uses the equal-norm minimum-sphere lemma, a standard network-flow characterization, and convex quadratic KKT conditions. No independent expert mathematical audit has occurred.
