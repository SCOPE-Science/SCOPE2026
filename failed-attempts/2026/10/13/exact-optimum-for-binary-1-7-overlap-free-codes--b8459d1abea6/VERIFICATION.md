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

For any nonempty admissible binary code the length-one prefix and suffix sets are disjoint and hence are opposite singletons. At n>=14 the seven-bit boundaries are disjoint; their compatibility is necessary for every cross-pair and sufficient for allowing all middle blocks. I rebuilt compatibility by string slicing and independently generated all common suffix neighborhoods by iteratively adjoining the intersection with each prefix row (include/exclude induction, not the frozen lectic traversal). Each neighborhood can be paired with all prefix rows containing it, bounding every biclique. This gave 1,944 distinct neighborhoods, optimum 744, optimal side sizes (24,31) or (31,24), and 31 suffix partners for the first 24 prefixes. Lower-cutoff values 64 and 216 also reproduced. The exact finite search and boundary reduction prove the claimed quantifier. The support note's Python 3.8 minimum is inaccurate (the bundled script uses int.bit_count, available in 3.10+); this is not a defect in the bound.

## originality

FAIL

A distinct indexed Resultary record explicitly gives the same exact theorem for all n>=14 under the same ordered-pair and self-overlap rules. Its different branch-and-bound certificate does not differentiate the mathematical finding. This is equivalent coverage, not an inference about priority from record dates. The motivating paper alone only gave a construction and a weaker upper bound.

## value

FAIL

The cutoff and upper-bound question are genuinely motivated in the primary literature, but this delivered finding is a covered exact value with the existing construction and graph reduction. The alternate traversal corroborates correctness but is not asserted or established as a separately useful methodological result, complexity improvement, or classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
