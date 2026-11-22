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

The argument is self-contained: it factors the finite Walsh compression, computes its inverse-square Jacobi operator, proves a strict spectral-edge inequality, and derives the principal eigenvector boundary phases and uniform asymptotic expansion. These are analytical steps, not finite extrapolation.

Run `python3 checks/check.py` with Python, SymPy and SciPy to reproduce supplementary algebraic tests and Jacobi eigenvalue comparisons. The checker verifies the inverse identity, the Jacobi square and determinant recursion for every integer \(2\le N\le12\); the positive comparison-vector identity for those indices; and numerical sharp-norm/shifted-gap agreement at nine indices through \(N=1000\). It does not prove uniqueness or novelty, and numerical tests do not constitute a proof for every integer.

The leading constant in the quadratic limit is \(\sqrt2\pi^2(1+1/\sqrt2)^3\). The error statement is \(O(N^{-4})\) in the shifted denominator \(N+5+3\sqrt2\). Other dyadic truncation patterns and arbitrary Walsh maximal operators are not analyzed. No independent mathematical audit has been performed.
