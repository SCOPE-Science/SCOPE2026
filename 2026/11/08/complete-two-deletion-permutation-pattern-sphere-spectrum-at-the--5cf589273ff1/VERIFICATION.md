---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The domain has exactly 7!=5040 permutations, each with exactly C(7,2)=21 two-position deletion histories. The map from any retained tuple of distinct values to its relative-rank pattern uniquely represents the receiver output. Enumeration of every source and history computes the set of unique S5 standardized patterns, then increments one cell by its size. Independently reimplemented enumeration using direct rank comparison and reproduced all 20 nonzero histogram cells, the 0 at s=20, both maximal witness words and sum_s s H7(s)=55116; sum H7(s)=5040. Since this is a FINITE theorem, complete enumeration is an exhaustive computer-assisted proof, with no extrapolation to n>7.

## originality

PASS

The correct deletion-pattern model and first 2-prolific length were known. Original Homberger and Bevan manuscripts provide maximum and near-maximum characterizations but not the exact 5040-element sphere-size frequency spectrum or isolated missing value 20. A complete self-contained finite census is an independently motivated contribution.

## value

PASS

An exact output-ambiguity distribution for the natural two-deletion/standardized permutation channel at the first length where all histories can be distinguished; it records all attainable values, nonattainable 20, and exact mean. This nonarbitrary finite boundary is motivated by permutation-pattern packing and deletion reconstruction, even without a general generating function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
