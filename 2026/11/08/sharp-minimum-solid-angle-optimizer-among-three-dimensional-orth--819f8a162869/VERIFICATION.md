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

# Verification of the orthoscheme solid-angle maximum
The independent numerical verifier runs as `python verify.py` from the extracted package. It uses an explicit vector determinant and cross-product formula for each of four vertex cones, with a different code path from the factored analytic endpoint formulas. It tests 20,000 positive length triples over eight log-scale units and compares the minimum to the asserted constant. It additionally numerically differentiates the symmetric one-parameter half-angle tangent at 1,000 test ratios, checking the exact analytic derivative, and tests the optimizing ratio.

Observed result: `ORTHOSCHEME_MAXIMIN_OK 21000 sharp_min_steradians 0.2756427992162654`.

No sampling, however extensive, establishes an all-real-variable inequality. The complete proof in RESULT.md uses monotonicity on a fixed sphere and an exact derivative sign, establishing all positive triples and uniqueness.

Limits: inputs are Euclidean orthoschemes of dimension three with strictly positive successive path lengths. Independence refers only to the coding method, not to a separate scientific audit. Historical-priority checking is provisional.
