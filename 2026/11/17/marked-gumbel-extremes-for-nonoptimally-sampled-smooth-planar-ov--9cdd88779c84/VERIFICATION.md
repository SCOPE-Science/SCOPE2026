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

The analytic derivation is in `RESULT.md`. The source `check_nonoptimal_hausdorff.py` runs directly in the extracted artifact directory using Python 3 and NumPy. Its reproducible checks include exact \(H_n=1-\cos(g/2)\) on the unit circle, independent quadrature of the nonuniform Laplace tail integral, and fixed-seed sampling at \(n=12000\). A successful run prints `NONOPTIMAL_INSCRIBED_GUMBEL_CHECKS_OK`; this was observed in the saved source run.

Finite-sample simulations converge slowly because the Laplace prefactor has \(O(1/\log n)\) corrections. The tests are diagnostics, not a certificate of an infinite marked Poisson limit. The mathematical proof uses uniform cap geometry, exact normalized exponential spacings, coupling to deterministic quantile grids, independent rare-event convergence, and Laplace method at the isolated nondegenerate minima. The scalar positive-density spacing distribution is previously established and is not asserted novel.

No independent mathematical audit has been performed.
