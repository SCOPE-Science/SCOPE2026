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

Binary x-coordinates force extremality of every lifted support. For any representation of the midpoint with a large endpoint S, take S\T nonempty by swapping if needed. Coordinates on S∩T and outside S∪T are fixed. For every missing-side a in S\T, each r-monomial of S containing a is bounded by x_a and has the same mean 1/2, so equality holds almost surely. Including any two such a in one r-set makes all these indicators one Bernoulli variable Z. An (r−1)-subset of S meeting S\T has product Z; adjoining any b in T\S yields a midpoint monomial of mean zero. Therefore x_b vanishes on Z=1 and its mean 1/2 forces x_b=1−Z. The midpoint is supported only on the given endpoints, hence their minimal face is the edge (a relative-interior point of a larger face admits representations using its other vertices). With both endpoints small, setting the sum of monomial coordinates to zero gives a face, projecting to the cube with sum ≤r−1. Its vertices are binary: two fractional coordinates can exchange mass, and a single fractional coordinate can vary unless the integer rank bound is tight, in which case it cannot be fractional. At the midpoint the free-coordinate count is the symmetric-difference size, reduced by exactly one if both endpoints are top-rank. This gives precisely flips and top-rank exchanges. Below top rank there are n flips; at top rank there are r−1 removals and (r−1)(n−r+1) exchanges. Counting flips by direction and lower endpoint gives n times the sum of binomial(n−1,k) for k=0 through r−2, while the exchanges contribute half their incidence count. This verifies the degrees, enumerator, and total edge count. The small simplex graph for r=2 makes the full graph complete; for r≥3 the empty set and a two-set are nonadjacent and have a common large neighbor even at r=n. The inspected finite midpoint-collision script corroborates but cannot replace the all-dimensional argument, since uniqueness among pairs alone does not exclude representations using more vertices.

## originality

PASS

The supported distinction is the full graph of the true complete exact-degree lift for r≥3, in particular the universal high-support vertices and the consequent all-dimensional graph counts. The quadratic complete-graph case and the standard low-face matroid geometry are not awarded originality on their own.

## value

PASS

Adjacency is a natural invariant of the true convex hull for a canonical homogeneous monomial lift, especially because relaxation adjacency can differ. The universal clique and rank-face decomposition together decide every edge, degree and sharp diameter for the entire family, rather than merely improving a numerical bound or reproducing the quadratic case. No claim is made about sparse and mixed-degree lifts, pivots, or facets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
