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

Each side gives one nested chain on the opposite marks, of at most b or a nonempty levels respectively. Those levels never coincide across the two sides, and empty is counted once. With equality, every size between one and the opposite mark count is mandatory, and empty must occur. Counting witness vertices and marks side by side gives order at least 2 max(a,b); counting all distinct traces gives order at least a+b+1. If a>b, a minimum host has a vertices on each shore and every left vertex is marked. The a nonempty right traces therefore fix the whole staircase after ordering left vertices by the successive new marks. If the right marks have staircase ranks j_1<...<j_b, then left rows give the b nonempty suffixes and also empty exactly if the top rank a is unmarked (also true for b=0). Every rank is fixed under side-preserving isomorphism, so the binomial census follows, and the staircase is connected. Symmetry handles b>a. For a=b=k, at 2k+1 vertices all vertices on the shorter shore must give nonempty traces, including one seeing every opposite mark. Thus the opposite marked vertices also give nonempty traces; only the extra vertex can give empty and is genuinely isolated since the shorter shore is all marked. The marked core is forced to be the staircase, with two possible named shores for the isolated vertex. A new left vertex adjacent to every marked right vertex and a new right vertex adjacent only to that new left vertex preserve nesting, connect every vertex and witness the empty trace at order 2k+2. This includes k=1. The trace supremum and VC dimension follow from sharpness at all splits and the two-point bound. Replay: RESULT.md proof, with checker lines 64–110 for small-order coverage and 113–158 for the constructions. The checker was inspected, not executed; it considers all mark splits with positive total, and its finite checks do not carry the arbitrary-size claim.

## originality

PASS

Nesting and the elementary linear trace estimate are not credited as novel. The supported contribution is the joint split-sensitive least order, connectedness penalty, and full marked minimum-order census. The strongest neighboring classifications use different graph classes, marked equivalences, or invariants, as compared below.

## value

PASS

The unbalanced and balanced cases differ in how the empty trace can be realized. The sharp connectedness penalty and all minimum-host marked classes answer a natural resource question beyond the elementary capacity bound; they specify exactly which staircase rank choices realize saturation without extra vertices. The census can be used without an exhaustive labeled-matrix search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
