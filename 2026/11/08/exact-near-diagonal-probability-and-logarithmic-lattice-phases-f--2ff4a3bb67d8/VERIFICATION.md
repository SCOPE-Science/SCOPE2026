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

# Verification checks and limitations

The accompanying standalone `verify.py` uses Python's `fractions.Fraction` and `math` libraries only. Execute `python verify.py` in the directory containing this report and the script. The program successfully completed **1,392 checks** in a fresh execution from these packaged paths.

The code independently evaluates the conditional equal-cell triangular distribution and the geometric tail; compares it with the finite closed form for multiple integer bases, rational probabilities and cell scales; tests the reflected birth-death stationarity equations; and tests the critical linear-log coefficient, the bounded-density coefficient, the joining of lattice-phase endpoints, and the nonconstant phase value. Exact rational comparisons are used for finite identities; floating-point calculations are used only for asymptotic and phase diagnostics.

The infinite invariant-mixture summation, limit coefficients, lack of a normalized limit, and completeness of subsequential phases are proved in `RESULT.md`, not by finite program execution. Publication-priority comparisons are bounded by accessible literature.
