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

The geometry is verified analytically via the quotient metric, a Haar-surjective sum/difference map, disk–rectangle integration, a strict fixed-area overlap derivative, and a four-corner tail expansion.

The package file `pillowcase_geodesic_check.py` computes independent sampled quotient distances and compares its theoretical CDF for 36 thresholds against observed frequencies from 1,800,000 independent sample pairs. It checks square-vs-rectangle CDF domination for 15 area/aspect configurations, 300 radii each, and verifies fourth-order upper-tail coefficient numerically for three rectangles. Expected success line: `PILLOWCASE_GEODESIC_LAW_OK`.

Sampling, finite grids and approximate arithmetic do not constitute proof for every radius or aspect ratio. No independent mathematical audit or certification has been performed.
