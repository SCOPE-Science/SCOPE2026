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

# Analytical and reproducibility checks

The Euclidean chord-vector identity reduces the triangle property to a one-dimensional trigonometric threshold. The exact uniform-angle coefficient is obtained from the convergent arcsine-square power series. The speed-power density has an explicitly normalized Fourier expansion, and the quadratic pure-density term vanishes over the circular obtuse region. The mixed term is an exact sum of two elementary boundary-line integrals. Analytic dependence after partitioning the moving right-angle boundary, together with the axis-swap symmetry, upgrades the remainder to fourth order.

Run `python checker.py` from the same extracted directory with Python 3.11, NumPy and SciPy. It independently computes chord-vector dot products and uses Gaussian quadrature and an arclength-CDF grid to test several exponents and both anisotropy signs. A passing script is a finite consistency check, not an external or infinite mathematical certificate. Neither full global acuteness distributions nor fourth-order signs are certified.
