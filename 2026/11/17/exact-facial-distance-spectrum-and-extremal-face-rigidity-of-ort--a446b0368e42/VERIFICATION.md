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

# Reproducible checks

The standalone program `verify_facial_distance.py` requires Python 3, NumPy and SciPy. Running `python verify_facial_distance.py` completed successfully and reported 96 finite, independently optimized face-versus-complement distances for the seven listed parameter pairs. For every pair it also compared the minimum over all exclusive and mixed rank types against the proposed closed expression and counted equality types.

The numerical optimizer uses the actual cube-corner coordinates and convex-combination variables, independently of the separating-normal proof. Its tolerance is \(2\times10^{-6}\). The code does not enumerate all dimensions or certify an unrestricted theorem; the proof in `RESULT.md` establishes the arbitrary-parameter result. No external or independent audit has been performed.
