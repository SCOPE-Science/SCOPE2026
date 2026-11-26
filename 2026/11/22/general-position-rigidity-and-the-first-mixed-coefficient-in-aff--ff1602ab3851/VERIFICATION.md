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

In a connected bipartite graph an edge's endpoints have distances from a third vertex differing by exactly one, so a general-position set of size at least three is independent. In an independent selection here distinct points are distance two, selected point-line pairs distance three, and selected line-line pairs distance two if intersecting and four if parallel. The only possible additive equality is 4=2+2 for parallel end lines; a selected point cannot be distance two from them, while a selected line is distance two from both precisely if it is a common transversal. This proves the selected-line dichotomy. For b≥1 parallel lines the total mixed size is at most q²−b(q−1); with b different directions the union has size ≥bq−binom(b,2). For q≥4 the penalty b(q−1)−binom(b,2), concave on [2,q+1], exceeds q−1 at both endpoints, so only b=1 can attain q²−q+1. For q=3 the only possible extra equality is b=4 with distinct pairwise intersections. Adding the line at infinity would give five projective lines with no triple concurrency. Such a family covers 10 of the 13 points; on every family line each point is already a pairwise intersection. A pencil based at an uncovered point would therefore pair off the five lines, impossible. Thus maximizers are one line with all its off-line points, with q(q+1) choices. The all-line bound q+1 is smaller than q²−q+1 for q≥3, and every point subset is general position; this gives the unique full-point maximum and both coefficient formulas. At q=2, b≤2 gives mixed size at most three. Among eight different-direction triples, four are concurrent (one per point) and the remaining four cover three points each, giving four mixed maxima plus the pure point maximum. Exact independent metric enumeration returned (overall size, overall count, mixed size, mixed count)=(4,5,4,4) at q=2 and (9,1,7,12) at q=3, with coefficient 48 at degree seven for q=3.

## originality

PASS

The general distance-partition criterion already covers the structural test by direct specialization, and the earlier once-subdivided complete-graph record explicitly covers the order-two maximum and polynomial. The distinct contribution is the affine-plane extremal argument and exact first mixed coefficient for arbitrary finite affine planes of order q≥3, not a new general-position criterion or the q=2 data.

## value

PASS

The point–line incidence graph is canonical for any finite affine plane, and the first degree admitting mixed selections measures a natural gap below the rigid maximum. The extremal classification identifies all configurations that close that gap, yielding the exact first mixed coefficient uniformly without field-coordinate assumptions. This is more than a computation at the already covered order-two graph or an application of the generic structural test alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
