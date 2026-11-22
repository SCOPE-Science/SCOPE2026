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

# Reproduction and limits

Run `python check.py` with SymPy, NumPy and SciPy installed. The script symbolically derives the exact mixed density and validates the four margins, then computes numerical diagnostics for the scalar threshold and envelope at selected angles. It does not certify a global numerical minimum, and the finite angle grid is not an infinite verification. The mathematical proof relies on the fixed-argument AM-GM extremizer, both attainable derivative signs, the exact infimum condition, the sine sign boundary and explicit large-angle comparison bounds. The proof covers every positive real angle and all real dependence parameters, only at exponent one.

The approximate transition in the text is derived numerically using the scalar minimization, not claimed as an independently validated interval. The explicit minimum formula is the exact threshold. Statistical estimation and general shape exponents are outside scope.
