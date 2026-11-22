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

# Verification scope

Run `python verify.py` from the extracted directory with SymPy and mpmath installed. The script checks critical derivatives exactly for four integer exponents, eight independent high-precision width instances (including noninteger exponents), the rational quadratic three-root census, branch alternation and selected high-exponent roots and multipliers. The observed execution output was:

`PASS: exact cusp derivatives, 8 high-precision cusp-width checks, rational triple-cycle census, affine contraction and large-exponent branch checks`

The finite checker is supporting reproducibility, not an infinite or all-parameter certificate. The proof in RESULT.md supplies the analytic quantifiers: every real exponent d>1 for the sharp cusp/fold criterion and all sufficiently large d for every *fixed* strict-alternation parameter triple. Complete priority and independent audit are not certified.
