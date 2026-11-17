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

The exact projected squared-axis gap follows from the trace and determinant of the plane compression of \(\operatorname{diag}(B+\eta,B,B-\Delta)\). Its independent direct-eigenvector reconstruction is compared with the closed discriminant by the packaged program `check_projection.py`.

Execute `python check_projection.py` with the versions specified in `requirements.txt`. The program tests \(16{,}384\) uniform sphere normals for each of three parameter sets; compares Cassini region areas from numerical quadrature against complete elliptic integrals at five thresholds; and uses two-dimensional spherical-Jacobian quadrature to test shrinking-anisotropy ratios at \(t=0.4,1,2\). This run completed with the marker `ELLIPSOID_CASSINI_CROSSOVER_CHECKS_OK`.

These computations establish neither infinite-limit convergence nor historical priority. Analytical verification rests on the exact spectral identity, localization, dominated convergence, the square-map area formula, and elliptic-integral differentiation in RESULT.md. Independent mathematical audit has not been performed.
