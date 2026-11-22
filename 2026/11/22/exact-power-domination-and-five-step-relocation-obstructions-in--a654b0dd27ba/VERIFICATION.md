---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The claim is a finite exhaustive classification for a graph with 27 vertices. Verification used the *actual programs accompanying this result*, executed as `sh REPRODUCE.sh` with Python 3, C++17, and NetworkX installed.

`verify_bitset.py` exhausts all 27 singleton, 351 pair and 2,925 triple candidate starting sets, constructs all 567 optimal states and all 160,461 unordered pairs, and checks every shortest-path distance. `verify_group.cpp` independently uses a Cayley-group graph presentation and C++ bit masks and repeats the complete census and distance checks. `verify_orbits.py` verifies the graph isomorphism between presentations, enumerates all 54 graph automorphisms and proves 11 optimum-triple orbits and eight maximum-penalty-pair orbits by finite enumeration.

All three programs completed and printed PASS. The two full-pair distance computations agree on jump and slide edge counts, eccentricities, and all six penalty-histogram bins. The tested result does not extend to unexamined larger graphs, different propagation rules or sensor budget changes. The source comparison is same-model only and is subject to the historical risks reported in REVIEW.md; no independent audit has been performed.
