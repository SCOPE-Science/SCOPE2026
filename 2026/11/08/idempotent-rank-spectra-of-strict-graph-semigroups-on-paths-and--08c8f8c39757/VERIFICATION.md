---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

This assessment is of repairs/2/RESULT.md. The original formulas are correct; the repair changes the scientific focus and attribution, not the sequence. Distinct nonempty vertex fibers must be disjoint edges, and an edge between two image values would have a four-element preimage. A partial map is idempotent exactly if every image value is fixed, so its fiber must contain that value. Thus allowed choices are precisely independent sets in the conflict graph of oriented edges. In alternate L_i,R_i order equal and neighboring underlying edges account for all pairs at distances one and two and some at distance three; the remaining distance-three pairs are R_i,L_(i+2), whose selected endpoints are adjacent. All other pairs are compatible. The same argument works cyclically with either directed arc and C3 is the complete six-vertex exception described in the proof. This gives the claimed cubes, including the empty list at P1. In a cyclic list of N=2n entries, k pointed choices correspond to ordered gaps at least four summing to N; there are N binom(N−3k−1,k−1) such pointed choices when 1≤k≤N/4. Dividing by k and including the empty set yields the uniform formula including k=n/2 and k=0. The linear gap count yields the credited path formula and its series. Idempotent fibers stay in their original component and isolated vertices contribute 1. A cube's earlier and later neighbors, up to three each, form two cliques, so the original Chudnovsky–Seymour Theorem 1.1 applies; the coefficient signs exclude nonnegative roots, and Newton's inequalities in the actual polynomial degree give the stated normalization. The earlier recorded checker output is finite and was not rerun. Independently run `cd /workspace && python3 checks/rank_reviews.py` for direct definition checks on P1..P5 and C3..C5 and every conflict pair on P1..P20 and C3..C20, separate from the universal argument.

## originality

PASS

The original's originality assessment is rejected for the path rank enumeration and general selected-endpoint characterization: the earlier indexed path record states them, and the positive binomial restatement alone does not rescue them. The repaired result focuses on the distinct exact conflict-graph identification with cubes and its cycle rank and degree-two root consequences, with the path series and general real-rootedness theorem explicitly credited. The compared statements establish ingredients and partial cases but do not identify those strict-idempotent complexes with the cubes or state the resulting full cycle rank/root classification.

## value

PASS

The repaired structural identification encodes which local rank-one fibers may be selected together, not just a translated list of counts. It gives the full rank spectrum of the cyclic strict semigroups and a global negative-root and coefficient-shape result for the maximal-degree-two family. The cyclic closure and perfect-matching boundary make it a natural extension, and the graph model supplies a route to use general independence-polynomial results. Recomputation of the existing path enumerator is not the assessed contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
