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
Run `python3 verify_endpoint.py` with Python 3 and no external dependencies. The actual embedded script was run and returned three `PASS` statements before the scientific assessment. It constructs a fixed rational Gram approximation and an explicit rational vector, verifies 21 integer fraction-free positive pivots for a rank-one-shifted matrix, obtains a spectral-gap bound, and checks rational endpoint inequalities. Its analytical remainder estimates are stated in the file and in RESULT.md.

The output relates to a 21-dimensional matrix, and therefore does not extrapolate numerical sampling to arbitrarily sized extensions. It does not test physical data noise, estimate real-world measurement variance, or establish the error of a completed quadrature step. Independent auditing has not been performed.
