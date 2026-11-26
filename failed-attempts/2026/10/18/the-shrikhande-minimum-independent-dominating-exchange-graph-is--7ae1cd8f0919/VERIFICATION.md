---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

No pair dominates since each closed neighborhood has seven vertices. The independently reconstructed minimum family consists of the 32 triples in the two stated translation orbits. A one-vertex exchange between independent dominating sets is a slide: the new set must dominate the removed vertex, and no unchanged vertex was adjacent to it, so the arrival vertex is adjacent to it. In coordinates, the cross-orbit overlap shifts are D={(0,0),(1,2),(3,1)} with no two-vertex overlaps within an orbit. The triangles are the 32 stated faces and each primal edge is in two faces. The displayed linear map has unit determinant and sends D to D'={(0,0),(0,3),(1,0)}, proving the graph isomorphism. The separately written /workspace/branches/409e5724-a412-4f41-9e56-88ea883e24de/independent_structural_check.py reconstructed all 32 and 48 masks matching the frozen certificate and independently checked the map and all-source distances (1,3,6,9,9,4). Analytically, two steps within a part project to Cayley differences D'-D' minus zero, exactly the standard Shrikhande connection set C, so the even levels have sizes 1,6,9. D' reaches three vertices at distance one and D'+C reaches twelve distinct vertices including those three, giving nine at distance three. The remaining four are at distance five because the even part is exhausted within four steps. Translation and part swap with coordinate negation give the same layers from every start. The frozen verifiers were inspected, not executed.

## originality

FAIL

A distinct Resultary theorem identifies the entire optimizer family as the triangles of an explicitly isomorphic edge-disjoint copy of Shrikhande on the same labels. Under that identification the exchange condition is mechanically the triangle-dual adjacency, and the slide condition is automatic by domination. Combining it with the known recognition of that dual gives precisely the frozen graph. Even the displayed correspondence is the catalogue coordinate map up to an affine symmetry of the target. This is demonstrable coverage by a distinct record and a known graph identification, not an assertion that the later-indexed catalogue result had priority over the frozen result.

## value

FAIL

The choice of the optimum-configuration graph is natural and the exact slide diameter would be useful if unknown. Here, however, the whole graph follows mechanically from the indexed exact optimizer-to-triangle identification and the known dual. The alternative coordinate map is just a target symmetry, and the remaining narrow numerical invariants are distance data computed from that already determined graph. No independently useful unresolved invariant remains in the submitted claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
