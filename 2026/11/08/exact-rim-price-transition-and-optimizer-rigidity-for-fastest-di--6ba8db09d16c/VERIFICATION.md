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

# Verification and limits

The universal statement is established in `RESULT.md` by explicit Rayleigh quotients, one-dimensional optimization of their affine envelope, and equality-case Fourier eigenvector rigidity. Its derivation does not depend on a numeric exhaustive search.

Run `python3 verify.py` from the same directory. The checker uses only the Python standard library and contains a Jacobi symmetric-matrix eigensolver, analytic optimum formulas, seeded heterogeneous feasible budgets, all critical-interval samples, and first-Fourier forcing checks. Replayed output: `VERIFY_OK 1279`.

For audit of normalization, a uniform wheel with per-spoke rate \(a\) and per-rim rate \(b\) has nonzero eigenvalues \((m+1)a\) and \(a+4b\sin^2(\pi k/m)\), where \(1\le k\le m-1\). The price of one spoke is one and the price of one rim edge is \(c\). The optimizer has positive spoke conductance at every permitted price, including the boundary of the support transition. Discarded rim conductances are permitted zero values, not a disconnected graph.

Numeric checks cover only finite sizes and price samples; rounding tolerances are used for trigonometric and eigenvalue computations. The originality assessment is bounded by cited inspected sources. An independent mathematical audit has not been performed.
