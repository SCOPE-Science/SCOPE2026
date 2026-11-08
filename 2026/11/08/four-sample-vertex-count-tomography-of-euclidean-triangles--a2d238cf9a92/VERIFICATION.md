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

The analytical proof treats all nondegenerate triangles; the code supplies exact finite-case and independent numerical checks. Run `python verify.py` with a standard Python 3 installation. Expected successful output: `VERIFY_OK exact_occupancy_shapes=5 continuous_hull_trials=180000 nonidentifiability_pair=1`.

The exact occupancy portion enumerates all 81 four-point side-label assignments for five exact rational triangular side profiles. The independent geometry portion samples actual Euclidean boundary coordinates and determines the convex-hull vertex count with a monotone-chain algorithm, comparing frequencies to all three theoretical probabilities. Floating-point collinearity is resolved by a fixed cross-product tolerance in the numeric checker; the proof is exact and does not rely on this tolerance.

The inverse cubic, discriminant feasibility and endpoint inequalities are proven symbolically in `RESULT.md`. Simulation cannot certify a universal inequality or rule out unindexed prior results. No independent audit or external validation has been performed.
