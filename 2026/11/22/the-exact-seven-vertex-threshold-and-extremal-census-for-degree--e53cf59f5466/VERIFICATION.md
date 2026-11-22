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

# Verification

Build and run `verify.cpp` using a C++17 compiler, e.g. `c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify && ./verify`.

The supplied program enumerates **all** 21-bit masks representing simple graphs on fixed seven labelled vertices, checking masks with at most fourteen present edges. Every unordered bipartition is tested through the 63 nonempty sides not containing vertex six. It checks all opposite-shore degrees against two. It asserts exact immunity counts zero at edge counts zero through thirteen, exactly 15,015 at fourteen, and that the ten explicitly supplied representative-orbits are disjoint and their union coincides with the complete enumerated set.

Exact observed output:

```text
EXHAUSTIVE_LABELLED_7_VERTEX_2_CUT_CHECK_PASS
NO_IMMUNE_GRAPHS_AT_0_THROUGH_13_EDGES_PASS
MINIMUM_14_EDGE_IMMUNE_COUNT_15015_PASS
TEN_DISJOINT_ISOMORPHISM_ORBITS_PASS
ORBIT_SIZES 105 2520 2520 1260 2520 1260 630 2520 1260 420
VERIFY_OK
```

A separate cross-check using independently supplied seven-vertex unlabeled graph-atlas representations also found ten types with the same degree sequences and orbit-size total. The standalone certificate does not need that atlas or an external package.

The result is a completely enumerated **finite** classification. It does not certify any all-order asymptotic conjecture. Historical priority is provisional; no independent audit has been performed.
