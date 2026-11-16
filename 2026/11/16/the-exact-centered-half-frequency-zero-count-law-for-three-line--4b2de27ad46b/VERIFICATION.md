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
Run `python verify.py` with Python 3 and no additional packages. The checker directly computes quadratic roots and compares the Schur count, maps sampled polynomial zeros back to Gaussian-STFT cancellations, checks the general unequal-amplitude balance radius, and compares Monte Carlo zero-count frequencies to the exact probabilities. Its deterministic seed and tolerances are documented in the code. Output in the reviewed package was `THREE_LINE_HALF_STRIP_CHECKS_PASSED 451910`.

The analytic proof in `RESULT.md` is required for the infinite-parameter assertion: stochastic tests alone cannot establish universal validity, boundary simplicity, or publication originality. No independent external mathematical audit has been performed.
