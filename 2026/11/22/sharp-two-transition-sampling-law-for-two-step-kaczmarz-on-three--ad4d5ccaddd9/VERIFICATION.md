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

# Verification and boundaries

The Python checker bundled with this result evaluates each actual ordered projection product, constructs the weighted second-moment matrix independently of the symbolic derivation, and compares its largest eigenvalue at nine rational parameter values against the theorem. Nine finite-direction minimax linear programs, one at each parameter, independently optimize all nine ordered-pair probabilities under 360 sampled initial directions. The checker also tests exact rational benchmark factors. Its actual output was:

```
PASS 22 standalone exact/numeric checks; finite directional LP grid has 360 test angles
```

This validates finite computations only; it is not exhaustive in angle or parameter. The universally quantified claim is proved analytically in `RESULT.md` by a Loewner bound, reflection convexity, two monotone affine modes and equality conditions. A distribution chosen using the current initial error or residual is outside the permitted class, as are multiple batch horizons and nonorthogonal relaxations. No independent audit has occurred.
