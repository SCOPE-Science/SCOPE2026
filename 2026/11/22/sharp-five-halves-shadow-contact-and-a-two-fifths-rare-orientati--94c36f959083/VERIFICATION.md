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

# Reproducibility and limits

Run `python3 check.py` in the directory containing this report. Its deterministic tests compare the closed area formula against a separate longitude-integrated and latitude-quadrature representation, assess monotonicity and endpoint values, and test the noninteger contact coefficient at several clipping heights. The checks are finite numerical diagnostics, not a proof of strict inequalities for all directions or of the asymptotic error bounds. The displayed analytic argument is the source of the theorem.

The references are publicly accessible; independent scientific validation has not been carried out. The local formulas and their normalization apply to a **solid** unit ball intersected with an oriented half-space in three dimensions. The orthographic shadow area is not the area of the spherical cap surface and should not be confused with a perspective or luminous irradiance integral.
