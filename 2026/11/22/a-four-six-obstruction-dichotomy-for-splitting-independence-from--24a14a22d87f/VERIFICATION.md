---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In any lax split, all rows of degree at least two must meet the independence part. This part is a rectangle, so its column set lies inside the intersection of the active rows. Each active row must therefore have at most one cell outside that intersection. Conversely, taking all active rows times their common columns leaves a partial function in the complement, including the separate no-active-row case. For a failure choose two neighbors of one row outside the intersection and an active row missing each; retain two neighbors in each witness row. If there are disjoint selected pairs they give two stars. Otherwise the distinct pairwise-intersecting pairs have empty total intersection and must be the three edges of a triangle on columns, giving the six-cycle as a subteam, not necessarily induced in the original team. Every proper subteam of either example is satisfying: at most two rows remain active, and if two survive in the cycle case their original common neighbor is still present. The labelled count chooses ordered-by-label rows and disjoint unordered column pairs, or a missing-column bijection on three rows and three columns. The first term is zero for q<4, including q=1. The edge-list algorithm counts degrees, active-column incidences, and exceptional cells in linear time. A complete 3-by-3 rectangle is satisfying and contains a false cycle; this is one-way local refutation, not hereditary satisfaction. VERIFICATION.md's phrase 'either side' should be read as assigning overlap to the unchanged independent rectangle and shrinking the functional part; shrinking the rectangle arbitrarily is not valid, but neither RESULT.md nor the checker relies on that. AUDIT.json's 'column-centered' description should read 'row-centered'. These supporting-text slips do not affect the theorem or checks.

## originality

PASS

Best of checked knowledge. The mixed split is not a dependence-only coherence example or the inverse-dependence pseudoforest problem. The intersection test and its complete two-pattern minimal-falsifier census were not covered in the inspected material.

## value

PASS

A basic mixed two-variable split has a precise recognition rule, sharp refutation bound and complete labelled obstruction census across unbounded finite alphabets. The failure of downward closure makes the distinction between bounded refutations and hereditary testing substantive. This is useful as a small exact comparison case for the established two-dependence-atom classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
