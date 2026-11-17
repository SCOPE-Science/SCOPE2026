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

The proof establishes a local Euclidean midpoint-depth expansion uniform in the boundary parameter; localization to nearby endpoint pairs and dominated \(L^1\) convergence prove the sharp coefficient and conditional total-variation limit. A continuous-mapping argument yields only weak convergence for the scaled exact depth. Cauchy--Schwarz, total turning angle and a degenerating ellipse family give sharp optimizers and the complete fixed-perimeter range.

The standalone `verify_midpoint.py` was executed against the files in this package. It independently computes ellipse curvature integrals, compares the circle asymptotics to its exact elementary expression, samples actual ellipse boundary chords and compares their nearest-boundary midpoint depths to predicted probabilities and conditional-gap moments. It completed with `MIDPOINT_BOUNDARY_CHECKS_OK`.

Numerical sampling has finite uncertainty; a fine sampled boundary approximates exact Euclidean boundary distance. These diagnostics are not an independent proof, and independent mathematical audit is not yet performed. Historical priority is provisional because two relevant older complete articles were inaccessible.
