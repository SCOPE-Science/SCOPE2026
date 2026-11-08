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

Run `python3 verify_polya.py` in the same folder as the extracted files. The checker requires only Python's standard library. It independently enumerates Dirichlet-multinomial probability distributions of finite weak compositions with rational concentrations, compares mixed moments to the closed covariance formula, tests the strict ratio recurrence and the exact `alpha=1` zero-crossing classification. The actual fresh run passed 36,936 exact rational comparisons.

This is a finite test, not a computational proof for real concentrations or all sizes. The analytic proof derives all hypotheses and limiting claims in RESULT.md. There is no external independent audit or formal certification.
