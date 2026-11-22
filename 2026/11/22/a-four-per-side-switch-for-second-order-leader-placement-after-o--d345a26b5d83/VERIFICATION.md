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

## Reproduction

Run `python verify.py` using Python 3 with SymPy and NumPy installed. The checker reconstructs all five class costs from the grounded inverse and rank-one deletion formula, checks them against displayed rational expressions, verifies strictly positive integer-coefficient polynomial expansions, and exhaustively checks all two-leader pairs via direct diagonalization for every integer graph size from 3 through 14.

Recorded outcome: 1,947 passed checks. The exact symbolic identities and sign arguments establish the all-integer theorem; the 3-through-14 sweep independently checks formulas but cannot prove the infinite claim.

## Scope and limits

The system is the unit-weight one-link-defective balanced complete bipartite graph, exactly two perfectly pinned leaders, and the second-order stochastic response with matched Laplacian position and velocity feedback. The covariance interpretation is verified by a two-dimensional modal Lyapunov equation. No external audit or independent mathematical validation has been performed.
