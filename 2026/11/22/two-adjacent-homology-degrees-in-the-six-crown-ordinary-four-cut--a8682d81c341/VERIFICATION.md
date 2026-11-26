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

Disconnected four-sets have shore splits 4+0 (all), 3+1 (the singleton misses its matched vertex), or 2+2 (both matching edges are absent); these disjoint classes have 30, 120, 15 members. A face of the dual is exactly a set containing none of them. The separate exact replay builds the full face poset and reproduces 768 faces and 350 disjoint matching pairs; topological sorting all 2,832 covers in the match-reversed graph reaches all 768 nodes. With orientations by increasing vertex order, each signed pivot contributes −[u:f]/[u:t] to the other facet terms. Acyclicity makes the gradient recursion finite, and the 66 integral coefficients from the unique critical four-cell are all zero; mod-two ranks are not needed. Forman's theorem gives one vertex, 66 three-cells, one four-cell and no other cells. The three-skeleton is a wedge of 3-spheres, is 2-connected, and Hurewicz identifies its π3 with H3; the attaching map has the computed zero degree vector and is nullhomotopic. Alexander duality for 12 vertices takes degrees 4 and 3 to original reduced homology degrees 5 and 6 via 9−i, with ranks 1 and 66 and no torsion. Purity follows from equal complement sizes. The lower-dimensional field homology obstructs both pure shellability and Cohen–Macaulayness over every field.

## originality

PASS

The strongest inspected neighboring results are for ordinary four-cuts of the five-crown and for ordinary three-cuts of general crowns. Published complete-bipartite and Cartesian prism theorems do not include the six-crown. No exact equivalent or covering result was established in the inspected material.

## value

PASS

The six-crown is the next crown after the inspected five-crown at the same natural cutoff, and the complete bipartite graph is a closely related benchmark. The exact example changes the pattern from a single reduced homology degree to two adjacent integer degrees, neither top-dimensional, and identifies an integral wedge for the dual rather than merely computing field Betti numbers. It supplies a specific useful test case for structural or computational predictions about cuts of crowns and matching deletions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
