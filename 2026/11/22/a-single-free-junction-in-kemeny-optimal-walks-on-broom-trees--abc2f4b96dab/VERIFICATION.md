---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

N times the zero-target Kemeny sum is the Kirchhoff index by the Laplacian pseudoinverse identity; each tree edge contributes its cut-pair count times its reciprocal weight. Positivity of cut counts makes the objective strictly convex, and the equal-leaf candidate and its multipliers can be lifted to every individually adjustable leaf edge. Let L=2h or 2h+1 as appropriate. The recorded sum polynomials give E/O<h/(h−1) for even L and E/O<(h+1)/h for odd L. These bounds are at most m²(m+L)/(L(m+1)): the latter increases with m and the comparisons at m=2 reduce to h²≥4 in the even case and 2h²+3h−3≥0 in the odd case. Thus the first junction is strictly slack, including L=3 and L=4. For the remaining KKT signs, c_j is a product of two positive linear factors and has strictly decreasing consecutive ratios c_{j+1}/c_j. For an interior odd junction, S_O(k)/S_E(k) is a strict upper prefix average of the decreasing ratios c_{2i+1}/c_{2i} (append zero at the end for even L), so it exceeds O/E. For an interior even junction, S_O(k−1)/S_E(k) is the lower prefix average of increasing ratios c_{2i−1}/c_{2i}, with the first numerator replaced by zero because O excludes c_1. It is strictly below O/E: there is a later ratio or, for the last even junction when L is odd, the unpaired positive final odd term. These prove strict positivity of the displayed interior multipliers without numerical sampling. Full sums give zero at the endpoint, and root stationarity holds since c_1/x²=c_0/a². KKT proves the optimum; strict convexity gives uniqueness; the two square-root allocations give the stated minimum. The terminal path vertex is also a leaf and has positive holding. The fixed-L limit follows from c_1∼Lm, c_0∼m, and positive slopes of E and O.

## originality

PASS

The supported contribution is the exact all-size optimizer and active capacities for the unequal-arm broom. The optimized reversible-chain framework and the tree resistance reduction are not the contribution. Distinct catalogue entries with substantially similar formulas do not cover the unequal-arm broom; their shared index date does not indicate order or priority.

## value

PASS

A natural one-branch departure from a path yields a sharp, size-uniform capacity pattern: root and subsequent interior path budgets are tight, but the first interior budget must be left partly unused. Exact optimizers on all brooms, and the contrasting first-edge versus tail scales, are useful benchmarks for kemeny-minimization methods and do not follow from a preference to saturate every local capacity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
