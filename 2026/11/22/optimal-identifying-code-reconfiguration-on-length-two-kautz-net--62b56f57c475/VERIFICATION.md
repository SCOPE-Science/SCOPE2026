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

In a fixed terminal-letter column, two omitted vertices would have identical signatures. Equality at the lower bound forces one omission per column, giving the function f. The outgoing selected sets B_b vanish precisely at a star center. If two nonempty B_b,B_c gave the same closed signature, their disjoint first-letter classes would force each to consist only of the cross-vertex (b,c) or (c,b); then the column of any third letter would omit twice, impossible. A cyclic permutation attains the bound. Exchanges change one missing symbol, so Hamming adjacency is exact. Same-center stars form a coordinate clique; different centers differ at each of the q−2 third arguments. For q≥5 no good vertex can neighbor two different-center stars, and a common neighbor of two stars in the same clique is a star. Thus counting deleted-neighbor incidences proves the degree formula. At q=4, different-center stars are at distance two only for the reciprocal choices f(b)=c, f(c)=b. For each unordered pair of centers they have two good common neighbors, and neither can be adjacent to a third star: each star already uses its sole reciprocal partner. This gives 12 degree-6 vertices, and 72 total lost-degree incidences give 48 degree-7 and 9 degree-8 vertices. At q=3 the two remaining maps are the two 3-cycles, at distance three. Counting removed edges with internal star edges restored once gives the displayed q≥4 formula. Bounded independent enumeration verified literal signatures for q=3,4,5 and the spectrum and edges of the surviving graphs through q=6; see /workspace/branches/475bc14d-f850-4146-9748-9f1c8826840a/independent_small_check.py. The two frozen standalone scripts were read, not executed.

## originality

PASS

Pass for the exact all-alphabet reconfiguration invariants, including the exceptional degree spectrum, not for the minimum size, one-omission/nonstar characterization, or ternary count in isolation. The 2019 general arc criterion actually implies the full one-omission/nonstar characterization on specialization, not just some local restrictions; the family count and Hamming model are short deductions from it. The closest inspected sources do not compute the deleted-neighbor overlaps and exchange spectra. The quoted Corollary 3.9 is Corollary 3.2 in the inspected arXiv v2; that corollary directly covers q≥4, not q=3.

## value

PASS

The degree spectrum describes how many single-sensor swaps can preserve a minimum code, not just how many codes exist. Counting the exceptional overlap at q=4 and proving its disappearance for q≥5 gives exact exchange flexibility for every alphabet size on a standard directed network. These are natural invariants independent of the established minimum-cardinality theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
