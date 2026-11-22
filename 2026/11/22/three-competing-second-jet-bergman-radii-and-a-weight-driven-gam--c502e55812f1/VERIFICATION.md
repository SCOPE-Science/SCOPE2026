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

# Reproducible diagnostics
Run `python3 checker.py` from the directory holding this package. It uses only the Python standard library and prints a `PASS` line after 98 exact-rational diagnostic assertions.

The checks consist of: 44 polynomial factorization identities at multiple positive kernel exponents and monomial degrees, 45 independent direct three-jet Gram inversions at rational points, and nine rational Laguerre root/height interval inequalities at exponent \(\beta=2\).

For the last group, the Laguerre cubic after multiplying by a nonzero scalar is \(24-36t+12t^2-t^3\). Each of its three positive zeros is isolated in a rational interval, and exact fractional Taylor bounds on \(e^{-t}\) prove disjoint upper and lower ranges for the Gamma capture heights. The finite checker does not replace the analytic Jacobi interlacing, the all-degree derivative identity, the large-degree limit, or the large-weight Hermite argument in RESULT.md. No independent audit has been performed.
