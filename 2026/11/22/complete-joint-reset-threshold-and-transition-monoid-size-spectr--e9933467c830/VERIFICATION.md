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

Independently enumerated all unordered pairs of four-state maps with weight two off the diagonal, recovering the ordered labeled census. I computed monoid size by closure under prepending from the identity. For reset length I worked backward from all singleton target sets under inverse images, using subsets of the four states. After d steps the reached sets are the full inverse images of singleton targets under words of length at most d. The first appearance of Q is therefore exactly the shortest constant word length, and closure without Q is exactly the no-reset case. This matched every CSV cell (179 distinct cells, exactly 65,536 automata), all row totals and extrema, the given (8,176) witness, and the absence of lengths greater than 9. Independent conjugation with all 24 permutations, plus exchange of letters, gives the exact computed sets of threshold-nine pairs for sizes 128 and 145, each of cardinality 48. The conditional maximum falls from 176 at length 8 (and each of 3–7) to 145 at length 9. The empty word contributes the identity to monoid size but does not reset four states.

## originality

PASS

Pass for the complete joint distribution and the sharp comparison of conditional maximum sizes across reset thresholds, not for the existence of the two length-nine examples or the isolated pair (9,145). The four-state examples are classical, and Trahtman expressly tabulates the CPR example at size 145 and length nine. Holzer–König give a two-generator construction whose size lower bound already specializes to 176 at four states. No inspected source couples such monoid-size information to the full labeled threshold distribution or establishes the exact 176-to-145 joint boundary across the two levels.

## value

PASS

Shortest control to a constant and the total number of behaviors of the two generators are natural but different structural invariants. Four states already separate the fastest reset thresholds, the longest reset thresholds, and the global monoid maximum. The exact joint table exposes a sharp boundary not visible in either marginal or in known extreme examples and gives a reusable labeled benchmark for questions about their dependence. Its value is the exact coupling, not recomputing a known reset bound or CPR's size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
