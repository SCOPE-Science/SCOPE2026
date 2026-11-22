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

The complete mathematical argument is given in `RESULT.md`. To replay the standalone numerical comparisons, install `mpmath` and run `python verify_spherical_slab.py` in this directory. The checker was run successfully from the packaged path and reported **198 passing deterministic numerical checks**. It compares an independent sampled convex hull projection perimeter with the support integral, checks the beta atom against angular integration, varies dimension and slab aspect ratio, checks endpoint coefficients and positive monotonicity on finite grids.

The finite grids and sampled hull approximations are **not exhaustive proofs**; the continuum and asymptotic conclusions follow only from the stated analytic support calculation and local dominated-integral arguments. The numerical convergence rates near logarithmic and fractional-power endpoints are not proposed as certified uniform error bounds. The 2012 archival source date is independently supported by the arXiv public posting metadata for 1203.2464; it dates supporting literature, not this theorem.

An independent mathematical audit has not been performed.
