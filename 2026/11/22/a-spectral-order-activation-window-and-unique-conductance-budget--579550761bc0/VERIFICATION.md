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

# Reproducible numerical and exact checks

Run `python3 verify.py` using the Python standard library. For the packaged executable code, the reproduced run produced `VERIFY_OK 2239`.

The checker constructs the full weighted combinatorial Laplacian, independently diagonalizes it by a Jacobi procedure, compares the eigenvalues with the claimed block spectrum, checks rational inverse identities by exact Gaussian elimination, verifies the price constraint, objective values and support boundary for multiple finite sizes and parameter choices, and compares the analytic optimum with many nonsymmetric feasible conductance assignments. It also checks the five-vertex activation exponent and the large-spectral-order asymptotic. The checker has no dependencies on unstored files.

**Scope limitation:** Finite computations cannot prove an infinite-size theorem or global optimality against every feasible assignment. Those statements depend on strict matrix spectral-trace convexity, the group-action uniqueness reduction, the explicit scalar objective derivative and the monotone-derivative proof of exactly one spending peak in `RESULT.md`. An independent audit has not yet been performed.
