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
# Reproducibility checks

Execute `python rook_rank_checker.py` with Python 3. The checker uses exact rational arithmetic and directly enumerates every signed rook placement for 72 coefficient/rank test cases with ambient dimensions two through four. It compares those direct second/fourth moments with the independently derived occupancy formula.

It also checks exact sharp witnesses for all pairs of dimensions two through twenty-six; verifies both nonnegative lower-deficit decompositions in 2,380 rational coefficient cases; and tests positive, nonuniform additive equality matrices at several critical ranks. All these checks completed successfully in the present package assessment. They are finite consistency checks; the analytic proof, not test coverage, establishes arbitrary dimension and rank, complete equality cases, and Euclidean optimality.

Recompute the two-cell probability by counting matchings containing a prescribed disjoint pair: it is \(k(k-1)/[n^2(n-1)^2]\). Conditional sign integration then yields the moment formula. To reproduce the exact lower identities, form normalized squared coefficient masses, marginal row/column sums, and the interaction residual in the supplied result. The lower identity above the threshold is convex interpolation between the critical additive identity and the variance decomposition for a uniform full permutation.

The analysis does not provide independent certification, exhaustive source coverage, nor any theorem about other moment exponents.
