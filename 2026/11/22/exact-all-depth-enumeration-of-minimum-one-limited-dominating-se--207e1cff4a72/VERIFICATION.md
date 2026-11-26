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

A vertex has at most one edge at a first difference before the final coordinate: that position must immediately precede its maximal constant suffix. In a bottom nine-vertex block only diagonal corners can have edges leaving the block. Each nonempty terminal triangle therefore needs at least two selections by the one-limited condition; two empty triangles are incompatible because the transposed off-diagonal endpoints then have no selected neighbors. One empty triangle forces two selected transposed neighbors, each of which forces its entire triangle to be selected. This proves the six-per-block bound, including in partial configurations with deferred outer domination. The unequal-last-symbol construction attains it: local triangles have two selections, and the linked endpoints have identical selection status. With six selections, either the three omitted symbols prescribe an involution and give four patterns, or one triangle is empty and the other two are full, giving three more. At a single cross edge a flag 2 must meet 3; a flag 0 can meet 0 or 3; selected-selected pairs are all allowed. The three fresh edges use distinct child corners, leaving the diagonal child corners untouched. Restricting an optimal parent to its labelled children and gluing these exact profiles are inverse operations; no flag 2 can survive at completion. For n=1, K3 admits exactly three minimum pairs. RESULT.md line 28 uses 'dominating set' as shorthand in this one-limited context, not as an ordinary domination-number claim.

## originality

PASS

The exact labelled census at arbitrary depth, not the known optimum size or the complete depth-two optimum census, survived the comparisons. The four-choice lower bound does not exhaust the configurations or determine the recursion.

## value

PASS

The transfer solves the exact finite optimizer-enumeration problem for a natural recursive graph family where only sizes and a restricted construction were established in the closest sources. Its treatment of owed domination versus available capacity explains how optima compose, and produces the exact census rather than just another family of attaining sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
