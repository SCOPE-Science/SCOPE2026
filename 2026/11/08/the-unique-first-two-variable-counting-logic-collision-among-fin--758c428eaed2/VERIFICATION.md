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

The finite classifications were checked with two executable programs. `verify.cpp` constructs every nonisomorphic tournament on at most six vertices by inductive extensions and canonicalizes each candidate under every vertex permutation, then runs directed stable color refinement using a palette shared across all structures of one order. `verify_mckay.py` independently uses McKay's complete published table to check the six-vertex equivalence partition, the two 15-bit witnesses, and all induced transitive 4-subtournaments.

Reproduction commands: `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify` and `python3 verify_mckay.py`. The expected output is in `CHECKS.txt`.

The exhaustive six-vertex computation has finite scope. The every-larger-order claim is proved by a symbolic extension of the specific witnesses, not by extrapolation. Equivalence of directed color refinement and two-variable counting logic is standard and not separately formally certified here. Independent mathematical audit has not been performed.
