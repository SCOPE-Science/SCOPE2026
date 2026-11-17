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

The accompanying `verify_inertia.py` is executable using Python 3, NumPy and SymPy. Run `python verify_inertia.py` from the directory containing the script. Its completed direct execution returned:

`VERIFY_OK equilateral_exact=1 collinear_exact=1 noncollinear_inertia_and_jacobian_cases=56 collinear_sign_cases=4`

Two exact symbolic determinant identities are checked, 56 finite nonsingular balanced polygon examples with heterogeneous active/inactive indices are checked against the complete Jacobian and finite-difference derivative, and four exact collinear threshold/sign cases are checked. The analytic rank-two quadratic-form proof is what verifies all finite sizes and continuous parameters; random examples do not themselves establish a theorem. Independent evaluation has not been performed. The result excludes the nonsmooth active-set transition at equality of growth and damping parameters and gives no nonlinear collinear stability classification.
