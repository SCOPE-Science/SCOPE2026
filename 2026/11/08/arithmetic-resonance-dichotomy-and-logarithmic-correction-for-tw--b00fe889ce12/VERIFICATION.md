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

Run `python3 CHECK.py` with Python 3.10 or later; no external packages are required. The packaged script was executed successfully and returned:

`VERIFY_OK independent_arc_intersections=55 grouped_pair_covariances=90 asymptotic_residual_tests=30 independent_base_exact=True`

The 55 exact window-intersection checks directly enumerate inverse images of short arcs and compare their rational lengths to the closed formula. The 90 finite-variance checks enumerate all pairs of event labels and test their integer determinant, then compare the full covariance sum to the grouped resonance formula. The 30 asymptotic checks test the bounded-correction prediction at several parameter sets and sample sizes, using exact fractions for the variance and floating-point logs only for the boundedness diagnostic.

The true infinite-parameter result follows from the accompanying mathematical proof; bounded finite tests are not an infinite proof. There was no independent expert review or external formal certification. The result does not establish a central limit theorem or generic noninteger-base analogues.
