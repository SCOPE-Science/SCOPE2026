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

## Actual verification

The proof uses the exact monotone angular-ratio inversion, direct Jacobian expansion, the independently published scalar cross-ratio density, and Scheffé's lemma. Executing `python verify.py` checks the scalar density by quadrature; independently tests the exact inverse Jacobian at three shrinking thresholds; draws 2,000,000 seeded Dirichlet spacing samples; compares the event frequencies at three thresholds with the integrated scalar law; and reports the finite-threshold conditional means of the three marks. A successful run terminates with `MARKED_IDEAL_QUADRILATERAL_CHECKS_OK`.

Finite Monte Carlo and quadrature are corroboration, not an infinite-precision or infinite-limit certificate. The mathematical limit requires the analytical proof. No independent audit has been performed; historical priority is provisional.
