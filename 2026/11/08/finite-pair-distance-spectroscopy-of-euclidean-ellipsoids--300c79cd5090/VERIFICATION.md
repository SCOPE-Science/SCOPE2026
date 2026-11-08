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

# Analytical and computational verification

The separately implemented `check_ellipsoid.py` uses exact SymPy arithmetic to evaluate the unit-ball radial calibration \(c_{d,k}\), generate the spherical quadratic-form coefficients, and reconstruct the squared-semiaxis polynomial for distinct positive spectra in dimensions 2 through 5. It also checks the elementary moments and sharp two-moment inequalities and draws 90,000 independent uniform point pairs each in dimensions 2, 3 and 5. On the accompanying version the program outputs `ELLIPSOID_DISTANCE_INVERSE_OK exact_dimensions=2,3,4,5 calibration=8 simulation_dimensions=2,3,5 samples_each=90000`.

These finite tests do not prove the theorem for unbounded dimension; that conclusion rests on the exact Dirichlet generating identity, beta calibration, and Jacobian rank arguments in RESULT.md. The symbolic checks do not independently certify the novelty or any noisy-sample stability property.
