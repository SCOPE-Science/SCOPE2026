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

The package includes `check.py`, executable with Python 3 and SymPy. It symbolically checks the four-dimensional transfer matrix, invariant and normalized density, its characteristic polynomial, three- and four-lag covariance identities, full-mode cancellation via characteristic roots, the exact Green–Kubo rational expression, the strictly negative derivative factorization, positive-coefficient polynomial expansions, and the limiting variance \(1/12\).

These algebraic checks are reproducible from the files embedded alongside this document; no external dataset or experiment is needed. The manuscript separately proves why the finite-dimensional computation applies to all integer parameters and all nonnegative time lags. Verification does not establish publication priority or supply an independent mathematical audit.
