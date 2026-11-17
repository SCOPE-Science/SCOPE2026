---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For the specified 12-vertex cubic Tietze graph with 18 ordered edges, independently generated all 1052 (augmented) matching faces. Counts of nonempty simplices by dimensions 0..5 equal (18,117,335,408,165,8). The explicit staged vertex-toggling matching with pivot order 11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12 has 518 augmented pairs and 16 remaining four-edge faces; removing the empty pair leaves 517 ordinary pairs, one vertex, sixteen 3-cells. Independent Hasse topological sort visited all 1051 ordinary face nodes and 3744 cover arrows, so the integral CW type is wedge^16 S3. Edge-label permutations induced by given D6 r,s yield signed chain Lefschetz characters on rotations (16,0,-2,0,-2,0) and zero reflections; this decomposes into four one-dimensional characters plus 3 copies of each 2-dimensional rational character. No integral D6 lattice claimed.

## originality

PASS

PASS: A full matching complex of the triangle-expanded Petersen (Tietze) graph, not its perfect matching set, is new relative to checked forest and outerplanar matching-complex theorems and flower-snark perfect-match counts. Existing Petersen graph matching results are not automatic under a vertex-to-triangle expansion. The exact dihedral rational character adds symmetry information absent from these theorems. Equivalent line-graph independence computations remain a priority risk.

## value

PASS

PASS: The Tietze graph is a canonical cubic nonplanar triangle-inflated Petersen graph. Its complete finite matching-complex sphere wedge and full D6 homology character are natural, exact, non-obvious graph invariants; they distinguish triangular inflation from forest/outerplanar behaviors and are not merely a cheap dimension-one test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
