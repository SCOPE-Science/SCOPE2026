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

# Reproduction and mathematical checks

Run `python verification/verify.py` in this package after installing `verification/requirements.txt`. The actual executed check returned:

```
PASS 660 exact rational tests and 210 numerical kernel-system tests
```

The exact tests verify tridiagonal kernel identities, the Sherman–Morrison formula, strict interior positivity, endpoint thresholds and the reconstructed noisy linear system. The numerical tests directly invert physical exponential-covariance matrices rather than reusing the closed-form result. These tests cover only finite parameter samples. The full theorem relies on the explicit precision-matrix proof, exact sign factorization and the elementary weak-limit argument in `RESULT.md`; no independent audit was conducted. The paper-priority assessment is limited to explicitly inspected accessible sources and should not be construed as a comprehensive uniqueness certificate.
