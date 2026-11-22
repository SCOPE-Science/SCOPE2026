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

The theorem is proved in `RESULT.md`; no external verifier or independent audit is asserted. Reproduce the ancillary comparisons by running `python verify.py` with Python 3, NumPy and SciPy installed. The script constructs the images of all twenty-seven product vertices in four-dimensional translation space and computes their convex hull independently of the symbolic mixed-area identity.

The check covers 250 seeded random positive scale triples and arbitrary relative angles, and separately checks four positive scale triples at both predicted sharp configurations, for eight endpoint cases. It checks no continuum or infinite-dimensional certification: the analytic proof handles the untested parameters.

The literature comparison distinguishes maximum *overlap area* from the four-dimensional *feasibility-region volume*, and the known repeated-triangle Rogers–Shephard upper endpoint from the new weighted orientation-minimum classification. Historical literature not indexed by the searched resources remains a risk.
