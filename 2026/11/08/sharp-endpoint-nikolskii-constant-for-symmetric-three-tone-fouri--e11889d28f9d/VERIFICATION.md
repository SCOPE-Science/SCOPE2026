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

The exact orthogonal-basis Gram computation, strict analytic bounds and collision Taylor expansion appear in `RESULT.md`. Independently evaluate the fixed-gap formula in `CHECK.py`; invoke `python3 CHECK.py` using only Python's standard library. The test checks multiple positive gaps, complex coefficient vectors and exact low-order Taylor coefficients in the closed-form trigonometric remainder.

The finite tests do not establish the global inequality: that rests on the proved positivity of \(H(t)\) for all \(t>0\) and \(F(t)\) for all \(t>0\), including both frequency regimes. The sharp limiting constant follows from exact Taylor coefficients, not finite numerical extrapolation. No independent audit or external validation has been performed.
