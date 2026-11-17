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

# Verification of the conditional barycentric law

Run `python check.py` with NumPy and SciPy installed. The standalone checker constructs two-dimensional Gaussian random simplices directly and extracts their null vectors with a Cartesian cross product, checks the unequal-scale density by quadrature, and tests the distinguished-vertex critical law, Gaussian-mixture fluctuation and bulk inverse-participation ratio against independent random samples. The numerical diagnostics are finite and do not establish the full asymptotic claims; the proof uses exact Gaussian invariance, a coordinate Jacobian, the strong law and the central limit theorem.

The observed diagnostic values were: density integral 1.0, absorption frequency 0.24889375 versus 0.25, Cartesian/half-normal Kolmogorov distance 0.00228512, critical-window distance 0.00162963, fluctuation mixture distance 0.01125926, critical majority frequency 0.336259 versus theoretical 0.338334, and bulk squared-weight coefficient 1.569972 versus \(\pi/2\). All asserted numerical tolerances passed.

Independent mathematical audit: not performed. Historical priority: provisional; potentially relevant source texts remain inaccessible.
