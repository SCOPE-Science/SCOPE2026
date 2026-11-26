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

Every fiber of a regressive nondecreasing idempotent is an interval rooted at its left endpoint. An element of the double centralizer belongs to C(e), because e is among its tests. For each adjacent collapse t_j taking only j to j−1, commuting forces h(j−1)=t_j(h(j)) and prohibits h(x)=j at x≠j. With all t_j this forces the global center to be {0,1}, splitting on h(2); with t_j only at nonroots it forces constant behavior on any block whose root is lowered, and identity or collapse on each block whose root is fixed. Every regressive monotone map of the roots lifts to a block-constant element of C(e), so the induced action of h is central on the root chain. When that action is constant and there are at least two roots, every later block collapses to 1 and monotonicity collapses the first as well. A single root is covered by the global center. For identity root action, the cross-block witness in Step 4 commutes with e: successive whole blocks up to B_j map to B_i, with image of each root s_i and with a nonroot image s_i+1 only on B_j; order and regressivity hold at the boundaries as well. Evaluating at s_j+1 distinguishes any unequal choices on the two nonsingleton blocks. The reverse containment follows because 0 and 1 commute globally and e commutes with all its centralizer. Thus the singleton chain and both endpoint idempotents have the claimed exceptions. The source checker implements direct composition over n≤8; it was inspected, not executed, and the all-size result rests on the proof.

## originality

PASS

Pass for the center of the full idempotent centralizer, not for the block model, the description of first centralizers, or their size. The closest full-centralizer theorem gives a membership criterion for the test transformations. It does not classify simultaneous commuting with them, and the mixed-block exclusion genuinely uses non-idempotent tests that commuting-idempotent results do not account for.

## value

PASS

This is a uniform structural invariant for all idempotents in a natural family of noncommutative finite monoids. Regardless of the size and block structure of the centralizer, it reconstructs any nontrivial e as the only central element other than 0 and 1. The non-idempotent witness explains why smaller commuting-idempotent censuses cannot give that reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
