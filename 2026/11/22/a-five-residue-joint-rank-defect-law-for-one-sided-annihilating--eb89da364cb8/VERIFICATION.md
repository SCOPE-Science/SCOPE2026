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

The attached `verify_one_sided_theta.py` is a dependency-free Python 3 program. Direct prime-field matrix enumeration checks all ordered idempotent pairs in five tested small configurations and their complete two-rank and reverse-product rank cells. Integer arithmetic compares every rank cell for the projection–square-zero correspondence across dimensions one through 34 and field-size parameters two, three, four, and five; all rectangular matrix rank counts sum to their full populations. Integer maximization verifies the quadratic saddle exponent for dimensions one through 100. The recorded tests also show numerical convergence of the five-residue total and the fifteen-residue two-sided rarity prefactors. The script terminates with `ONE_SIDED_PROJECTION_THETA_CHECKS_PASSED`; its complete output is included in `verification_output.txt`.

The universal theorems are justified by the explicitly shown block decompositions, Gaussian cancellations, completion of squares, Euler-product bounds and dominated convergence, not by the finite tests. Arithmetic at field-size parameters four and five validates polynomial counting identities only; exhaustive matrix multiplication was performed over prime fields two and three. No standalone infinite proof certificate and no independent mathematical validation is claimed.
