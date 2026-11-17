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

## Actual verification
The formula follows from the explicit determinant computation and positive-vertical lift. Running `python verify.py` checks the determinant across independent random configurations, Delaunay interior-edge stability for sizes 4, 7 and 12 under four aspect ratios, and numerical integration of the arcsine marginal. The tests support, but cannot replace, the proof. Independent mathematical audit has not been performed; historical priority is provisional.
