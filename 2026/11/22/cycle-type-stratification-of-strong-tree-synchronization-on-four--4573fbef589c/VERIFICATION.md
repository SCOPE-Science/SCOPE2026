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

# Reproducibility and scope

Run `c++ -O3 -std=c++17 verify_bfs.cpp -o verify_bfs && ./verify_bfs` and independently `c++ -O3 -std=c++17 verify_relax.cpp -o verify_relax && ./verify_relax`, then `python3 verify_witness.py`. All three succeeded from supplied sources. The matching exact histograms are in `bfs.out`, `relax.out`, with the explicit mask witness in `witness.out` and `witness.json`.

Both exhaustive programs cover 1,048,576 total commutative binary tables for each of the five unary permutation conjugacy classes, without statistical sampling. The first uses subset-height closures; the other uses shortest-derivation label setting. The separate witness checker tests the unique newly appearing masks through height eleven. The proof uses algebraic conjugacy for all 24 unary permutations and a fixed-point-free centralizer argument for the 56 state-isomorphism classes.

Limitations: exact only for four states with unary permutation and commutative binary operation; no claim of human or independent external audit.
