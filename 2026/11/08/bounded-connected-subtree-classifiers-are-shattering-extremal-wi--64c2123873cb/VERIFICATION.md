---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. For any shattered S, the all-positive trace forces its Steiner hull to have size <=r; any queried internal hull vertex cannot be excluded while maintaining positive queried vertices across both sides, hence S must be its leaf set. Conversely, fixing all interior Steiner vertices and toggling its leaves realizes the full strong-shattering cube; the 1- and 2-vertex cases work separately. U maps bijectively to L(U), giving equality of concepts and shattered supports. In a star, the leaf (r-2)-skeleton and center spokes give the asserted wedge of circles and spheres; standard simplex-skeleton homology applies. Independently enumerated all supports of a 5-vertex path and 6-vertex star at every cap and confirmed exact criterion.

## originality

PASS

PASS with historical-priority limits. Munaro (2016) and Kranakis et al. earlier bound VC dimensions through maximum-leaf spanning trees; subtree polynomial/leaf-count optimization is established. Their statements do not give a size-capped all-support leaf-hull iff shattering theorem, a fixed-outside Boolean cube, or star shattered-complex homotopy. Resultary semantic search found adjacent clade and tree-path query systems with different concept families, not a stronger covering theorem. The exact strong-shattering equivalence and mixed-dimensional topological consequence survive; older lopsided/convex-range aliases remain a risk.

## value

PASS

PASS. Membership-query concepts on budgeted connected tree subgraphs are natural classification objects. A complete description of every shattered support and strong shattering at every budget is more informative than a scalar VC bound; the explicit nonpure, multi-degree homology star complexes provide a meaningful structural/topological consequence, not mere recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
