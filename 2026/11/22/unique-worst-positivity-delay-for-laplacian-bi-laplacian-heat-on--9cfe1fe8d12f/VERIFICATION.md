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

# Computational verification

Run `python3 verify_mixed_star.py` with Python 3, NumPy and SciPy available. The checker independently constructs eight star Laplacians, uses SciPy's matrix exponential, tests spectral-entry formulae and exact-root sign changes across seven positive mixing strengths, and compares independent root optimizations to the derived logarithmic optimizer.

Observed output from the packaged script:

```
INDEPENDENT_MATRICES_AND_HORIZON_SIGNS_PASS 280
OPTIMAL_STRENGTH_AND_LARGE_STAR_LIMITS_PASS 11
STAR 2 ETA_STAR 0.43500904290195 MAX_TIME 0.20047404849102
STAR 3 ETA_STAR 0.36558658251019 MAX_TIME 0.16340490904944
STAR 5 ETA_STAR 0.28333620407334 MAX_TIME 0.12011714415753
STAR 10 ETA_STAR 0.18994059894152 MAX_TIME 0.073122454235974
STAR 100 ETA_STAR 0.037859356614782 MAX_TIME 0.0094929013071166
```

Finite floating-point checks cannot establish uniqueness for all positive parameters or equality in the infinite-star limit. Those statements are established analytically in `RESULT.md`. No independent mathematical audit was performed.
