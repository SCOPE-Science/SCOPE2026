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

The exact proof and its limits are in `RESULT.md`. Run `python3 check.py` in a standard Python 3 installation. The script uses only integer arithmetic and `fractions.Fraction` and executed with 326 exact assertions passed. It reconstructs the positive coefficient lists for every required derivative polynomial at sizes four through twelve, checks the strict negative thirteen-vertex rational witness and the fourteen-vertex derivative, independently enumerates labelled attachment histories through seven vertices and cross-checks the leaf-count transition probabilities, and checks finite stochastic tails as diagnostics.

The all-parameter stochastic comparison and all-size negative derivative propagation are proved analytically in the result text. Exact finite computations are exhaustive only in the stated ranges. No claim of independent assessment or general-purpose formal verification is made.
