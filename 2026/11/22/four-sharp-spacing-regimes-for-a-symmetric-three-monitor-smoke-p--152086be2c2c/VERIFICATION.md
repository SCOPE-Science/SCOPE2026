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

The proof is analytic: partition by the number of active footprints, differentiate each of the three exact formulas, and compare the strictly decreasing Gaussian density ratio against \(q^2\) and \(q\). The checker is supplementary rather than a substitute for these steps.

Reproduce finite numerical checks using `python checker.py` (Python standard library). Observed result: `PASS: 97444 finite numerical assertions; four analytic regimes sampled`.

The theorem proves only the symmetry-constrained objective for positive \(r,\sigma\) and \(p\in(0,1)\); it does not identify optimal unconstrained monitor locations or model practical calibration, alarm specificity, correlated errors, or changing meteorology. No independent audit has been performed.
