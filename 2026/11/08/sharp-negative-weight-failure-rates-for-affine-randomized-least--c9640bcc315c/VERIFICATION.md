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

# Verification and limits

Run `python3 verify.py` using the Python 3 standard library only. Observed output:

```
EXACT_RATIONAL_CASES 4648
P3_BAD 0.321349540849 MONTE_CARLO 0.320833
LAMBDA_STAR 1.263164403304
EXPONENTIAL_RATE 0.172761450635
VERIFY_OK
```

Exact fractions test the normal-equation weights, exactness on constants and linear polynomials, and the negative-weight sign-event equivalence at 4,648 configurations. Numerical integration checks the closed three-sample integral and the Gaussian error-function expression for the moment generating function. The numerical derivative locates a unique root on the bracket used by the proof; seeded simulation is illustrative only.

The probability identity for three uniform samples and the exponential rate for every qualifying symmetric law are proved analytically in RESULT.md. No finite test, simulation, log, or numerical optimizer alone certifies the infinite large-deviation claim. The asymptotic conclusion uses a standard Cramér large-deviation theorem; its normalization and requisite strict interior event are explained there. The only decimal constants are reproducibility aids, not interval-rigorous numeric certificates. Independent validation has not been performed.
