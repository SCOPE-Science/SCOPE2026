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
# Verification

From this directory, run `python verify.py` using Python 3 with NumPy and SymPy installed. The checker forms the three unit rows at six correlations, computes the exact expected one-step matrix and the full nine-by-nine Kronecker superoperator for 8,466 numerical inequalities over probability grids, checks the two analytic optima, and verifies rational examples and the symbolic maximum. Its actual output on the packaged version is:

`PASS: 8466 spectral inequalities checked; exact rational examples and maximum checked`

The infinite parameter and iteration quantifiers are supported by the hand proof in `RESULT.md`: exact two-by-two eigenvalue identities, invariant-block decomposition of symmetric covariance matrices, positive leading-eigenmatrix trace, two strictly opposing affine-envelope minimizations, and a one-variable sharp loss maximum. The tests do not prove global uniqueness; the analytic equalities and strictness do. No external data, other records or network access are needed to reproduce the computations. This is not independent mathematical validation.
