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

Exact check: the local equation has partial derivatives `-z^(d-1)` and `-(d-1)*x*z^(d-2)` in characteristic `p`. The quotient is `R/(z^(d-2)*(x,z))`, where `R=k[[x,z]]/(h)` and `h(x,0)=-a_m*x^d`, hence `z` is a nonzerodivisor. The exact sequence and the length of `R/zR` establish `(d-1)^2` for all valid parameters. The included SymPy checker independently reproduced Groebner bases/standard-monomial counts for six cases with characteristics 2, 3, 5 and several nonmonomial polynomials. This is not independent mathematical validation.
