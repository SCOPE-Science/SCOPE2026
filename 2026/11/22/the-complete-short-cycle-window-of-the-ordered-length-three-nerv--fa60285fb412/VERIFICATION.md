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

The ordered total-length definition gives normalized free chain groups, with adjacent repetitions dropped after signed face deletion. An independent BFS/tuple construction and integer Smith changes of basis reproduce boundary rank triples (2,4,8), (3,9,23), (4,16,35), (5,25,42), with unit nonzero invariants and H1=0. This gives free (H2,H3) ranks (0,16), (0,9), (9,5), (5,6). The full integral cutoff-two H2 kernel bases have sizes 8,7,5,6; after embedding into the target and applying the target D3 row transform, all coordinates beyond the nonzero Smith pivots vanish. Unit pivots prove actual integral boundary membership. H1 maps to zero and the source has no higher cells. For homotopy, triangle relations replace each directed 1-cell by its shortest unit walk, with inverse edge orientations identified by backtrack triangles. Two complementary arcs of lengths at most three compress to the same cell for n=3 through 6; the sole graph loop is killed. The triangle compression uses the triangle inequality on the rest of each walk. Degree-two Hurewicz and the Whitehead exact sequence supply sphere maps for free H2 and H3 bases; the simply connected homology Whitehead theorem yields the stated wedges. This proves homology vanishing of the inclusion, not an assertion about arbitrary cycles or all cutoffs.

## originality

PASS

The supported distinct claim is the exact four-entry integral homotopy classification at cutoff three and its complete transition comparison. The cutoff-two ranks, framework, and stable range are not fresh claims. Closely related results do account for much of the transition reasoning but not for the four target ranks and homotopy types.

## value

PASS

The high-girth condition singles out exactly this finite window before any calculation. The mixed wedges for C5 and C6, contrasted with the pure C3 and C4 wedges and the stable circle summand, detect the first exceptional higher-dimensional homotopy behavior. The zero transfer tells a researcher interpreting the persistence barcode that the target two-dimensional classes are new, not just numerically similar to classes at cutoff two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
