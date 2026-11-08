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

The universal proof is in `RESULT.md`, particularly the exact positive-semidefinite Schur-complement equivalence, the strict-convexity Hessian inequality, and KKT boundary conditions. Reproduction command: `python3 verify_bipartite_pinning.py` (Python 3 with NumPy and SciPy). The supplied deterministic verifier executes 100 random full-matrix eigenspectrum tests; 100 separate SLSQP optimizations; 1,280 support-order comparisons; 86 high-rate affine checks; 200 two-price branch checks; and 196 exact-rational identities. The printed PASS line contains the category totals. The numerical tests are finite corroboration, not a proof of universal claims. The proof uses classical spectral and convex-optimization facts, and no external independent validation has been performed.
