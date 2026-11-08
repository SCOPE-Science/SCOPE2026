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

The proof uses the explicit longest-path occupancy criterion, the classification of one-vertex maximal feasible sets, and exact binomial counting. The external input is only the established notion of a \(k\)-path vertex cover and the elementary longest-path criterion for complete multipartite graphs.

The accompanying `verify.py` independently constructs each tested graph from its multipartite adjacency relation and searches for ordinary paths on \(k\) distinct vertices, without using the occupancy criterion to decide feasibility. It compares all admissible and inclusion-maximal cardinality coefficients against the formulas. Execution with Python 3 standard library produced:

`VERIFY_OK instances=557 independently_tested_subsets=320576 all_and_maximal_polynomials=PASS bipartite_parity_cases=PASS`

The direct enumeration covers every multipartite partition of orders \(4\) through \(10\) with at least two positive parts and the tested range \(4\le k\le\min(N,8)\). Larger balanced bipartite parity coefficients are checked by exact integer arithmetic using the binomial formulas through \(m=24\). No finite enumeration is asserted to prove the unrestricted theorem; the written combinatorial argument supplies that proof. An independent mathematical audit has not been performed.
