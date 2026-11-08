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

The analytic proof in RESULT.md is the evidence for the infinite families of step counts and phases. It establishes the exact two-node and three-node quadrature representations directly from the Shu–Osher stages; applies a finite geometric-series identity; uses a rank-one spanning criterion for all singularities; and verifies the strict phase crossover algebraically. All domains and exceptional phases are specified there.

The attached standard-library check.py separately evaluates both published integrating-factor Runge–Kutta stage recurrences. Executing `python check.py` returned `CHECK_OK 2940 direct-stage/eigenvalue/phase comparison checks`. It tests 20 iteration counts and 21 ordinary/near-resonant step phases for both integrators, plus additional exact-resonance and spectral-order checks. The resonance comparisons use floating-point arithmetic in the script; their *exact* correctness is established by the analytic projector sums in RESULT.md, not inferred from a floating-point tolerance.

Symbolic special case: at an odd half-turn step, Simpson's projector weights are one third along the initial axis and two thirds along the orthogonal axis, whereas the trapezoidal weights all lie on the initial axis. Both matrices remain positive semidefinite. The continuous integral has two equal eigenvalues because the total angle is an integer number of half-turns.

This verification does not test arbitrary matrices, rounding-error effects, nonconstant forcing, higher dimensions, or global literature priority. No independent mathematical audit has been performed.
