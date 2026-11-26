---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The squared two-step map for pair (i,j) is (a_i^T a_j)^2 P_i because the complementary projections are rank one in the plane. Pay at least q_i per conditional successor (q_0=u, q_±=q=min(u,(2u−1)^2)); taking the two coordinate diagonals gives a lower bound max{q(1−u)(1−t), u t+qu(1−t)}, t=Pr(I=0), for every joint law. Balanced leaves and minimizing successors attain it. For u<1/2 the unique crossing gives the stated t and an isotropic optimal matrix; imbalance already raises the maximum eigenvalue of the cheaper matrix, while at balance any nonzero positive-semidefinite excess strictly increases it. For u>1/2 the vertical quadratic form forces t=0 and minimum successors, and any nonzero off-diagonal entry makes the optimum impossible. At u=1/2 the only zero-overlap pairs are the two opposite-leaf pairs, with arbitrary mixture. The identity (2u−1)^2−u=(4u−1)(u−1) gives the tie at 1/4. The exact benchmarks 3/80 vs 1/16 and 3/16 vs 11/18 follow from the same matrix. An independent diagonal density-matrix dual attains the bound: for u<1/2 its first diagonal is u(1−q)/(u+q(1−2u)), otherwise use the vertical unit projector. That dual and all nine supported/forbidden pair costs were checked at 102 exact rational parameters in /workspace/branches/independent_replay.py (kaczmarz); the grid is corroboration only.

## originality

PASS

The supported result is the exact unrestricted joint-law optimum and all equality cases for this symmetric three-row family. The matched variants change horizon, coupling/marginal constraints, relaxations, or the optimized selection rule. No covering statement was found in the actual material inspected; access gaps limit historical priority, not the mathematical decision.

## value

PASS

A complete shortest-horizon benchmark on a natural symmetric overdetermined geometry separates local successor preference from global balancing of error directions. The exact 3/8 example shows that deliberately including a less favorable pair can improve minimax retention over every deterministic schedule. The two distinct changes in support and the classification of all ties make the result useful for comparisons with independent and coupled designs, without an extrapolation to runtime or long-run rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
