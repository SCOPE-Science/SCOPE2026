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

# Verification of the mathematical claim

The proof is self-contained modulo the classical Lyapunov convexity theorem and the standard finite-rank nuclear trace identity on \(\ell_1\). The nonatomic vector-measure splitting is used **only** to choose \(h\) with \(|h|=f_D\) and \(Th=0\), and the atomic trace bound is used **only** after compressing to the atomic band. No finite-dimensional test is promoted to an infinite-dimensional proof.

`CHECK.py` is an optional exact-rational diagnostic of positive rank-restricted finite matrices with column \(\ell_1\)-norm at most one. It checks both the tail lower bound and its attainment by coordinate projections, reporting `RANK_MODULUS_ATOMIC_EXACT_CHECK_OK 3200` upon success.

Unproved limits: no analogous formula is asserted for signed inputs, nonpositive or noncontractive approximants, or alternative operator topologies. Full-text comparison against the later version of the motivating paper was not possible; its known qualitative characterization is expressly excluded from novelty.
