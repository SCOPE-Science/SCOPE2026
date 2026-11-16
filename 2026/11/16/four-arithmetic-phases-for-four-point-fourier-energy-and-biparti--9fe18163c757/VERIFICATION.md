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

The exact-integer checker `checker.py` enumerates all four-subsets for cyclic orders 8 through 33, checks both maximal-energy values and full equality classes, and independently enumerates 60 directed-edge graph examples to validate the closed energy formula. To replay, run `python3 checker.py` alongside this file. The program prints its exact test counts and raises an assertion on the first discrepancy.

The universal step uses a separate analytic argument: subgroup stabilizers divide four, nonzero difference multiplicities pair as positive integers no larger than three, and a difference of multiplicity three must correspond to a four-vertex path or a three-cycle plus an isolated vertex. Character orthogonality then transfers the sharp energy result to the graph collision dimension. Finite cases are tests, not a proof of all integer orders.

No independent mathematical audit has been performed. Bibliographic priority beyond the inspected publications and indexed research records remains open.
