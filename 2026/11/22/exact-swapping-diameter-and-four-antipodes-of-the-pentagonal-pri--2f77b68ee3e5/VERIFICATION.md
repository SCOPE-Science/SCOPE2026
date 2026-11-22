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

Two complete deterministic algorithms for the stated ten-vertex graph were executed from the actual included `enum_factoradic.cpp` and `enum_packed.cpp` sources. Each reached exactly \(10!=3{,}628{,}800\) distinct permutations, with the same diameter \(17\), all eighteen distance-shell sizes, exactly four specified antipodes, and transportation-deficit maximum \(4\) attained \(1{,}440\) times.

The executable `verify.py` rebuilds the two C++17 programs, checks those reported invariants against literal expected outputs, and explicitly applies the seventeen listed legal swaps to confirm a diameter witness. Actual checked output: `VERIFY_OK: 3628800 states; diameter 17; four listed antipodes; max transportation deficit 4, 1440 states; identical distance histograms; 17-swap witness`.

The finite enumeration is exhaustive because the factorial algorithm gives a bijective index of every ten-token placement and explores every prism-edge transposition. The separately encoded hash-map algorithm corroborates the census without reusing factorial indexing. The graph is connected and token relabelling makes its configuration graph vertex-transitive, so this one-source census covers all start–target pairs up to isometry.

Scientific limits: this does not verify any larger prism, any earlier literature's originality, or a claimed asymptotic behavior. No independent external audit has been performed.
