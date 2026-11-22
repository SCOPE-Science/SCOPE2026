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

The displayed formula for steady oxygen follows by solving the constant-coefficient scalar differential equation. The sign reduction is the positive-denominator factorization involving the quadratic \(Q(z)\); its discriminant and root signs establish the full global theorem, not a numerical search. The critical square-root constant follows from the exact two-root formula and the concentration-gap exponent from integrating the factored derivative.

Reproducibility: with Python 3 and only the standard library, execute `python3 verify.py` in a directory containing this file and `verify.py`. The test suite asserts the analytic derivative equivalence for varied exponents and strengths, subcritical and supercritical derivative signs, the critical stationary tangent, the exact worked three-crossing example, and asymptotic turning-rate separation. Expected output: `CHECKS_PASSED 21781`.

The tests are finite floating-point spot checks and cannot establish the infinite theorem by themselves. Physical validity is restricted to strictly positive predicted oxygen. Uncalibrated Hill-response parameters, a fixed upper reservoir, and steady rather than transient transport are material assumptions.
