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

The proof is analytic and establishes the rank, eigenvalues, strict inequality, and both asymptotic limits for all real \(0<a<b\) and \(L>0\). Numerical checks are supplementary, not certification of infinite-dimensional statements.

Execute `python verify.py` using Python 3 and the `mpmath` package. The optional finite-matrix comparison additionally requires `numpy`. The tested script completed 63 analytic-identity, numerical-quadrature, exact-moment, and matrix-spectrum checks without failure. The script tests the full-line subtraction identity by direct piecewise quadrature, reflection-split Gram determinants, short/long length asymptotic behavior, and four-nonzero-singular-value finite-rank structure. It does not establish historical priority or replace peer review.
