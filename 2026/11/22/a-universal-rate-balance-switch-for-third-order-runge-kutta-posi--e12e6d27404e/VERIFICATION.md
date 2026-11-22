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

# Reproducibility and mathematical verification

The endpoint matrix and boundary mechanisms are proved in `RESULT.md`. Execute `python verify.py` with Python 3 and SymPy; the complete captured output is `verify_output.txt`. The script derives the matrix entries by symbolic polynomial expansion, reduces and verifies the analytic cutoff identities, tests all displayed example matrices, and checks 7,623 rational matrix entries over six leaf counts and seven rational rate pairs with three positive rational step sizes. The exact analytic argument, rather than numerical tests, establishes all-dimensional nonreentry and unique rate-balance switch.

The first public motivating source is the February 16, 2021 arXiv v1 of Blanes–Iserles–Macnamara (arXiv:2102.08242). Source-comparison limitations are recorded in `REVIEW.md` and `AUDIT.json`. The mathematical proof has not been independently audited or externally certified.
