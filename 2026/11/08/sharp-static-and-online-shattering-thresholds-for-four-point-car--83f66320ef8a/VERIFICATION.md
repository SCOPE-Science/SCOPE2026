---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The 2x2-positive corner constraint forbids VC shattering of a triple: positive diagonal pair forces the third corner. Explicit two-query witnesses handle m,n≥3 and strips, and concept counts handle 2x2 and 2x3 boundaries. A root-positive fixed-rectangle class has online rank at most two because a second positive query fixes one or both remaining row/column parameters; hence whole Ldim≤3 and strip Ldim≤2. A complete eight-leaf 3x3 depth-three tree embeds into larger grids, proving the remaining lower bounds. Independent full exact recurrence yielded (0,0),(1,1),(2,2),(2,2),(2,3),(2,3) on six grid sizes.

## originality

PASS

The first 3x3 (VC,L)=(2,3) example is **already a special case** of the 2026-11-02 exact closed-neighborhood theorem on H(2,3): complementing each closed rook neighborhood yields precisely a 2x2 rectangle, preserving VC/Littlestone ranks by swapping labels. The surviving original assertion is the uniform all-m,n fixed-cardinality classification, including every narrow strip and the global Ldim bound; neither unrestricted combinatorial-rectangle dimensions nor the isolated 3x3 closed-rook case directly state the all-grid result.

## value

PASS

A natural uniform K_{2,2} incidence concept family has a complete two-parameter static/adaptive dimension table, including exact narrow-domain boundaries. The all-grid classification extends beyond the previously-known 3x3 special case and gives a reusable exact benchmark for restricting set-product hypothesis families. No arbitrary downstream theorem is needed for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
