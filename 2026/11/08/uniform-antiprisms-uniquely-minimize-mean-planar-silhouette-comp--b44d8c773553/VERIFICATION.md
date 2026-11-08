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

# Verification record

Run `python verify_antiprism.py` with NumPy, SciPy and SymPy installed. The checker uses the polygonal model defined in the result. It performs three symbolic identities, exact formula/optimal-height agreement for seven polygon orders, independent planar convex-hull reconstruction of \(2{,}700\) silhouette vertex counts, and Monte Carlo expected side-count checks on \(675{,}000\) independent isotropic directions. It printed `ANTIPRISM_SILHOUETTE_OK symbolic=3 tested_n=7 sightline_samples=675000 hull_reconstructions=2700`.

The direct hull calculations use projected vertex coordinates, whereas the analytic expression and the faster independent edge-normal counts use face normals; they therefore exercise distinct geometric implementations. The floating-point samples are diagnostic, not a proof of global uniqueness. The analytical derivative and edge-length identities prove the infinite family theorem. No independent audit or formal machine certification is claimed.
