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

For two perfect matchings, a selected edge distinguishes them exactly when it belongs to their symmetric difference. Each component of that difference is an alternating even cycle whose vertex complement is matched, so hitting every nice cycle suffices. Conversely the two alternating halves of a nice cycle extend by the same complementary matching, so each such cycle must be hit. I checked the explicit affine-to-LCF isomorphism on the complete edge sets. In the LCF graph I independently enumerated simple cycles by paths with fixed least vertex, deduplicated by edge mask, and used an exact cached complementary perfect-matching recursion. This gives 42 matchings and 603 nice cycles with all six stated length counts. Filtering the complete size-eight and size-nine mask families by the nice cycles gives 0 and 13,608 hits; monotonicity excludes every smaller size. Indexing nine-masks by eight-edge cores constructs every one-replacement edge and gives the exact degree histogram, 104,490 edges, and one component of size 12,636 and 108 of size nine. For each small component I verified an explicit grid characterization: its triangles partition into rows and columns intersecting at singletons, and edges are exactly pairs sharing a coordinate. Seven-edge core matches to the giant certify a two-replacement bridge from every small component (eight-edge overlap is impossible across one-replacement components). The threshold is therefore exactly two.

## originality

PASS

The forcing criterion and its nice-cycle formulation are prior general theory. The distinct bounded contribution is the exact Pappus optimum and the geometry of all optimal observation sets. The general bounds underdetermine the optimum and provide no exchange census. The closest inspected Pappus exchange computations use either perfect matchings or minimum maximal matchings as states, not optimal forcing sets; the analogous global-forcing census for Heawood concerns a different graph. No inspected statement or implication supplies the Pappus census. This is not a claim of historical priority.

## value

PASS

The exact number of membership observations needed to distinguish all matchings on this classical cubic incidence graph is a well-motivated invariant between nonmatching generic bounds. The result goes beyond the scalar optimum: 108 isolated rook components and one giant contrast sharply with connectivity under two simultaneous replacements. This quantifies how freely optimal measurement sets can be modified at fixed cost, and the nice-cycle census gives an independent transversal interpretation. These fixed-graph data are useful for comparing observation and reconfiguration behavior, not a generic computation on an arbitrary small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
