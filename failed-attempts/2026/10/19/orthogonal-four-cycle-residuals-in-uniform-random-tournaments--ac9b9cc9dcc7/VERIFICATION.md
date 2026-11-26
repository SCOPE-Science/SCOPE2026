---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For each of the three unoriented Hamilton cycles per four-set, summing the two directed indicator products gives (1+sum of the six sign pairs+the full product)/8. A given wedge belongs to exactly one cycle on the four-set; a given pair of opposite edges appears in two cycles with opposite relative signs. Thus wedge quadratics contribute half the centered local cyclic-triangle count, and the degree-four sum is exactly the displayed residual after summation over four-sets. Two distinct such products have different edge supports, so under independent fair signs the residual is orthogonal to all shorter Walsh products and has variance 3 binom(n,4)/64. Distinct triangle indicators have disjoint edge supports or share only one edge; in the latter case their conditional means given that sign are both 1/4 and their remaining edges are independent. The variance of T_n is 3 binom(n,3)/16. Projecting gives exactly the displayed affine predictor because it has degree ≤2; expanding its variance and covariance yields the finite formulas, correlation, and residual fraction. This proof includes n=4 and makes no claim of conditional expectation given T_n.

## originality

FAIL

The distinct Resultary theorem 3b4b1b16fef5 has exactly the same local and global residual, moments, variance, affine predictor and correlation. Its local degeneracy and four-vertex table also mechanically imply the apparent Walsh refinement: the known cycle indicators have sign-degree at most four, their sum and the triangle count are invariant under full edge reversal, and the indexed conditional degeneracy eliminates all constant and wedge coefficients. A disjoint-edge quadratic coefficient vanishes by swapping the endpoints of one edge. A degree-four support on K4 is a cycle or a triangle with a pendant edge. Swapping the two triangle vertices away from the pendant attachment preserves that support and changes its sign, killing the second type. Vertex relabeling fixes a common coefficient in cyclic sign convention for the three surviving cycle products. In the transitive orientation 1→2→3→4 with all edges forward the three cyclic products are −1,+1,+1, and the indexed table gives the local residual 1/8; hence the common cyclic coefficient is 1/8. The full projection, support count and signs therefore require no independent assumption or additional invariant beyond the indexed result and elementary sign symmetries. This is statement coverage, not an attribution or priority decision.

## value

PASS

The exact representation identifies the low-degree fluctuations of four-cycles and the size and structure of the remainder, giving a meaningful distinction between affine forecasting and orthogonality to the whole low-degree space. The formulas give exact finite error, rather than just observing large correlation. This values the mathematical content, not a claim of a new contribution over the indexed result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
