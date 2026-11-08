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
Run `python3 verify.py` with a standard Python 3 installation. It deterministically samples 60,000 states in the closed triangle across eight weight ratios and three step strengths, checks forward invariance and potential descent, checks eigendirection slope inequalities, and checks critical multiplier sign on six boundary probes.

The actual execution output was:

```
VERIFY_OK triangle_samples=60000 slope_cases=8 critical_spectral_cases=6
LIMIT: finite sampling supplements, but does not establish, the theorem
```

The proof itself is the finite series of analytic steps in `RESULT.md`. No calculation here certifies an infinite family by finite sampling. The classical stable-manifold theorem is used for hyperbolic fixed points, and the degree-one covering argument is used for global invertibility. There has been no independent scientific validation.
