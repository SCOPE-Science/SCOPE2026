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

The exact analytic chain is provided in `RESULT.md`: hemispherical bisector normals, their cosine surface density, Gaussian positive-part angular integration, the density change of variables, and the CDF with endpoint evaluation. Each step applies to the whole parameter range. In particular, the CDF has no unaccounted atom at either endpoint; the density integrates to one.

Run `python verify_voronoi.py` using Python 3 with NumPy available. The checker was executed from the final candidate artifact and returned:

`THREE_SITE_SPHERICAL_VORONOI_AREA_LAW_OK 500000 125000`

It verifies the CDF at the endpoints and at the exact quarter-sphere checkpoint, checks that numerical differentiation agrees with the density, integrates the predicted density against the zeroth, first and second moments, generates 500,000 independent direct spherical-site triples, and separately estimates the actual spherical-lune area from 125,000 uniform spherical observations for four frozen normal pairs. The checker has a fixed random seed; empirical checks use explicit tolerances and are finite-sample consistency evidence, not proofs of universal validity.

Independent review and exhaustive historical priority verification have not been performed. One potentially closely related 1971 spherical tessellation paper and another 1994 spherical mosaic paper could not be read in full. Their precise claims remain a documented limitation rather than an assertion of noncoverage.
