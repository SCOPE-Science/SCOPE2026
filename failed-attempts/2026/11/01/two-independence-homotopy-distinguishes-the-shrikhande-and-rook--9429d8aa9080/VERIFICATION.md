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

A simple induced graph has each component of size at most two iff every degree is at most one; a vertex with two neighbors generates a P₃ as a not-necessarily-induced subgraph even if the neighbors are adjacent. Independent exhaustive enumeration from the named Cayley and rook definitions confirmed the common strongly regular parameters, the distinct local neighborhoods, and agreement of component and degree predicates on all 65,536 masks of each graph. The nonempty face counts are 1,336 and 1,192. With the given pivot list and after releasing the empty-face–vertex-11 pair, the retained genuine covering pairs number 639 and 543. Topological sorting of all 4,960 and 4,224 oriented cover relations visits every face. This proves acyclicity; the one critical vertex and only 57 or 105 critical three-cells give CW models whose three-sphere wedge type follows because all attaching maps go to a point. No integral conclusion is inferred from the mod-two check. Replay: python3 /workspace/branches/4e6a3499-bdf8-4d13-a677-8309fa9eb6c7/ind2_replay.py (saved ind2_replay_output.txt alongside).

## originality

FAIL

The 2026-10-18 Resultary record cfdca22c256f and two distinct 2026-10-25 records already give the exact integral wedges for Ind₂ of the same two named graphs. Record 910d35e0c15c also states the same reversal of the ordinary independence sphere counts. A distinct same-day record has the same theorem as well, but no within-day order is inferred. A common pivot sequence is an alternate witness for the existing classification, not a new classification.

## value

FAIL

The topology of these natural cospectral graphs and the reversal are meaningful objects of comparison, but both exact answers and the reversal were already established. The proof repeats finite enumeration and the same general Morse method with a different certificate; it does not fill an unresolved exact invariant or establish a new structural phenomenon beyond those earlier results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
