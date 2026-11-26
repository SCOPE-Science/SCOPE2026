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

Reconstructed the theorem for the specified unweighted GP(8,3). Distance signatures separate all vertices exactly when the indicated subset is resolving; enumeration of sizes 0 through 4 proves minimality and completeness. A legal move is uniquely specified by the removed and inserted vertices of two distinct sets differing in one element, with the extra adjacency predicate for a slide. Exhaustive unweighted shortest-path searches and comparison of the two distance matrices therefore exhaust all 51,040 unordered pairs. A fresh independent program reproduced zero smaller sets, 320 bases, the full degree, eccentricity, distance and penalty distributions, both connected graphs, the two radii and diameters, and the distances (2,10) for the stated witness. It enumerated 96 automorphisms, with orbit sizes 24,24,32,48,96,96. Preservation of adjacency and nonadjacency is a sound pruning condition on partial injections and characterizes automorphisms on completed bijections. The recorded GP and LCF checks corroborate but do not substitute for the fresh run.

## originality

PASS

The pass is for the complete ordinary metric-basis motion and orbit classification, not for the notion of reconfiguring metric bases or a four-landmark construction. Strong same-day indexed matches were compared as statements: the same graph with a different resolving predicate, and the same motion rules on a different graph. Neither gives the 320-state metrics and sharp penalty for GP(8,3). The strongest plausible thesis match remains an explicit priority risk, not evidence of prior exact coverage.

## value

PASS

The canonical symmetric cubic graph gives a useful complete example of how local moves alter the geometry of all optimal landmark placements. The two graphs are both connected, yet sliding makes every state have eccentricity 12 while jumping has two eccentricity classes and diameter 5. The exact optimal penalty and explicit witness measure the loss from locality instead of just comparing diameters or exhibiting one feasible route. The complete census includes the orbit classification on which future symmetry-based comparisons can build; it is not merely a recomputation of the metric dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
