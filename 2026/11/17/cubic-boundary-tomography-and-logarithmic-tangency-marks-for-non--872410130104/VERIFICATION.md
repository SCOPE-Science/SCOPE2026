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

# Mathematical and computational verification

Exact formulas were checked from first principles: the chord endpoint-to-line Jacobian, intersection-position determinant, boundary logarithmic mass, the two mixed sectors, integrability of simultaneous tangent degeneracies, and label symmetry. The conditional sector densities were shown to exhaust probability mass, allowing Scheffé total-variation convergence.

`python CHECK.py` evaluates the finite-radius planar density via an FFT angular convolution, compares with the published uniform case at five radii and tracks anisotropic convergence at three directions. The deterministic cyclic-order identity yields crossing probability 1/3. Quadrature and finite tests corroborate but cannot establish infinite limits; the analytic proof in RESULT.md is the mathematical evidence.

External/independent audit is not performed. Historical originality is provisional due to inaccessible full text of David–Fix (1964).
