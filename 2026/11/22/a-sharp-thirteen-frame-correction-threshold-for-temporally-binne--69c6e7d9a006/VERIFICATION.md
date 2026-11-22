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

## Reproducibility and scope

Run `python3 verify.py` using the accompanying source file and Python standard library. The assertions exactly check the normalized covariance identity, finite boundary differences, the rational 13-frame breakpoint and the local-but-not-global 13-frame example. The proof of the all-integer global result is mathematical, via consecutive-difference sign and decreasing positive terms, not through bounded test enumeration.

This work has received self-review only; independent audit or physical calibration has not been performed. Reference timing edge effects, uncorrected fixed target detector variance, nonuniform windows, partial subtraction coefficients, nonstationarity and spatial atmospheric decorrelation lie outside the theorem.
