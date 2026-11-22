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

Finite verification: `python3 verify.py` regenerated the \(4{,}366\) nine-sensor codes, excluded all eight-sensor codes, counted all \(117\) optimal reversal-invariant eleven-sensor codes, and matched both supplied orbit-representative tables; it returned `VERIFY_OK`.

An independently implemented C++17 bitmask enumerator (`verify_alt.cpp`) confirmed the unrestricted and invariant cardinality counts and both attainment witnesses; it returned `ALTERNATE_OK`.

The computations exhaust exactly \(\binom{27}{8}\) and \(\binom{27}{9}\) unrestricted subsets and exactly \(2^{18}\) invariant orbit selections. The proof explains why these search domains are exhaustive and why the signatures implement the identifying-code definition. The result does not cover larger alphabet sizes, longer words, or other identification radii. Independent mathematical audit has not been performed.
