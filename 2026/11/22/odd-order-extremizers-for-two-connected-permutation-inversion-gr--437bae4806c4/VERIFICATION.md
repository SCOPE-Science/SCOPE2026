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

Passes for the repaired claim, not as printed. Frozen RESULT.md lines 44–51 incorrectly identify (1,2) with (2,1). At L_6 their words are 4261735 and 4612735, respectively, with different 321 counts. The correct pair is (2,1) with (3,2); unrestricted iteration over all cells is not repetition-free. The complete repaired RESULT.md derives the table from the prefix rank formula, proves the deletion-run criterion, and lists one representative per class. Its four duplicate pairs are disjoint and none deletes a triangular cell; the length-four base has two triple classes and two singleton classes. The checked 4-chordal bound gives the odd lower bound by integrality, while a degree-two insertion into the even ladder preserves two-connectivity and attains it. Anchored greedy ears have increments (1, at least 2) or (2, 3); equality allows no singleton step after a triangle and exactly one after a square. Hence a final singleton step comes from the unique even ladder, while a final two-vertex step is the forced operation F on a smaller odd minimizer. Both exceptional commutations were verified by explicit word identities, and F(321)=42513 handles the first triangle start. The exact cell and neighbor counts then yield 3m−2 distinct minimizers, of which m have one triangle.

## originality

PASS

For the repaired result, credit the edge bound, even ladder, and anchored-ear machinery to Verkama. The numerical odd minimum is a direct consequence once a two-neighbor insertion is used. The distinct contribution is the all-odd-order characterization by distinct insertions and the exact extremizer census refined by 321. The closest same-day comparisons count either named insertion types or a different connectivity stratum at orders beyond five, not this classification.

## value

PASS

The repaired result classifies the natural first nonempty inversion stratum of two-connected permutations at every odd order. The explicit generation, duplicate rules and 321 split distinguish structurally different extremizers; they are not a finite scan or simply an application of the known edge bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
