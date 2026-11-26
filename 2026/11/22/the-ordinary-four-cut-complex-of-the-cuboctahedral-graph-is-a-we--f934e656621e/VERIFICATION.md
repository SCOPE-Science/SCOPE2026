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

The dual is precisely the complex with no disconnected induced four-subset. Enumeration via the geometric cuboctahedron independently found 126 connected four-sets, 24 five-faces, no higher dual faces, and the stated primal face vector. Independently replayed all 132 supplied pairs in cube-edge labels, requiring a unique proper coface at each deletion; the residual face vector is (12,60,112). A separate greedy collapse in geometric labels reduced the dual to (12,66,118) in 126 moves, also of reduced Euler characteristic 63. The original dual's complete two-skeleton makes it simply connected, so its collapsed two-complex has free H2 of rank 63 and is a wedge of 63 two-spheres by Hurewicz and homological Whitehead. Integral Alexander duality on 12 labels puts its cohomology in primal homology degree 12-2-3=7. The primal full five-skeleton gives 4-connectivity, and Hurewicz with vanishing H5 and H6 gives 6-connectivity. An integral basis represented by seven-spheres then gives the claimed wedge. Purity follows from the 369 distinct complements, each of size eight.

## originality

PASS

The inspected exact and nearby statements do not give either homotopy type for the ordinary four-cut of this graph. This is a bounded comparison, not a priority determination.

## value

PASS

The natural intermediate cutoff for a standard named graph has only top-dimensional homotopy, in contrast to both adjoining mixed-dimensional wedges. This determines an integral homotopy type and its dual in a case not handled by the complete-skeleton shortcut; it is more than a face count or a field Betti calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
