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

# Reproducibility and limits

The theorem's direct formulas and infinite-dimensional arguments are in `RESULT.md`, sections Finding and Proof. The weight-ratio product argument establishes positive power-law coefficient convergence. The negative and positive spectral subspace constructions rely respectively on normalized-coordinate off-diagonal decay of order \(O(j^{-1/2})\) and finite-difference off-diagonal decay of order \(O(j^{-3/2})\).

Run the included standalone `checker.py` with Python 3 and the `mpmath` package using:

```bash
python checker.py
```

Observed outcome: `PASS 182 finite/high-precision diagnostics; infinite conclusion established in RESULT.md proof`. The 182 checks include rational arithmetic verification of the finite-difference quadratic identity; direct Hurwitz-zeta evaluation of the infinite matrix elements for polynomial rows; tests of leading coefficients at large indices; and strict diagonal dominance of four-by-four normalized positive and negative quadratic-form matrices.

These computations inspect finitely many parameters and indices, so they do **not** by themselves certify infinitely many eigenvalues. That conclusion uses the quantifier \(\forall m\in\mathbb N\) in the two inductive subsequence arguments in `RESULT.md`. Neither the full list of eigenvalues nor a sharp asymptotic eigenvalue law is computed. Self-review was performed; independent mathematical validation was not performed.
