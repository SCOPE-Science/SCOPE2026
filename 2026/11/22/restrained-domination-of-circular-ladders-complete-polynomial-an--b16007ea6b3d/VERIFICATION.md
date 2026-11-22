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
The supplied `verify_prism_restrained.py` constructs both local-constraint transfer matrices, verifies the symbolic determinant factorizations and the all-order formal expansion used for the minimum counts, tests the direct graph definition against all subsets for three through nine rungs, and checks minimum and high-end coefficients through thirty rungs.

Run with Python 3 and SymPy using `python verify_prism_restrained.py`. Successful replay concludes with `VERIFY_OK`; the symbolic determinant, formal coefficient identities and finite enumerations are all checked during this invocation. The parameter ranges in the program are exhaustive only within their stated finite ranges. Infinite claims are proved by the transfer bijection, formal identities and Perron–Frobenius argument in `RESULT.md`, not by finite extrapolation. Approximate roots are checks, not certificates of uniqueness; primitivity proves uniqueness.

Self-review: passed. Independent audit: not yet performed.
