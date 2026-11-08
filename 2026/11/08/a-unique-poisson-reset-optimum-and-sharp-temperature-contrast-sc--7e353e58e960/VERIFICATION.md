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

# Verification summary

The analytic statements and normalization can be reconstructed using only `RESULT.md` and the code `verify.py`. In an environment with Python 3 and `mpmath>=1.3.0`, run `python verify.py` in the extracted package directory. This execution passed 36 numerical comparisons: alternative integral identities at six width ratios, derivative sign and local maximum checks, and the two limiting frequency/height scales. The code prints the tested dimensions and resulting optima for reproducibility. See `requirements.txt` for the numerical dependency.

The exact theorem is proved by the single sign change in the second time derivative of the per-cycle divergence, a strictly monotone ratio of opposite-sign Laplace contributions, and exact asymptotic comparison. No finite grid proves uniqueness over a continuum. The code does not certify physical dissipation or experiment-specific reset implementation, and independent mathematical review has not occurred.
