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

# Verification notes

The stationary second- and fourth-moment formulas were obtained by applying the Markov generator to all monomials through total degree four and retaining the even-sign sector. The accompanying `checks/verify.py` regenerates the full 25-state and reduced 15-state generator matrices from the model equations; it verifies the symbolic moment formulas, the exact rational witness, and 160 independent numerical evaluations of the full stationary linear system. All model parameters in the theorem must be strictly positive. The sharp global sign proof comes from the positivity of every denominator factor and elementary analysis of the sign polynomial; floating-point tests are not exhaustive proof. External expert validation has not been performed.
