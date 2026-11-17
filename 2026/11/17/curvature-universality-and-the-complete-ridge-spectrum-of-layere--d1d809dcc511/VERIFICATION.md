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

Run `python verify_layered_curvature.py` with Python 3, NumPy and SciPy. The checked script reconstructs vertices, normals, candidate ridge intersections, Euclidean projection volumes and exterior angles independently of the beta-integral proof. Observed result: `LAYERED_CURVATURE_PASS numerical_profiles=11 brute_ridges=466 profile_identities=262125`. Finite experiments do not establish the general theorem. The proof of generality is in `RESULT.md`; no independent audit has been performed.
