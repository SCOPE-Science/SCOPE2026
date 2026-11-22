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

Execute `python3 check.py` using Python 3 with only the standard library. The independent checker reconstructs the two substochastic finite-state kernels with exact `fractions.Fraction` arithmetic; it verifies each row sum and the one-row rank-one perturbation, computes temporal cumulative absorption, then compares each coefficient against the nonnegative convolution factorization in the proof.

Observed output:

```
PASS 17760 exact rational temporal identities and sign checks across 40 finite systems
Covered both reflection protocols, lazy and non-lazy dynamics, and N=2 boundary degeneracy.
```

The 40 systems consist of corridor sizes \(N=2,3,4,5,6\) and eight parameter pairs, using every initial state and horizons through \(36\). This is not an exhaustive computation over all parameters or all times. The general theorem relies instead on the analytic generating-series and positivity proof in `RESULT.md`. Publication-priority originality remains dependent on availability of relevant literature, and no independent audit has been performed.
