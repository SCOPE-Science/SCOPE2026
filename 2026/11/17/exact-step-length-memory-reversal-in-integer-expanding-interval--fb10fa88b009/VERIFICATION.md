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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 and its standard library. The code integrates the product of two piecewise-affine trajectory step-length observables over an exact rational common refinement of all relevant branch boundaries. It tests slopes two through seven and lags one through three, compares against the proposed all-lag covariance expression, and checks the sign classifications and rational asymptotic-variance expression for slopes two through fifteen.

The observed successful output was:

```
VERIFY_OK transfer_eigen_checks=96 exact_piecewise_integrals=18 covariance_lags=1..3 slopes=2..7 sign_and_variance_cases=14
```

The program uses no sampling or approximate floating point, but a finite collection of cases cannot prove the all-parameter theorem. The general proof is given in `RESULT.md`: exact branch integrations, transfer-operator eigenidentity, and an explicit bounded reverse-martingale decomposition. Independent audit and independent mathematical validation have not been performed.
