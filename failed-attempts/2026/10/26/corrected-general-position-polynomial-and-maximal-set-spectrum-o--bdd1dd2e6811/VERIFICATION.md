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

The frozen Finding's crown theorem is correct. Same-class distinct vertices are at distance 2; unmatched cross pairs are adjacent and matched cross pairs are at distance 3, using two distinct extra indices when measuring that distance. For a mixed triple {a_i,a_j,b_k}, if k differs from i,j it is on a length-2 path through b_k; otherwise a length-3 geodesic from the matched a_k to b_k through the other selected a and an extra b witnesses failure. A pure triple cannot fit on a geodesic between its extreme same-class vertices. Thus all pairs count, and all larger valid sets are pure. The pure subset sum double-counts the empty set and omits precisely n^2 cross pairs, giving the stated polynomial. The extension criterion gives exactly both full classes and all cross pairs as inclusion-maximal. Connectedness and regularity follow directly. Replay: RESULT.md lines 13–24; independent BFS/subset tests reproduced the formula and maximal masks for n=3,4; frozen verify_output.txt documents the author's wider finite enumeration only. The n=3 illustration is not itself a nonunimodality witness, but the frozen text's scope disclaimer should not be read as asserting unimodality: at n=8 the correct coefficients in degrees 2,3,4 are 120,112,140, so Proposition 4.3's unimodality assertion fails for the crown family.

## originality

FAIL

Demonstrated prior coverage: the October 12 Resultary record proves the same polynomial, the correction to the same published formula, and exactly the same general-position-set characterization. Its characterization mechanically gives the entire maximal-set list and hence the cardinality spectrum and unbounded gap; this is not a case of missing evidence or priority inferred from a same-day date.

## value

FAIL

A correct polynomial and full inclusion-maximal census are worthwhile aims, but this submission repeats the already catalogued exact feasible family and its correction of the published count. Reading off the maximal sets and missing sizes from that family adds no mathematically substantive claim requiring independent dissemination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
