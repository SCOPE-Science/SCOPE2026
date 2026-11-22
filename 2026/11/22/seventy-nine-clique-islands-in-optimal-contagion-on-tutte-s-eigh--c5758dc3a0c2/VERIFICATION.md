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

The C++17 enumerator checks all \(5{,}852{,}925\) eight-vertex subsets of the incidence construction, comparing two-neighbour infection with induced-tree complements. The independent Python checker uses the symplectic-vector construction and backtracks through all \(111{,}225\) independent eight-sets, then tests complement connectivity, infection rounds and the optimal exchange graph. Both yield \(12{,}780\) optimum sets and seventy nine-cliques plus one component of size \(12{,}150\).

The six-symbol orbit verifier enumerates \(S_6\) exactly, confirms \(40\) orbits and confirms exactly one admissible exchange for each chosen vertex. The analytic proof gives the cardinality lower bound and an exact tree-median exchange lemma. These are reproducible finite checks and mathematical arguments, not an external proof certification.

Run commands appear in RESULT.md. The intended outputs are `INCIDENCE_CENSUS_OK`, `SYMPLECTIC_VERIFY_OK`, `SYMPLECTIC_EXCHANGE_OK`, and `EXCHANGE_AND_ORBITS_OK`; failure of any asserted value stops the corresponding verifier. Claims extend neither to other graphs nor to unverified novelty or independent review.
