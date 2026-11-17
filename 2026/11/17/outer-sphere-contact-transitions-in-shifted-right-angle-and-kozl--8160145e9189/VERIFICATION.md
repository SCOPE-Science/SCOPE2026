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

The standalone verifier `verify_outer_shell.py` was run directly from this package before embedding. It produced:

`PASS: 1245 exact instances and 11278 assertions`

The verifier enumerates all sums of summand vertices for each listed finite instance, deduplicates the resulting coordinate vectors, and checks the maximum of all pairwise squared distances, the count of pairs at the asserted maximum, the radius-squared inequality for every candidate-sum point, the number of boundary contacts, and the direct coordinate formula. It also checks the binomial autocorrelation identity by separate finite summation through \(n=79\). The general proof, not the finite experiment, establishes the infinite-parameter statement.

The source literature confirms the right-angle Minkowski-sum realization and complete-skeleton vertices. The paper's later-degree details, arbitrary-rank facet structure, and historical-priority uniqueness are not certified by this verifier. No independent audit was performed.
