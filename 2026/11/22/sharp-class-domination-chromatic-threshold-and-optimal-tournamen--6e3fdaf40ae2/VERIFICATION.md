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

# Reproducible checks

The theorem is proved symbolically in `RESULT.md`: the class-capacity lemma, explicit small orders, standard optimum-colouring normal form and existence of near-regular tournaments suffice for every integer in scope.

Run `python3 verify_constructions.py`. In the finalized package, the standalone program checks the complete Kneser edge partition, pairwise intersection of all edges of each colour class and the existence of an actual common-neighbor witness, for every integer order from five through one hundred. Expected terminal marker: `CONSTRUCTIONS_OK`.

Run `c++ -std=c++17 -O2 -Wall -Wextra count_optimum.cpp -o count_optimum && ./count_optimum`. This independently enumerates every tournament orientation on five or six centres, directly reconstructs all classes and tests properness, coverage and common-neighbor witnesses. Expected results: `n=8 count_per_triangle=24 unlabelled=1344`, `n=9 count_per_triangle=5184 unlabelled=435456`, then `TOURNAMENT_CENSUS_OK`.

These finite computations are corroborative, not exhaustive proofs for all orders. The accepted proof requires the previously published classification of optimal proper two-subset Kneser colourings; direct original-full-text comparison is limited as described in the scientific review. No independent audit or proof certification is claimed.
