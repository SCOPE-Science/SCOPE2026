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

# Verification record

Running `python3 checker.py` from the extracted directory gives six exact comparisons between independent labeled and reduced finite-state calculations for \(m=2,3,4,5,6,7\), plus two explicit base-value checks and thousands of exact-rational inequalities across the one-tag, two-tag, upper-bound, and lower-bound proof steps.

The pre-package execution reported `verified 2985 exact assertions`, with the finite probabilities \(0,1/5,8/65,1231/11375,562248/6062875,634107503/7766542875\) for \(m=2,3,4,5,6,7\). The checker only verifies finite cases; the asymptotic \(3/4\) follows analytically from the telescoping estimates in `RESULT.md`.

No independent audit or external validation is asserted.
