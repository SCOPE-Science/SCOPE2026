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

# Verification of the fixed-radius hyperbolic disk law

An executable standalone checker `check_hyperbolic_disk.py` uses tensor-product Gauss–Legendre integration over the two boundary radial deficits. The angular aperture is evaluated exactly by the cosine rule; it is **not** replaced by the leading square-root approximation. The numerical integrals compare against the predicted \(\varepsilon^{5/2}\) coefficient for Euclidean and curvature-minus-one disks with radii \(0.5,1,2.5\), at four decreasing thresholds. They also compute conditional means of the first three rescaled deficits and compare with the exact Dirichlet means \(2/7,2/7,1/7\). Three curvature-parameter sweeps independently check the strict order predicted analytically.

Run with `python check_hyperbolic_disk.py` using NumPy. Success is reported as `HYPERBOLIC_DISK_DIAMETER_RIGIDITY_OK`. The checker has no external data dependency or hidden package path. Numerical quadrature is supporting evidence only: the infinite asymptotic statement, the Dirichlet limit, and the strict curvature inverse are proved analytically. Independent mathematical and historical review has not been performed.
