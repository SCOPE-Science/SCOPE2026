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

The analytic verification is the facet-normal Gram calculation, the six-type ridge census and the simplex Dirichlet integral in `RESULT.md`. The identity \(V_{N-2}=(2\pi)^{-1}\sum_R\phi_R\operatorname{Vol}_{N-2}(R)\) fixes the normalization. The script `check_geometry.py` independently enumerates vertices and actual affine face volumes for seven low-dimensional profiles, with each listed facet-pair count checked. Its finite sample is not offered as proof of the all-parameter formulas.

Reproduce with Python 3, NumPy and SciPy: install `requirements.txt`, then run `python check_geometry.py`. A successful run concludes with `SPLIT_STEINER_DIRECT_PASS`.

No third-party mathematical audit or formal certification is claimed. The all-parameter proof uses exact integration rather than reliance on numerical tolerances.
