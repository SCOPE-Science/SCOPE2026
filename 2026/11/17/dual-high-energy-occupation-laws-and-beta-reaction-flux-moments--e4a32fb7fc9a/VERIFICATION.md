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

The symbolic checker `check_dual_occupation.py` differentiates the conserved energy and the logarithmic and linear test observables, and evaluates the exact integer beta coefficients. Quadrature witnesses at finitely many energies check normalization and finite-energy behavior without claiming numerical proof of an infinite limit.

The analytic verification is the four integrable distortion estimates, which handle all inverse-branch endpoints before passing to uniform measures. The original-time period follows from those estimates and coincides with known leading asymptotics. All coupled limits and moment limits refer to actual positive periodic orbits, not simulated transients.

Independent audit: not performed. Publication-priority coverage beyond inspected texts remains an explicit limitation.
