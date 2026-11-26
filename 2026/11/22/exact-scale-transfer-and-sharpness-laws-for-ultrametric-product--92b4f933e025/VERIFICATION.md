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

For nonempty finite ultrametrics, distance at most r is an equivalence relation and its classes are exactly the closed r-balls. Since the product metric dominates each coordinate, no centered product ball meets another class rectangle; covering optima add. In an ultrametric class, every center has eccentricity equal to its diameter by applying the strong triangle inequality to a diametral pair. The farthest coordinates in a rectangle can be chosen independently, so the rectangle takes exactly one ball iff the sum of the two diameter powers is at most r^p. The maximum over rectangles uses the maximum class diameter in each factor, giving both directions and strictness otherwise. With equilateral X-class of size m and interpoint distance a, a center covers its own row and only radius-t portions of other rows, t=(r^p-a^p)^(1/p). One center per row or a radius-t cover projected from one row gives both upper bounds. Any cover using fewer than m centers leaves an uncentered row, and covering that row forces the projections of all centers to cover the Y-class at radius t. This proves the exact minimum on each rectangle. Singletons use a=0 and cost one with t=r; a=r gives t=0 and distinct Y-points are singleton t-classes. The equilateral extremal family and two-scale example give min(m,n) and 5 respectively. The normalized diameter-power condition is monotone in p but need not hold at any finite p when one normalized diameter is 1 and the other positive; the maximum metric separately always multiplies. The proof handles every finite real p>=1, not just the integer powers in the inspected frozen checker, which was not executed.

## originality

PASS

The strongest retrieved coverage concerns the maximum product, different general sum-metric hypotheses, or simpler domination instances. None supplies the finite-p closed-ball diameter threshold and equilateral-to-hierarchical scale transfer. This is a bounded comparison of actual statements, not a global priority certification.

## value

PASS

The diameter law completely answers when a natural product-cover lower bound is an equality, including arbitrarily large excess in sharp examples. The scale-transfer law reduces a potentially large product covering problem to single-hierarchy counts at explicitly shifted radii, with no equilateral restriction on the second hierarchy. It is a useful exact reduction beyond the maximum-product or rook-graph cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
