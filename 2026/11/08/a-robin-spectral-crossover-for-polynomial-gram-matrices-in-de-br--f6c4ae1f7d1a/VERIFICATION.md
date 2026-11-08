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

# Reproducibility and verification

Run `python CHECK.py` after installing the single listed dependency in `requirements.txt`. The finite checker was executed and passed 405 assertions, comparing Gram entries with the original coefficient-sum norm, bidiagonal factorization, determinants, numerical eigenvalues and limiting ratios. Finite matrices do not establish any uniform or infinite-dimensional limit: the analytical proof in `RESULT.md` provides the argument for those statements.

The normalized parameters are \(q=(1-\sqrt{1-c^2})/(1+\sqrt{1-c^2})\), the matrix size is \(n+1\), the finite crossover scale is \(n(1-q)\), and the continuum kernel has Dirichlet data at zero and Robin data at one. No independent audit has been performed.
