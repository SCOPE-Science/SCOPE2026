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

# Reproducibility

From the provided source file run `c++ -O3 -std=c++17 check_bicommutant.cpp -o check && ./check`. The expected final output is `CATALAN_BICOMMUTANT_OK`. All Catalan maps on chains of sizes one through eight are generated in canonical nondecreasing order, and each one is checked against its direct composition centralizer. For all idempotents, the code computes the center of that entire centralizer, not merely the centralizing idempotents, and checks both cardinality and identity of its members.

The infinite conclusion rests on the blockwise proof in RESULT.md, especially the local adjacent-collapse generators, the induced root action, and the separating map between blocks. Checking the finite cases cannot independently validate an all-size proof. No formal proof assistant or external independent audit has been used.
