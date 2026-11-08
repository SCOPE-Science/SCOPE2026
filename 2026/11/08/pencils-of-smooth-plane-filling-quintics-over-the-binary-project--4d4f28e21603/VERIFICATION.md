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

Both exact, independent smoothness tests were completed. `verify_pencils_groebner.py` uses the Jacobian ideal on three affine charts over \(\mathbb F_2\) and reconstructs the full projective classification and the attached `pencil_orbits.csv`. `verify_pencils_field.cpp` uses independently implemented finite-field evaluation for extensions through degree ten, with an arithmetic-genus justification for exhaustiveness. Each confirms \(139\) equation orbits, \(10\) smooth equation orbits with \(1{,}512\) equations, \(16{,}800\) valid pencils, and \(108\) pencil orbits with the same stabilizer and member-type strata.

No numerical extrapolation or unbounded computation is used. This verification covers the exact finite-domain statement, not geometric smoothness of all members over the algebraic closure of the pencil's parameter field; that stronger property is **not** asserted. The public metadata records self-review only; independent mathematical audit has not been performed.
