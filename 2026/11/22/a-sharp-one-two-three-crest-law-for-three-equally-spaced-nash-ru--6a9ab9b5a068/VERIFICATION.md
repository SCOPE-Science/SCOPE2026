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

# Verification notes

The complete analytic proof is in `RESULT.md`; its key steps are (i) piecewise conversion of the derivative to three explicit concave quadratics, (ii) unique zero of \(F(\delta)\) on \((1,2)\), and (iii) the uniform inequality \(2M<e^{-1}\) ensuring a positive derivative shortly after the last new impulse. These establish the root counts for **all** real positive gaps; the finite checker does not establish the universal quantifier.

Run `python CHECKER.py` using Python 3 and the standard library. The program prints `PASS: 2297 assertions; critical gap = 1.537805488887; peak counts: 1 at d=1, 2 at d=1.8, 3 at d=2.2`. Its rational arithmetic tests the polynomial coefficients and its root-location tests compare calculated peak counts against the proof on a finite grid; it additionally checks the negative-slope inequality. Boundary cases \(\delta=\delta_0\) and \(\delta=2\) are resolved symbolically in the proof, not by floating-point equality.

The normalized kernel is proportional to the three-reservoir instantaneous unit hydrograph. Empirical input noise, finite-duration rainfall and model mismatch are outside scope. No external proof assistant or independent scientific assessment is claimed.
