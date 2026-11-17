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

Run `python3 verify_cycle_angles.py` in a Python 3 environment without third-party packages. It independently enumerates the vertices of the standard root-cycle zonotope, its cyclic-interval facets, all pairwise facet intersections, their exact ranks, and normal Gram products, using rational arithmetic. It compares the observed face-indexed angle multiset with the stated composition formula and verifies the extremal levels and multiplicities for cycle orders four to seven.

Observed exact results: `CYCLE_RIDGE_PASS n=4 vertices=14 facets=12 ridges=24 levels=2`; `n=5 vertices=30 facets=20 ridges=60 levels=4`; `n=6 vertices=62 facets=30 ridges=120 levels=6`; `n=7 vertices=126 facets=42 ridges=210 levels=9`.

These finite tests corroborate, but do not establish, the all-dimensional statements. The logarithmic limiting law is proved analytically by a Riemann-sum limit for positive compositions and an elementary two-variable density integration. No independent mathematical audit or formal certification has been performed.
