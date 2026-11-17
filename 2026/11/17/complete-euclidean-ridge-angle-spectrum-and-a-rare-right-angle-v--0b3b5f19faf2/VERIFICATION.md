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

# Reproducibility

Run `python verify_ridges.py` with Python 3, NumPy and SciPy installed. Its direct incidence checks cover integer dimensions `q=2..6` and its exact integer identities cover `q=2..300`. Its convex-hull facet comparison is numerical but independent of the facet-label enumeration; no numerical finite test certifies all dimensions.

Expected successful final line: `K2Q_RIDGE_SPECTRUM_PASS q_hull=2..6 q_algebra=2..300`. The mathematical proof of the infinite statements is in `RESULT.md`, including the treatment of concentration and rare-angle variance.
