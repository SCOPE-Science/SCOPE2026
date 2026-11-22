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

# Reproducible verification

The source `pentagon_interval.py` has no nonstandard dependencies. Running `python pentagon_interval.py` constructs all monomial moments to total degree 24, evaluates 28 Taylor-jet components, computes all ten six-coordinate Hessians, and performs rigorous \(LDL^{\mathsf T}\) interval eliminations with \(10^{40}\) integer scale. It terminates successfully only if every interval denominator excludes zero, every one of the 60 pivots is strictly positive, and all ten *minimum* pivot lower endpoints exceed \(1/5\); see `certificate_results.txt`.

The exact-integer \(\sqrt5\) bracket is obtained using `math.isqrt(5 * 10**80)` and its successor. All other rational coefficients and outward rounding are based on integer operations. The check prints small first-derivative residual enclosures, while exact gradient vanishing is supplied analytically by symmetry and scaling. The coefficient formula, Hessian identity, and chart argument are set out in `RESULT.md`.

Run `python pentagon_quadrature.py` with NumPy for independent Gauss–Legendre double-integration of the unnormalized energy at the regular pentagon. Its output is in `independent_quadrature_results.txt`; it is an independent numerical consistency check of endpoint powers only, not an infinite-proof substitute.

This is a self-review and reproducible finite exact-arithmetic certificate. No independent mathematical audit has occurred. Historical priority, all-exponent claims, and global optimality are not certified.
