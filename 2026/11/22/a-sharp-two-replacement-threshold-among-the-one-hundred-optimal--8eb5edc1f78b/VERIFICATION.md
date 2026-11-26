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

If a dominating five-set selected l left and 5−l right vertices, the two shores would require l+3(5−l)≥10 and 5−l+3l≥10, forcing l≤2 and l≥3, respectively. Smaller dominating sets extend to size five, so none exist. I used an independent integer census, representing both shores by two-subsets after complementing each right label. Adjacency is disjointness across shores, and distinct vertices on the same shore are at distance two exactly when their labels intersect. The script finds a vertex isomorphism to GP(10,3) by a ten-cycle with distinct outside neighbors having the specified offset-three inner edges. It confirms 130 dominating six-sets, 100 semitotal with 3+3 vertices, all 4,950 pair comparisons (0 at distance one and 570 at distance two), and eccentricity four from all 100 states. It explicitly verifies the stated representatives and links each symmetry orbit to its induced-edge count, degree and shell vector, a crosswalk not explicitly asserted in the supplied code. For fullness of the symmetry group, a shore-preserving automorphism induces one of the line graph of K₅ on the left shore's distance-two graph; its only size-four cliques are the five stars. The stars determine the left labels, and each right vertex has a distinct left neighborhood. Thus the restriction is exactly S₅; the shore swap in the complemented model doubles it and commutes with S₅.

## originality

PASS

The supported distinct content is the exact optimum census, orbit structure and metric of its optimum-only exchange graph. The graph model, symmetry, terminology and size lower bound are established background. The strongest inspected comparisons share either the graph or the optimization predicate, but do not establish the census and exchange theorem together or via a direct specialization.

## value

PASS

The Desargues graph is a standard symmetric cubic test graph, and minimum semitotal configurations are natural constrained placements. All 100 optima being frozen at one move but jointly connected at two is a sharp, nontrivial objective-specific benchmark, not merely rerunning a known number. The orbit-resolved shells characterize how different starting types access the rest of the solution space and can test exact graph reconfiguration methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
