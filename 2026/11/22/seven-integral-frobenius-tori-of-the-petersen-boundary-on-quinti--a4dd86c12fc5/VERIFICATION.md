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

# Reproducibility and proof boundaries

Run `python verification/verify_petersen_tori.py`; dependency: Python 3.9+ and SymPy. The deterministic program uses explicit integer matrices and exact arithmetic, not sampling to establish the seven integral conjugacies. It checks all seven representative five-label conjugacy classes, each with a determinant-one-or-minus-one change of integral cycle basis; permutations in a conjugacy class are transported by the graph action.

It derives the Petersen graph (ten vertices, fifteen edges), checks that the fundamental cycle basis is an integral basis of the kernel of its integer incidence map, and checks the seven matrix equalities. It verifies sample finite rational torus cokernels by exact Smith forms at prime powers \(2,3,4,5,7,8,9,11,16,17,19\). These finite samples corroborate rather than replace the all-\(q\) integral torus identifications.

The boundary point-count proof includes every geometric component, node and half-edge orbit; its correction retains rational nodes with conjugate branches. The companion data table records cycle decompositions and the first-extension polynomials. The checker tests extension powers through six as additional consistency checks. No computation of an infinite collection of finite fields is claimed.

Historical priority is not settled by a negative search. No independent mathematical audit has been performed.
