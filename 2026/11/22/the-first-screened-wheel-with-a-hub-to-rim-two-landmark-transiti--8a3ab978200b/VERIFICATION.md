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

# Verification and reproduction

Run `python3 verify_screened_wheel.py` alongside `certificates.json` using Python 3.9 or later, without third-party packages. The script reconstructs grounded determinant coefficient arrays using exact integer fraction-free elimination and Newton interpolation; verifies every signed comparison polynomial against the supplied certificate; checks the seven-rim degree-ten sign pattern and a strict rational root enclosure; compares characteristic-log-derivative formulas to exact rational inverse traces; and exhaustively checks the two-landmark optimizer sets for rim counts three through seven over six positive rational screening strengths. It also checks the complete eight-rim zero-screening objective table independently.

The result of replay from the packaged science files was: `PASSED: 2760 exact integer/rational assertions`.

Finite tests are corroborative. The all-wheel-size small-screening statement follows from the explicit positive Green-function bound in the proof; the high-screening statement follows from a controlled fixed-size matrix-inverse expansion. The exact algebraic root is defined by a positive-root uniqueness argument, not a floating-point root finder. This reproduction does not establish publication priority or independent validation.
