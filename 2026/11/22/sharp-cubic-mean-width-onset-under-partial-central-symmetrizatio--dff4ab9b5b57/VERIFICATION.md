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

The exact analytic argument is in `RESULT.md`. To reproduce computational checks, execute `python verify.py` using Python 3; NumPy is optional but required for the separate five-dimensional random-matrix experiment.

The checker evaluated the direct spectral support maximum (not the postulated closed expression) by composite Simpson quadrature at \(t=0,0.2,0.49,0.5,0.501,0.55,0.7,0.85,1\), agreeing with the formula within \(2\times10^{-8}\). With NumPy, an independent 160,000-direction simulation on the unit sphere of traceless symmetric matrices passed comparisons at seven values, within a \(0.0025\) Monte Carlo tolerance. The threshold was also verified directly from the exact minimal eigenvalue \((1-2t)/3\) of the reflected projector's PSD representative.

The numerical tests are finite and are not certification for every parameter. Exact validity across the continuum rests on the stated matrix-geometry, angular Jacobian and elementary-integration proof. No external independent audit has been performed.
