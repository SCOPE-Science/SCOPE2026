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

The full overlap graph is balanced and reaches the all-zero root by repeated zero appends. Its outgoing choices are forced at weight two. Suppressing those choices sends a one-one position j to j+1 (or the root) by appending zero, and to s−1−j by appending one, for s=k−1. A reflected choice at j≥floor(s/2) traps [s−1−j,j], including the possible central self-loop. Otherwise all selected paths strictly advance and reach the root. The root's unique outgoing edge fixes rotation, and the BEST factorial product is 1 because every degree is at most two. The last-exit construction is a bijection here: at a nonroot degree-two vertex the chosen last edge fixes the full order. The factor set has k+C(k,2) distinct labels, giving the stated length. A fresh unused-window search at k=3–10 matches the quoted counts, confirms every low-position last-exit vector occurs once and verifies the k=5 example up to rotation. Exhaustion in these cases corroborates the unbounded argument rather than replacing it.

## originality

FAIL

Fredricksen (1993) explicitly gives the same numerical formula and the same independent paired-position join choices for binary weight at most two in its minimum-density subclass. The scope qualifier matters: the paper excludes split-and-rejoin constructions in general. For this t=2 specialization all candidate choices reduce to switches at pairs with nested positions, so the apparently wider possible class contributes no extra cycles, as witnessed below. The frozen last-exit representation recodes the same paired choices; its alternative proof does not establish a distinct claimed count or structural degree of freedom.

## value

FAIL

The language and count are natural. However, the earlier explicit enumeration and the established choice correspondence leave the frozen result as an alternative proof of the same binary count and a recoding of its known independent choices. The record does not establish a separately valuable new invariant, structural conclusion or extension after removal of that covered content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
