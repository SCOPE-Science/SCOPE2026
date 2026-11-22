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

# Reproducibility and limits

Run `python verify.py` using Python 3 and the standard library. The tested command returned `VERIFY_OK 97`. It checks triangular stage substitution against the closed transfer expression, high-stage amplification coefficients, weak damping signs and a quadratic number of repeated steps. Mathematical limiting statements follow from the uniform analytic expansion in RESULT.md, not from finite tests. The asymptotic is not asserted uniformly when the oscillation frequency grows with the stage count.
