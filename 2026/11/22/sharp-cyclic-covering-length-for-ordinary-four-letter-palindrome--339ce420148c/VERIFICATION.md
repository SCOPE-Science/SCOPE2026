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

Fix one cyclic occurrence per target. For distinct abba words a gap of one would require a three-symbol overlap bba=cdd, forcing equality of all letters and hence the targets. A two-gap can only be abba followed by baab with a!=b. These transitions use each unordered pair at most once, since reciprocal transitions would isolate a two-cycle in the single ordering of q^2>=4 distinct targets. Writing r for the number of two-gaps and z for gaps at least four gives L>=3q^2-r+z. Project the cyclic ordering to first letters: three-gaps are loops and the entire projection is balanced. For even q every vertex of K_q has odd degree, so each must be incident to an omitted pair or to a long-gap edge. Counting two incidences per omitted pair or long-gap transition gives the extra q/2 lower bound. For odd q use an Euler tour of K_q; for even q>=4 delete a perfect matching first (the remainder is connected and even-degree). Each retained edge contributes its two orientations in succession at gap two; neighboring edge blocks meet at a common first letter and have gap three. Diagonal targets and both orientations of deleted pairs are inserted at their corresponding first-letter vertices at gap three. The cyclic overlaps really glue: successive gaps are at least two, so nonneighbor starts in either cyclic direction are at least four apart and have no shared positions. The supplied q=2 circle attains 12. Independent replay `python3 /workspace/reproduce_frozen.py 3` checks binary cyclic hosts directly and exact minimum overlap tours at q=2,3,4 (12,24,44). The frozen checker was inspected, not executed. Finite tests do not prove the formula for unrestricted q.

## originality

PASS

Credit the known linear binary value and the directly overlapping q=4 cyclic minimum in a distinct same-day quaternary census. Only the universal arbitrary-alphabet cyclic parity theorem and all-parameter construction are supported as distinct by this bounded comparison. Different symmetries, lengths, or partial parameter tables do not give that theorem. No within-day priority is inferred.

## value

PASS

For the natural family of ordinary reversal motifs, the exact minimum tells how short a single cyclic test word can be over any finite alphabet. The proof makes the even-alphabet cost structural via parity and supplies optimal hosts. This value is in the uniform parity classification, not a recomputation of the known small cases or a claim about biological targets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
