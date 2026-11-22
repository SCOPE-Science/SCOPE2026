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

# Reproducibility and mathematical limits

The accompanying `check.py` runs only with Python standard-library modules and uses exact `fractions.Fraction` identities for the rational-parameter test and numerical direct checks of stationarity, pulse boundaries, and the first-variation inequalities. From the packaged file, run `python3 check.py`; the observed output was:

```
PASS: exact rational identities, source-example thresholds, pure-pulse cutoff, and first-variation inequalities for the mixed pulse–continuous branch
```

The proof is symbolic and all-parameter: renewal representation establishes positivity and strict convexity, the adjoint gives the optimality certificate, and the branch is verified directly by both state and adjoint equations. Numerical checks use finitely many sample times and are explicitly not claimed as exhaustive, or as validation of the epidemiological interpretation. The theorem does not quantify nonlinear outbreak incidence, policy feasibility with rate caps, or independent proof review. A previously published closed-form equivalent outside inspected material remains possible.
