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

# Reproducibility verification

The companion `verify.py` takes no input files or external data. Run `python verify.py` with Python 3, numpy, scipy, sympy available. It reconstructs the halfspace representation and its Euclidean normals. It enumerates normalized normal dot-product classes and confirms predicted multiplicities for all integer column counts from 2 to 32. For 2 through 8 it independently solves one slack-feasibility linear program per facet pair and checks the exact nonridge list; for column counts 2 and 3 it enumerates vertices with exact-rational matrices and confirms ridge codimensions by affine rank.

Expected marker: `TWO_ROW_PS_RIDGE_ANGLE_PASS angle_counts_m=2..32 strict_LP_m=2..8 exact_vertices_m=2,3`. The proof in `RESULT.md`, rather than these finite tests, covers all column counts. No independent mathematical audit or external proof certification has been performed. General affine changes can alter angles.
