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

# Mathematical verification

The complete argument is in `RESULT.md`. Independently, `verify_rectangular.py` builds each faulted graph's edges and degree constraints, constructs the full simplicial face family including the empty face, tests the proposed cone apex or distinct private-star witnesses, and computes the augmented simplicial chain ranks over \(\mathbb F_2\). Running `python3 verify_rectangular.py` produced `PASS: exhaustive fault patterns n=2,3; 15 rectangle types n=4`.

The verified finite collections consist of all 14 nonempty proper fault sets on \(K_{2,2}\), all 510 on \(K_{3,3}\), and one rectangle of each 15 proper size pairs on \(K_{4,4}\). These checks are finite corroboration only. The all-order integral homotopy statement is derived from the explicit forbidden-star and repeated-suspension argument, without relying on a finite-cases-to-infinity inference. An independently conducted audit has not been performed.
