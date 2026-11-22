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

The analytic theorem uses exact triangular chord moments, two exact polynomial rhombus profiles, a strictly increasing quintic critical-point polynomial, and positive Bernstein coefficients for the cross-branch comparison.

Run `python3 verify.py` with the Python 3 standard library. This checks exact rational Bernstein coefficients and polynomial identities, root brackets, numerical endpoint values and 398 independent polygon-edge chord integrations. Run `python3 verify_symbolic.py` with SymPy 1.12 or later to reconstruct both angular profiles by exact symbolic chord integration and differentiate them. Both checkers must report PASS. The independent quadrature tests are finite checks, not an infinite-domain proof; that role is played by the displayed algebraic identities and positivity certificate.

The second-stage result is conditional on the first axis being optimal for the equilateral triangle. No assertion is made about the globally optimized choice of two unconstrained axes or any subsequent iterations.
