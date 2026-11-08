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

Use `python3 verify_projection.py` with NumPy and SciPy installed. The attached program checks independent spherical-probability quadratures at five thresholds, 500000 Haar-sampled octahedral plane normals, explicit comparison of projected coordinate norms and leverage scores on 1920 coordinates, and four fixed-codimension Weibull benchmarks with 4000 independent normal frames per codimension. A successful execution ends in `CHECKS_PASS`.

The mathematical proof does not rely on simulation. The point-process theorem is an infinite-dimensional asymptotic; a finite test is neither exhaustive nor a scientific independence certificate. The moment result relies on Wishart spectral concentration and uniform chi-square minimum tail moments, as described in the proof. No independent audit was performed.
