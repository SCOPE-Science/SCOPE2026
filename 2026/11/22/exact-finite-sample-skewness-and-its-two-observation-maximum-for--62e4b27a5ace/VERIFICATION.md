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

# Verification

The complete proof and all five exact rational contraction values appear in `RESULT.md`. The included `check_moments.py` is an executable, third-party-dependency-free exact integration checker. Run `python3 check_moments.py`. It verifies the kernel-contraction constants, the mean and variance, the cubic-moment identity for 150 positive integer sizes, the finite-sample skewness maximum and the monotonicity derivative sign. The all-size moment and skewness statements are proved symbolically in the result, not by finite enumeration. Independent mathematical review has not been performed.
