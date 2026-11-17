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

# Verification checks

Run `python check_circumcenter_astroid.py`; dependencies are listed in `requirements.txt`.

The executable checker derives exact rational mixed moments independently of the sampling, compares them to large endpoint-angle samples, reconstructs triangle circumcenters from Euclidean perpendicular-bisector equations for three distinct ellipses, checks the astroid constraint and independent-angle representation, verifies local Taylor errors, and performs a direct rare-event Monte Carlo check of the asymptotic cusp coefficient. Its actual completed run printed `INDEPENDENT_CIRCUMCENTER_RECONSTRUCTION_OK`, `MOMENT_IDENTITIES_OK`, `INDEPENDENT_ARCSINE_PARAMETERIZATION_OK`, `CUSP_QUADRATIC_AND_CUBIC_EXPANSIONS_OK`, `CUSP_TAIL_CHECKS_OK`, and `ELLIPSE_CIRCUMCENTER_ASTROID_CHECKS_OK`.

The proof—not the computation—establishes the global density, support, all mixed moments, cusp constant and conditional total-variation limit. The source comparison is bounded and cannot exclude every earlier formulation. Independent validation has not been performed.
