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

## Executed checks
The standalone `verify.py` was run with SymPy. Exact symbolic assertions matched the input map, both symmetric-coordinate updates, both variance formulas, the derivative of two-step variance with respect to the triple product, and the algebraic optimizer and sharp coefficient. Additionally, 285 rational simplex states passed exact inequality comparisons (with the radical coefficient compared symbolically).

## Analytic limits
The arbitrary-state inequality and uniqueness of its equality cases rely on Schur's inequality, the fixed-pair-sum boundary characterization, and one-variable derivative sign arguments given in `RESULT.md`. The rational-grid samples are not exhaustive. No separate independent audit or formal proof-assistant certification was undertaken.
