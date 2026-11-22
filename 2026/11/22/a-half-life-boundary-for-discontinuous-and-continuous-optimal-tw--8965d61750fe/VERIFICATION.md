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

# Reproducibility and verification

The exact theorem is proved in `RESULT.md`. Reproduce finite rational checks using `python verify.py` with only the Python standard library. The checker compares the analytically specified optimum with all feasible breakpoints and the quadratic vertex in the clipped exposure factor, then samples additional rational dose allocations. It includes explicit equality and near-boundary tests, the one-half-life division, and the strict equal-versus-unequal comparison.

The checker returned `VERIFY_OK assertions=183183` on the reviewed source. These calculations verify exact rational test cases; they are not an exhaustive verification of real-valued parameters. For the infinite-parameter result, consult the branch partition, strict concavity and global comparisons in `RESULT.md`.

The model is an idealization: it does not infer clinical safety, treatment efficacy, independent historical originality or validation by any external party. Independent audit has not been performed.
