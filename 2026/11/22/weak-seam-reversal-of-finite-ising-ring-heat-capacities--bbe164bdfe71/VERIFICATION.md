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

The finite-volume calculation is reproduced by `verification.py` using Python 3 and `mpmath` 1.3.0. Execute `python verification.py` in a directory containing this file. The observed output is `SPECIFIC_HEAT_CHECKS_PASSED 143`.

The checks include 24 integer-polynomial factorizations, 72 direct spin-configuration partition sums versus analytical heat-capacity differences, 20 uniform-coupling strict-sign checks, 15 weaker-seam high/low-temperature checks and 12 high-precision weak-defect crossover roots. All-size positivity and the singular crossover come from the analytic identities in RESULT.md; finite experiments are supplementary. Independent scientific audit is not performed.
