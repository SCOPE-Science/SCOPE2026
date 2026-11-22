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

# Reproducibility and limits

The included `checker.py` uses only the Python standard library. Execute `python3 checker.py` from a directory containing the file. The successful run reports 600 exact-rational comparisons of the closed formula with exhaustive face-block row norms for random positive integer inverse weights in dimensions three through seven, and checks two exact rational weighted projections on the five-coordinate permutahedron against all 120 vertices and all proper-subset inequalities, attaining the finite ratio \(303/103\).

Exact arithmetic avoids floating-point uncertainty in these finite tests. The analytic face decomposition, weighted KKT equations, active affine projector norms, and subset-exchange optimization in `RESULT.md` prove the general statement; finite tests alone cannot prove arbitrary dimensions or arbitrary positive real parameters.

No independent audit or external validation has been performed.
