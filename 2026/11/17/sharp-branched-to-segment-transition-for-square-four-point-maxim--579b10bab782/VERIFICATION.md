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

# Verification and reproducibility

The exact argument uses the standard four-terminal Euclidean Steiner tree structure (including degenerate topologies), symmetry reduction of jointly convex functions, one-variable differentiation, and a strict comparison of the opposite-pair cost. The proof establishes the minimum for every real positive side scale and every nonnegative radius; no symbolic code is needed for that infinite assertion.

Run `python verify.py` with NumPy and SciPy installed. The verifier computes the original two-junction four-disk cost for all three abstract pairings, with unconstrained generic numerical optimization from four starting points, for 36 cases covering three square sizes and twelve radius ratios. It separately verifies the value and first-derivative agreement at the critical radius. Those finite checks are supplementary, sensitive to numerical tolerance, and do not independently certify the analytic theorem.

The closest identified literature studies general four-point Steiner trees, inverse maximal-distance-minimizer realizability, or general existence; historical priority of the all-radius square-corner calculation remains provisional. No expert or independent audit is represented.
