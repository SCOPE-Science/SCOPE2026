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

Run `python3 pauli4_checker.py` with the Python 3 standard library. It checks exact arithmetic in the quadratic Eisenstein field for three non-phase-equivalent four-tap sequences with identical complete autocorrelation, then computes the two-branch reconstruction for all admissible integer magnitude quadruples up to five and deterministic additional real-valued instances. All autocorrelation components and ordered coefficient magnitudes are compared. The executable is supplementary: universal inequalities, boundary cases and the all-parameter three-point fiber cap follow from the written circle and cubic proof, not finite tests.

## Boundaries

The exact triple example has autocorrelation `(65/4, 0, 0, 2)` for nonnegative lags zero through three. The proof separately treats the second autocorrelation equal to or different from zero, and distinguishes true Pauli partners from conjugate-reversal representatives. No independent audit has been performed.
