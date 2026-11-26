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

The ordinary cut dual on all 3n vertices contains exactly the sets all of whose triples are connected. For n≥5 its 16n triangles consist of column triangles, straight paths and corners. On four vertices the triple condition forces minimum degree two; no graph edge lies in two triangles, ruling out diamonds and cliques, and every four-cycle is a product square (two opposite cycle steps and two opposite color steps). Each square's opposite pairs force a possible fifth vertex to meet all four corners, which is impossible. A corner triangle identifies a unique tetrahedron and the deleted diagonal subsequently lies in just one triangle. A straight path's endpoints have a unique common neighbor, including at n=5. The indicated elementary collapses therefore leave triangulated prism boundaries with binom(3n,2)−15n additional bare edges. The n prism boundaries meet in disjoint column disks in cyclic order. Disk inclusions are cofibrations: glue along a spanning path, and the final attachment along two disks adds one loop as well as one sphere. Each extra bare edge between points of the connected core adds another loop. Integral combinatorial Alexander duality therefore gives the two stated free groups with the stated degree shift. The pure complex has nonzero homology below its top dimension, ruling out shellability.

## originality

PASS

The closest ordinary-cut comparisons use the same geometric strategy but do not cover a triangle factor with a long cycle. The same-graph open-neighborhood result classifies a different complex. The distinct supported content is the triangular-prism dual and exact integral ordinary-cut homology on this graph family.

## value

PASS

The triangle is a natural short-circumference boundary where product squares coexist with actual triangle columns. The theorem detects an integral change from a retained torus on longer tori to one sphere class per prism, and gives complete cut homology, including non-shellability, rather than only a count of two-cells or finite-field Betti data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
