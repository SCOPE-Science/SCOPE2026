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

# Verification details

The proof is algebraic for every integer \(d\ge3\). In `RESULT.md`, the global Dirichlet energy is normalized by \(2d\) times the global scalar energy. Gaussian absolute moments independently determine the regional second- and fourth-order tensors. The resulting operator is reduced using the three invariant sectors of the complete-graph unsigned incidence representation. The strict ordering is established by explicit characteristic-polynomial sign identities, not inferred from finite numerical computations.

Run `python verify_orthant_gradient.py` with NumPy: the checker rebuilds full normalized Gram matrices from independently enumerated fourth moments, compares complete eigenvalue multisets for \(3\le d\le10\), verifies strict ordering and trace, and compares large-dimension condition-number ratios. Verified output: `ORTHANT_GRADIENT_SPECTRUM_CHECKS_PASS 243`.

Run `python verify_factors.py` with SymPy: this checks both ordering factorizations, the middle-sector difference, and the determinant-based asymptotic identities. Verified output: `ORTHANT_GRADIENT_SYMBOLIC_IDENTITIES_PASS 6`.

The scripts do not establish publication priority and their finite tests do not replace the analytic all-dimensional argument. The claimed limit concerns the ratio of **concentration eigenvalues**; the singular-value condition number of the gradient restriction map is its square root. Independent mathematical audit has not been performed.
