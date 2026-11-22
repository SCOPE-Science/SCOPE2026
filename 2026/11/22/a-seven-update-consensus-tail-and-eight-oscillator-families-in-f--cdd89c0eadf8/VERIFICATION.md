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

The exact domain has 1,048,576 configurations, each encoded by a 20-bit integer. `folkman_census.cpp` checks the complete functional graph using a successor table, assigning each state's first-entry time and recurrent period. `verify_folkman_numpy.py` independently computes direct repeated iterates and tests the first occurrence of the equality \(F^{t+2}(x)=F^t(x)\). Their joint time/period census agrees in all twelve nonzero cells; both reach a sharp maximum time seven. The independent checker confirms that every maximal-delay trajectory reaches consensus, split 480/480 between the two uniform states.

`folkman_symmetry.cpp` reconstructs the full graph automorphism generators from the doubled \(K_5\) structure and enumerates group action on recurrent states, with temporal reversal added only for two-cycles. Its 44 fixed-state and eight temporal-orbit spatial classes sum to the respective complete populations. The source code and output counts are embedded with the result.

These exhaustive finite computations prove the stated invariant for the specified graph, not for all semisymmetric graphs. The full 1967 source text was not accessible; originality remains subject to historical priority. Independently authored external audit is not performed.
