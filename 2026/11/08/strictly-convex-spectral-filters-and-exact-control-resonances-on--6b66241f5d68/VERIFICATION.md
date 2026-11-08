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

The mathematical argument is in `RESULT.md`. The spectral decomposition is exact for every integer bipartition size at least two. The PBH test reduces the input-budget classification to support of eigenvectors on one or two omitted coordinates. Strict convexity excludes a three-level collision, and exact cubic monotonicity proves both RK4 resonances. The latter are algebraic irrational times, not approximated exact roots.

The companion `verify.py` is standalone Python standard-library code; run `python3 verify.py`. In the reviewed replay it returned `OK rational_matrix_checks 100 exact_coordinate_rank_checks 1884 two_missing_coordinate_tests 1584 positive_RK2_resonance 5/9 isolated_RK4_roots 2`. The checker uses `fractions.Fraction` for the transition matrices and Kalman rank computations on all complete bipartite graphs with both parts of sizes 2, 3 or 4, several rational positive timesteps, every pair of missing coordinates and representative single missing coordinates. It includes the exact rational RK2 collision times, the zero-time rank check, and exact rational bracketing of the two fourth-order cubics. The matrix experiments alone cannot prove the theorem for arbitrary sizes or irrational resonance steps; these cases are covered by the symbolic proof.

The claim concerns the directly actuated discrete matrix pair, not a physical hold/Runge–Kutta forcing discretization. No independent audit was performed.
