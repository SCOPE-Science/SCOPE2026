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

The analytic proof and complete bounds are in RESULT.md. Reproduce with `python verify.py` using Python 3 standard library. The checker recomputes rational polynomial identities, discriminant and threshold orders, evaluates uniqueness by derivative bisection, and runs 64,800 finite supplementary objective comparisons. The proof, not numerical tests, establishes all-budget claims. Values are hypothetical rates and have not been independently validated or empirically calibrated.
