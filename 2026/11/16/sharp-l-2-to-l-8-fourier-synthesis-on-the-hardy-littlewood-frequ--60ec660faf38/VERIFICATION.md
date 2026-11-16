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

## Reproduction

Run `python artifacts/verify.py` from the extracted package with SymPy available. The verifier exactly reconstructs the fourth convolution, proves the dyadic rational localization with 253 cells and maximum depth six, proves both negative diagonal Hessian numerators and strictly positive determinant on the localization square with exact rational coefficients, and uses high precision root solving only to print approximate coordinates. The exact global proof is independent of finite numerical testing.

## Limits

This proof covers only the complex trigonometric triple with frequencies 0, 1 and 3 on the normalized continuous torus at exponent eight. The provenance of the motivating published additive-energy source is December 17, 2021; this does not imply that the motivating paper proved the exact claimed constant. Independent historical priority and formal verification were not performed.
