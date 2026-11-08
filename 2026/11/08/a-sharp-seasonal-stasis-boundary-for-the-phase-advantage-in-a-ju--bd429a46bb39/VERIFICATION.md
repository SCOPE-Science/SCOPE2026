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

# Verification of the two-season phase comparison

Recreate the two-season products from the matrix definition in RESULT.md and verify the two polynomial identities for the trace and determinant differences. Evaluate their characteristic-polynomial difference at the Perron root of the aligned arrangement. Its sign converts to the eigenvalue-ordering sign because the opposite product's smaller eigenvalue lies strictly below the aligned product's Perron root. Strict monotonicity of the decreasing threshold \(K(F)\) and increasing Perron root then yields the exact unique switch.

Run `python verify_phase.py` with Python 3 standard library. The reproducible verifier checks 4,000 rational parameter profiles for the polynomial identities, uses 70-digit decimal arithmetic to corroborate the Perron-order sign, verifies the rational example's exact entries and boundary determinants, and checks one later positive-fertility parameter for the returned opposite-phase advantage. The script finishes with two PASS lines if the tests succeed.

The verifier is finite corroboration, not a proof of the all-parameter theorem. No stochastic survival, general multiseason order, nonlinear density effects or empirical demographic calibration is certified. Historical scientific priority remains subject to independent assessment.
