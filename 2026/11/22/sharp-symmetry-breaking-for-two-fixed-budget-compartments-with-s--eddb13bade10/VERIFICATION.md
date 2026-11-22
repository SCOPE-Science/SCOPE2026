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

# Verification performed

`verify_haldane.py` was executed from its exact submitted content in a Python 3 environment with SymPy. The run asserted the exact derivative identity, endpoint polynomial, discriminant and first/second derivatives; it also checked 600 exact rational model evaluations and 9-by-11-by-101 deterministic parameter/imbalance comparisons. Its output reports 10,667 completed assertions and the example's numerical values.

The universal theorem is instead justified by the analytical proof in `RESULT.md`, including all positive parameters, the optimizer at criticality, the boundary at zero substrate, the unique positive quadratic root, and both asymptotic limits. The finite grid is not an exhaustive parameter search and does not establish originality or independent validation.

Reproduction command: `python verify_haldane.py` (requires SymPy).
