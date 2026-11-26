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

Alexander dual membership is exactly the absence of a disconnected four-subset, with every subset of size at most three present. I regenerated the complex using graph-coordinate adjacency, independent induced-subgraph searches, and a direct all-quadruples test for larger candidates. The counts by cardinality were (27,351,2925,1593,324,54) with no larger faces. Independent pivot matching and complete topological sort reproduced 1877 pairs and all 17793 Hasse incidences on 5274 faces, leaving (1,1398,121) critical cells in dimensions (0,2,3). Exact signed unit eliminations of matched simplicial boundary entries independently gave 264 nonzeros on 24 rows and 84 columns, rank 12 over Q, and determinant -1 for the specified 12-by-12 minor. The Morse boundary therefore has twelve unit Smith entries; rank alone would not suffice. The Morse CW space is the homotopy cofiber of a map from a wedge of 121 two-spheres to a wedge of 1398 two-spheres; each component is determined by its degree vector by Hurewicz. Unimodular changes of bases are realized by homotopy equivalences on these wedges, reducing the map to twelve identities and zero on the other summands. The cofiber thus has 1386 two-spheres and 109 three-spheres. Integral Alexander duality with shift 24 gives original ranks 109 and 1386 in degrees 21 and 22, without other reduced groups. All facets have dimension 22, and the free nonzero lower homology obstructs shellability.

## originality

PASS

The strongest actual exact-graph statements are at ordinary cut threshold three. The strongest inspected four-cut cases are other Cartesian products, including two-factor rook graphs and path grids. No inspected theorem supplies this three-factor ternary ordinary four-cut wedge or its homology consequences; the catalogue self-match is the frozen record, not separate coverage.

## value

PASS

The smallest Hamming graph with three fully ternary clique factors is a natural comparison point for exact four-cut topology after the three-cut classification and the smaller rook-board computations. Complete integral topology of its dual is useful beyond a field-rank table: the primitive boundary calculation settles absence of torsion, and the 109 lower-degree original classes give a concrete obstruction to shellability. The distinction between threshold three and four or between two and three clique factors is mathematical rather than a relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
