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

The analytic proof in `RESULT.md` establishes the formulas and monotonicity for every admissible odd order, independently of any finite experiment. `verify.py` is a standalone Python 3 standard-library check that constructs the circular-arc boundary explicitly and compares the complete ordered-pair distance quadrature with both moment formulas. Command: `python3 verify.py`. It reports `PASS: 121 assertions; direct boundary quadrature and formula agree`.

The numerical midpoint quadrature is approximate, using explicitly specified tolerances. The strict all-order ordering is established by the derivative and variance arguments in the proof, not by the finite numerical side-count loop. The Taylor coefficients were also independently checked using formal symbolic series; the code does not purport to certify an infinite asymptotic expansion. The exact inverse uses ideal population moments; finite-sample measurement stability remains unproved.
