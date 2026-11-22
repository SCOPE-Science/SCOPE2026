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

# Verification and reproducibility

An exact Riccati periodic perturbation derivation, with all rates positive, proves the coefficient and phase partition. The bounded periodic ratio is analytic near zero forcing because its zero-forcing linearized return multiplier is \(e^{-2sT}\) strictly between zero and one. The half-period time shift makes the exponent even in amplitude. The proof does not infer infinite-domain identities from finite numerical evidence.

Run the included standalone `verify_phase.py` from the same directory using Python 3 only. It independently constructs a Riccati-Fourier coefficient and solves the full two-by-two time-dependent fundamental matrix via independent fourth-order Runge–Kutta integration. It completed **202 passing assertions**, including the exact rational boundary example, phase maximization, multiple unequal-removal configurations and equal-removal aligned exact invariance. Numerical ODE tolerances provide corroboration, not a formal certificate.

The first public motivating source is dated 2023-12-13; this date is the online publication date, not manuscript receipt or journal issue date. The analytic assertion covers arbitrary fixed positive baseline rates and frequency with sufficiently small forcing. At degenerate quadratic-coefficient-zero phases other than the exactly commuting case, no growth-sign conclusion is made. Independent validation has not been performed.
