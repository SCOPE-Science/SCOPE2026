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

A standalone standard-library Python checker (`verify.py`) was executed from the exact accompanying source file. It reported `VERIFY_OK 1383 test cases` and recovered the stated approximate tangency for \(a=3,b=1\). It verifies exact rational two-by-two matrix products, trace and determinant identities, a factorized characteristic polynomial, an exact strict-benefit witness, and a separate exact double-root certificate. Additional numerical checks cover three growth-contrast ratios and multiple migrant-survival values.

The complete real-parameter theorem is proved analytically in `RESULT.md`: a matrix square reduction, strict convexity of a cubic, continuity, and strict pointwise Perron-monotonicity. The finite checks do not prove these general statements. Computed numerical roots are approximations, not proofs of exact rational equality; the exact algebraic tangency equations define the threshold.

The scientific comparison includes full-text review of accessible primary sources and relevant published mathematical results. An unrecognized earlier equivalent positive-matrix theorem remains a possible priority risk. No independent external scientific audit or validation has been performed.
