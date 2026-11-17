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
# Reproducibility and verification

The full mathematical proof is in `RESULT.md`. Run `python verify_perimeter.py` with Python 3, NumPy, and SciPy. The standalone checker computes radially inscribed polygon perimeters, the limiting Lamé-curve perimeter via a separate Cartesian integral, and the curvature-integral coefficient by differentiating the polar parametrization. It checks the circle identity, three phase coefficients for the singular exponent, the critical logarithmic limit, and two exponents in the integrable regime. The execution passed 44 finite checks.

Numerical convergence at a finite number of values is evidence of consistency, **not** a proof of the full continuum of exponents or infinite-sample limits. The latter are established by the local normal-form expansion, chord-defect identity, tail estimates, and curvature-integration argument in `RESULT.md`. Lattice coefficient sums are specified by an infinite absolutely convergent series for each fixed exponent strictly below the critical one; finite truncation is only a numerical approximation. Historical-priority review remains provisional.
