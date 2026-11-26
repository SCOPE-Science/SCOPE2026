---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A proper power self-overlaps, and distinct rotations of a word overlap at the cut; thus a code has at most one member per primitive rotation class. A nonprimitive weight-three word must be a triple repetition, giving exactly n/3 exceptions when 3 divides n and none otherwise. Dividing the primitive count by n gives the stated floor. For the proposed code every prefix starts at the first 1. A proper suffix either starts with 0, starts at the third 1 and has length at least m (so the competing prefix has at least two 1s), or starts at the second 1 and has length at least B (so the competing prefix has three 1s). This checks all ordered pairs, including self-pairs. The sum of B-a for 2≤a≤m is (m-1)(2n-3m)/2, which agrees with the bound in each residue modulo three; n=3 has only the bordered word 111. Equality proves that the displayed construction meets each primitive rotation class exactly once. This is an optimal family, not a classification of all optimal families. The frozen replay is check.py alongside RESULT.md, for lengths 3 through 30; it was inspected, not executed. The proof is all-length and does not depend on this check.

## originality

FAIL

A distinct indexed record gives the same exact optimum and primitive-necklace transversal, with the displayed code reversed. Reversal is a bijection preserving weight, primitive rotation classes, and non-overlap (it interchanges the two words in a prohibited suffix-prefix equality). Thus the construction itself, not just the numerical capacity, has demonstrable equivalent coverage. The differing catalogue dates do not establish provenance, antecedence, or priority.

## value

FAIL

An explicit non-overlapping transversal of all primitive weight-three necklaces would be useful when not known: reaching the rotation bound does not follow from counting alone. Here both the bound and its attainment by this family are already supplied by an equivalent indexed result. Reversing its construction, without a new property or extension, leaves no distinct valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
