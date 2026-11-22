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

# Verification

The main proof is fully analytic and uses explicit gnomonic geometry, uniformly bounded boundary expansions and spherical polar area. To rerun numerical sanity checks from the included independent script, install a Python 3 environment with NumPy and SciPy, then execute `python3 verify_spherical_layer.py` in the directory containing this file. The actual result was:

`PASS: 40 area/coefficient checks; 80 finite conditional CDF tests; 376 marked-law Monte Carlo and second-limit checks`

The checker uses independent exact-area and polar-integral calculations, conditional radial quadrature, fixed-seed Monte Carlo area sampling of the layer, and large-side threshold tests. This does not prove the infinite asymptotic claims; their proof is in the result's steps 1–5. No external certification is claimed. First take \(\varepsilon\downarrow0\) at fixed \(n\), then take \(n\to\infty\). No simultaneous limit, noise-stability theorem or general nonregular-polygon extension is asserted.
