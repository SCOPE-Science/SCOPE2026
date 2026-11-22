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

The attached `verify.py` uses exact-rational SymPy calculations for the local identities and five-vertex witness, including the characteristic polynomial of the projected matrix. Its separate symmetric-eigensolver checks 200 source/time examples, with 9 graph specifications, five positive times each, and eligible starting vertices. The witness has the exact inequality \(61-a_1-a_2=215528/138043>0\), which, together with positive semidefiniteness, proves eventual negativity without numerical eigenvalue estimation.

The analytical proof, not finite testing, establishes all graph-size quantifiers, the positivity of reduced Jacobi semigroup coordinates, the exact asymptotic sign, and the at-most-one positive zero of each neighboring coordinate. A supplementary numerical root is used only to illustrate the crossing. Python 3 with `sympy`, `numpy`, and `scipy` is required; run `python3 verify.py` from the extracted package directory.

No finite-precision rounding guarantee or independent mathematical review is asserted.
