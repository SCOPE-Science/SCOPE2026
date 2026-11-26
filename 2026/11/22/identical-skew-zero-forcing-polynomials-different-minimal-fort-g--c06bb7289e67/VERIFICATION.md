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

A nonempty terminal white set is a skew fort. Conversely no vertex of a fort can be the first forced within that fort, since any witness adjacent to it has at least two neighbors there while it remains white. Thus the obstruction test is equivalent to failure even for arbitrary legal forcing order. Simultaneously detected distinct targets can be removed sequentially: removing a different white vertex cannot destroy a previously unique white neighbor, and the color of its witness is unrestricted. The independent replay checked all 65,536 white subsets of each independently constructed graph, confirmed degree six and two common neighbors for each distinct pair, and matched all coefficients, the forcing/containment equivalence, and every supplied labeled minimal-fort row. Both graphs give 4032,3648,1760,560,120,16,1 in blue degrees 10–16 and zero below. Both have 60 minimal forts of size four, 256 of size six and none of other sizes. The four-vertex induced degree signatures are uniquely those of 4K₁, C₄ and K₃ plus an isolate; the respective counts are (16,12,32) for Shrikhande and (24,36,0) for rook. The distinction is induced geometry, not a claim about abstract isomorphism of fort hypergraphs.

## originality

PASS

Pass for the common full skew polynomial and the precise comparison of minimal skew obstructions. The rook minimum is already a consequence of prior Grundy total domination and is not credited as new. Exact same-pair PSD work and ordinary rook-graph tables use different rules; inspected results do not give the stated skew comparison.

## value

PASS

These are the canonical same-parameter nonisomorphic (16,6,2,2) graphs, already used to compare forcing variants. The common rank-generating polynomial now demonstrably loses induced minimal-obstruction geometry even when counts at all sizes agree; the triangle-plus-isolate obstructions furnish a specific separation, not just a pair of unexplained coefficient vectors. Full coefficients and labeled forts provide reusable exact benchmarks for skew forcing and fort enumeration, beyond the known rook optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
