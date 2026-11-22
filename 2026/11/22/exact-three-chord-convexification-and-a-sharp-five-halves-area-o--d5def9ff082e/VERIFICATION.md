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

# Reproducibility and scientific limits

The mathematical proof and all quantified assumptions appear in `RESULT.md`. The independent status above is intentionally unperformed. The executable diagnostic `check_orthoptic_hull.py` uses 65-digit mpmath arithmetic for four positive near-threshold amplitudes and tests the predicted leading coefficient; where SciPy and NumPy are installed it also compares a 60,000-point numerical convex hull to the exact integral. These computations are nonexhaustive and do not substitute for the global supporting-line proof. The checked output is `THREEFOLD_ORTHOPTIC_HULL_AREA_CHECKS_OK`.

The exact first-public-date supporting source is the 2013-01-29 arXiv submission `1301.6991`; later specialized same-object research is acknowledged in the literature comparison. A failed search is not a mathematical proof of novelty. This result has not undergone an independent mathematical audit.
