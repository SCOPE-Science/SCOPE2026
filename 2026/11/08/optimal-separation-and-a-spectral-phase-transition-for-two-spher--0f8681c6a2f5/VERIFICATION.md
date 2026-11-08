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

# Reproducible checks

Run `python3 check_two_caps.py` with a standard Python 3 installation. The checker uses exact rational cap-moment integration, verifies each five-dimensional Gram sector in 33 disjoint rational test configurations, checks 19,829 other feasible angular placements on a numerical grid, and tests the exact symbolic transition sign across sampled radii. Successful execution emits `ALL_QUADRATIC_SPHERICAL_TWO_CAP_CHECKS_OK`.

The proof in `RESULT.md` is the evidence for the global continuum of radii and orientations; the numerical grid is not treated as exhaustive. The external literature comparison and the analytic coefficient normalization require ordinary mathematical scrutiny. Independent audit was not performed.
