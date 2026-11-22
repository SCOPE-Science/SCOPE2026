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

The proof is self-contained in `RESULT.md`. The accompanying `verification/check.py` uses Python standard-library exact `fractions.Fraction` in a finite grid of reduced rational phases with denominators two through twelve, including strict and boundary observation widths. The tests check the phase-reduction recurrence, eventual capture, rational exceptional-set lengths, and physical-time firing formulas. Additional high-precision irrational rotation tests exercise the first-hole-hitting and staircase formulas. Run with `python verification/check.py`; the observed successful completion reports `PASS rational parameter cases 2356 exact and high-precision checks 210492`.

The analytic proof, not finite computation, establishes arbitrary irrational rotations, exact periodic measures, and all width and time limits. The test script does not certify infinite-time dynamical behavior beyond the mathematical proof. The most substantive unproved external issue is exhaustive historical priority, especially an exact earlier theorem for a reset rotation on a deleted arc. No independent mathematical audit has been performed.
