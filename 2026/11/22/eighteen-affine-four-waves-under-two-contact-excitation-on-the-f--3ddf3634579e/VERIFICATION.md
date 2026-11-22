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

# Finite verification

The two provided C++17 sources compile without dependencies beyond the standard library and independently enumerate all \(3^{16}=43{,}046{,}721\) states. Execute the exact commands in `RESULT.md`; expected transcripts are `results_a.txt`, `results_b.txt`, and `geometry_result.txt`. The arithmetic is entirely integer-valued, so it does not depend on floating-point rounding.

`census_q4.cpp` computes the successor from four bit-permuted neighbor masks and assigns functional-graph components and entry times. `forward_q4.cpp` separately derives the excitation mask from direct counts at each of sixteen sites and follows every trajectory to its first repetition. Both produce one fixed point, eighteen primitive four-cycles, the same eleven nonzero entry/period classes, six four-cycles with basin 676, and twelve with basin 644. `geometry_q4.py` checks all eighteen cycle representatives and all 384 spatial automorphisms, yielding the two affine-plane classes of sizes six and twelve. `witness.txt` supplies a direct, local-rule-checkable seven-update trajectory and a four-period orbit.

These checks are exhaustive only for the specified sixteen labelled vertices and three states per vertex; no claim about all graph sizes or thresholds follows. Two implementations and a geometry checker reduce correlated implementation risks but do not substitute for external independent audit. Historical-priority claims remain qualified by the possibility of unpublished or unindexed equivalent tables.
