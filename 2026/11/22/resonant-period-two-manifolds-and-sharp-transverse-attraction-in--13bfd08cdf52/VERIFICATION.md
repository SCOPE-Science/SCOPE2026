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

# Verification and limits

The included `checks/check_period_two.py` ran successfully with Python and SymPy. It symbolically checks exact add/subtract reductions, loops over 160 deterministic rational parameter choices and exactly reconstructs the two-cycle whenever the nondegenerate discriminant is positive, and checks 43 exact two-step Jacobian characteristic polynomials in the resonance example. Result: PASS.

The complete real classification is proved algebraically in `RESULT.md`. The normal attracting interval is derived analytically from an exact quadratic Schur criterion, not from sampled multipliers. The complete text of one relevant published indexed finding was not accessible, and independent audit has not been performed.
