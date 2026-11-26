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

Corollary 1 of Joós–Lángi gives the Steiner-normalized parallelotope sum. For each tree component on r vertices, deleting any row of its incidence matrix has determinant ±1 by recursively eliminating a leaf, so Cauchy–Binet gives Gram determinant r; disjoint components factor. The only dependent four-edge sets are squares. For three edges, the connected count is s+m(d−1)^2, and the wedge-plus-edge count is w(m−3d+2). With four edges, stars and brooms embed without vertex repetitions by triangle-freeness; the repeated-vertex length-four nonbacktracking walks are exactly four per square up to reversal, giving E_0−4q_4. Deleting a three-edge tree's four vertices leaves m−4d+3 edges plus one if the tree is a path closing a square, giving D_0+4q_4. Counting wedges avoiding the three vertices of a fixed wedge uses adjacent-pair overlap 2(d−1), endpoint overlap c_ab, and triple overlap 1; the sum of c_ab−1 is 4q_4, giving C_0+2q_4. The outside degrees after removing the wedge are d−r_x; the sums of r_x and binom(r_x,2) are 3d−4 and c_ab−1, so the wedge with two disjoint edges contributes B_0−4q_4. Subtract the five types and the dependent sets from all quadruples to get the remaining count A_0+q_4. The weighted coefficient is −α, strictly negative by the displayed rational square-root bounds. An independent exact Gram-determinant tally verified the same V1–V3 and the difference −7α between the two cubic circulants, whose square counts are independently 7 and 0.

## originality

PASS

The general determinant sum is prior. In the inspected records and literature, neither it nor the known other zonotope statistics supply the five-type count as an affine function of the number of squares, or this explicit nonzero V4 coefficient. The supported distinct content is the specialized exact census and the consequent first geometric distinction at fixed n,d within the specified class.

## value

PASS

Canonical graphical zonotopes and the fourth Steiner intrinsic volume are both standard objects. It is meaningful to identify which combinatorial information first becomes distinguishable at fixed n,d: V1–V3 conceal square counts whereas V4 detects them with exact sign and scale. The two cubic 14-vertex graphs show the distinction genuinely occurs without changing degree, order, or triangle count. An explicit invariant is useful both to compute the geometric quantity without enumerating edge sets and to read a graph statistic from the geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
