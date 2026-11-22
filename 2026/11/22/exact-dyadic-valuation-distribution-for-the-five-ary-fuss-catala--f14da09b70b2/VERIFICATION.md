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

# Verification and limits

Run `python3 verify.py` from the extracted files. It checks the exact eight-coordinate polynomial identity and the direct valuation histograms for 16 dyadic lengths, with 127 exact Fuss–Catalan evaluations. Actual output: `VERIFY_OK symbolic_polynomial_certificate=yes finite_histogram_lengths=16 factorial_checks=127`. The polynomial identity is a finite exact algebraic certificate for the formal generating function for all lengths, while the finite enumeration alone is not an all-length proof. The variance and normal limit use the explicit spectral argument in RESULT.md. Independent audit has not been performed.
