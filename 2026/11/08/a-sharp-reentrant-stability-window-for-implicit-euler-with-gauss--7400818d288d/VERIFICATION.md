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

# Reproducibility checks

Run `python verification/check.py` from the extracted package root with Python, NumPy and SciPy installed. The checker was executed and printed `CHECKS_OK 824; crossing=1.306929727719281; acrit=1.278077587526104`.

Its finite checks include a separate direct Gaussian integral for the log potential (split at the singularity), the Dawson derivative equation, the global minimum over sampled noise amplitudes, analytic-versus-finite-difference sensitivity comparisons, both reentrant roots in five test regimes, and fixed-seed Gaussian sample means. Critical values are numerically approximated, not interval-certified. The infinite-time assertions, uniqueness, and moment divergence depend on the self-contained proof in RESULT.md. No independent mathematical audit has been performed.
