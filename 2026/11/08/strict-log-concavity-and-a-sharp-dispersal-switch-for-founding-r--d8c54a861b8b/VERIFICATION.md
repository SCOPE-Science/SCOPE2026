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

# Verification

Run `python verify.py` with the adjacent `hessian_certificate.json` file and SymPy. The exact arithmetic script verifies the four-state absorbing system, the rational first-pair success formula, all positive monomials in three Hessian numerators, their positive denominators, the signed endpoint derivative, and the ordering of the coefficient transition points. It separately generates the transition rates and solves \(25\) rational instances by Gaussian elimination, then compares with the symbolic probability formula.

The certificate contains the complete \(37+58+79=174\) integer coefficient table and checks monomial exponents as well as coefficients. The sign checks are exhaustive for the symbolic polynomials; the independent rational instances are additional diagnostics and do not substitute for the all-parameter polynomial argument. The ecological interpretation excludes permanence after two destination individuals are reached. Independent expert audit has not been performed.
