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

# Verification report

The embedded `verify.py` was executed with the embedded dependency specification (`requirements.txt`) in a Python environment providing NumPy and SymPy.

It passed symbolic differentiation and exact risk-factor identities, verified polynomial-moment exactness and the optimized two-site construction for every integer budget 2 through 19, and passed 11,999 random feasible-stencil spot checks at budgets 3, 4, 5, 6, 7, 8, 11, and 15. These tests do **not** certify a universal theorem. Universality follows from the signed coefficient decomposition, Holder and Cauchy--Schwarz, scalar optimization, and complete equality conditions in RESULT.md.

Reproduction command from the extracted package directory: `python verify.py`.

Scientific limits: independent oracle noise only; deterministic fixed-design linear estimators only; unrestricted all-nonlinear-estimator minimaxity not proved. Independent audit has not been performed.
