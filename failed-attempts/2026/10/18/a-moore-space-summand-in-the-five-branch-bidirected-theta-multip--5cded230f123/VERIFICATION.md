---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Every selected arc uses one of four directed hub slots, so enumeration through size four is exhaustive. A fresh chain computation (/workspace/branches/475b611c-e288-4f7d-b1fd-86ea4dadd189/independent_check.py) gives face counts 20,130,320,240, checks the chain condition, and obtains 208 unit factors and one factor 2 in the unreduced simplicial third differential. The rank of the second differential is 111: the mod-101 lower bound is already the upper bound from the chain condition. A separate in-memory reconstruction of the stated nonempty-face matching gives 297 pairs, critical counts (1,1,42,72), and all 710 nodes visited in the acyclicity check on 2180 incidences. Projecting the critical triangles to the unique critical edge gives 24 nonzero coefficients, with coefficient -1 at mask 4616. Consequently one two-cell attaches by degree -1 on the circle, and the union of this cell with the circle is contractible; quotienting it gives the two-skeleton wedge of 41 two-spheres without changing homotopy type. Hurewicz then identifies the higher attachments with their integral degree matrix. Its rank and sole torsion factor follow from the independent nonsingular part of the simplicial Smith computation: ker(d2) is primitive, so the cokernel of d3 has the same torsion as H_2. The 40 unit entries, one degree-two entry and 31 zero attachment columns give the asserted wedge. The check is not based on the frozen recorded success markers.

## originality

FAIL

The distinct Resultary entry 027fb88d517d explicitly gives the identical n=5 integral homotopy type as one case of a four-size classification. Two other indexed statements also cover n=5 exactly. This is demonstrated coverage, not an inference about priority from the same-day date. The academic multipath and chessboard results inspected do not themselves decide the restricted bidirected case.

## value

FAIL

Integral torsion and a full homotopy type in an unstable natural graph family are worthwhile invariants. However, this frozen single-instance formula is already expressly available in the precise branch size, in more than one indexed classification. Its alternate matching and computational checks corroborate rather than extend the exact scientific claim. No additional unknown invariant or new structural theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
