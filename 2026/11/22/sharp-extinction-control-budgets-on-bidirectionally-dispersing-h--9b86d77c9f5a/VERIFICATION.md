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

# Verification and proved limits

The theorem is proved analytically in `RESULT.md`. The Perron-eigenvector identity, edgewise AM–GM equality constraints and cycle consistency establish the sharp lower bound and unique feasible equality case; a positive left Perron vector and nonlinear quadratic crowding establish extinction even at exactly zero linear growth. The two-patch boundary branch follows a one-variable strictly convex minimization; the cycle contrast uses Jensen's inequality. No finite check establishes the general claims by itself.

To replay the additional exact-arithmetic tests, run `python check.py` in the extracted artifact directory. It uses Python's standard-library `fractions.Fraction` and checks 400 seeded random directed-tree configurations, 35 two-node configurations, one explicit three-node certificate and the biased triangle example. The analytic proof covers arbitrary positive rates and every finite connected bidirectional graph under the stated restrictions; the exact construction is fully evaluated for trees when the feasibility threshold holds, for all two-node rates, and for homogeneous-rate biased triangles. General non-balanced cyclic-network optimal budgets are not classified.

No independent scientific audit or independent validation has been performed. Priority beyond the inspected original and related matrix-control literature has not been established exhaustively.
