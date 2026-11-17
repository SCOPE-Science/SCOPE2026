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

The analytic proof of the finite spherical-cap illumination profile appears in `RESULT.md`. The standalone `checker.py` reconstructs independently the geodesic hull as a sampled spherical polygon by gnomonic projection and direct solid-angle triangulation; it compares this geometric integration against the exact closed form and an independent derivative integral. It also checks the two sharp endpoint coefficients. Running `python checker.py` produced `PASS: 27 numerical comparisons; spherical polygons are independently projected and triangulated`.

These numerical tests use finite boundary sampling and do not prove the continuous assertion. The exact argument uses spherical triangle laws, Girard's theorem, a sector-area decomposition, an explicit derivative and integration of endpoint expansions. The novelty comparison is provisional because an additional recent paper's full text could not be consulted. No independent mathematical audit has been performed.
