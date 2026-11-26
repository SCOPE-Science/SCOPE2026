---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The pure adjacency/equality classification is correct. In the finite recurrence, fixed-depth exact set interning (including repeated picks) is equivalent to both directions of the next-move condition; the terminal labels distinguish equality, adjacency and neither. I independently computed all ordered vertex choices with masks for the fourth-point profiles, without orbit reduction: widths 3–8 give twelve distinct types, and both twists at every width 9–32 give one distinct common type. For the unbounded range, a short signed cyclic gap of matching length has a mod-two constraint on its two endpoint offsets. Splitting at equal positions gives consistent new constraints because transport parities add, even when the old gap goes once around from a sole selected column to itself. In a long gap, at most one subgap is below the next cutoff; match that subgap and its parity, or leave both new gaps above the cutoff. Repeated columns respect the offset, including rungs and repeated vertices. Terminal length-one gaps preserve all horizontal adjacency. This proves the unbounded bridge through width 32 and the sharp within-family 18-vertex bound. At width nine the ordinary prism is planar and the twisted ladder nonplanar. The PASS is for the stated pure-language finding; the blanket scope remark about adding column/rung predicates should instead specify an expansion or say richer signatures are not addressed.

## originality

FAIL

A distinct earlier published SCOPE record states exactly the frozen final theorem and its sharp representative bound. This is established duplicate coverage, not a failure to retrieve literature. The signed-gap proof component does not make the exact theorem new.

## value

FAIL

The cutoff for loss of twist information is a natural logical invariant, but the frozen result recomputes a known exact classification, representative ceiling and topology contrast rather than adding a new boundary or application. The alternative tail proof bridges the same finite classification with a coarser rank-four sufficient bound than the earlier record's width 16; no independently valuable new final theorem is established as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
