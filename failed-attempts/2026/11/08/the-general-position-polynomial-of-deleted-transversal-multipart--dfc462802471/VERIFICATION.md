---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The graph is diameter two for a,r>=3, hence a forbidden geodesic is exactly an induced P3. Cluster-graph components are exhaustively row/column independent sets, full transversal cliques, three-cell rectangles and four-cell rectangles; counting these disjoint types gives the displayed coefficients, including g_3(3,3)=48. For a=4 the signed differences b4-b3 and b5-b4 and the unimodal binomial tail isolate the precise valley 12..39. Independent direct shortest-path subset enumeration verified the 3x3, 4x3 and 3x4 cases, rather than proving infinite quantifiers by code.

## originality

FAIL

Two earlier published full mathematical texts cover every asserted finding: the October 18 T*(r,a) theorem proves the identical all-a,r>=3 polynomial and exactly the a=4 12..39 nonunimodality window, alongside a=3 and r=1,2; the October 26 categorical-product paper gives the same complete polynomial in an algebraically equivalent representation. This is exact mathematical coverage, not superficial title matching.

## value

FAIL

A sharp coefficient/unimodality classification is mathematically meaningful in isolation, but this submitted final result repeats the exact published all-set enumeration and four-part threshold; no new useful invariant, boundary or structural theorem survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
