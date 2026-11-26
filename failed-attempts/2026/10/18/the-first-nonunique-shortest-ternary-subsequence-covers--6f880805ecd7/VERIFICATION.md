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

The greedy feasibility test is exact: prefix and suffix embeddings are in disjoint intervals around a fixed covered position. Composing embeddings proves transitivity, and any shorter cover of a factor extends by the surrounding letters. Thus the primitive-candidate filter is sound and a missing primitive length precludes longer primitive words. Independently, I enumerated every nonempty position subset for each host represented by first-occurrence alphabet normalization. Grouping subsets by their spelled word and OR-ing their position masks directly tests all covers, with no primitive bound or greedy predicate. Weighting one-symbol representatives by 3 and all others by 6 gives the full 3^n texts at each length. This returns zero through 10 and one normalized failure at 11, with the exact two covers of length 6, hence the six labeled failures.

## originality

FAIL

A distinct indexed record states the exact first ternary ambiguity threshold, the six labeled texts and the same representative pair of covers. This establishes equivalent coverage, not which same-date record came first or how the records are related. The inspected earlier papers establish the phenomenon and the primitive bound, but not this exact ternary census.

## value

FAIL

The ternary minimum would be a useful sharp boundary for uniqueness and a regression example for cover algorithms. As submitted, however, the exact boundary and all witnesses are already covered by a distinct available statement, and the record does not establish a separate new algorithm, structural result or extension beyond that finite answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
