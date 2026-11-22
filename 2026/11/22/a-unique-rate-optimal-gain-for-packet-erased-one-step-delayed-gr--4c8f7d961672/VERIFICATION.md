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

Run `python verify.py` after installing `requirements.txt`. The self-contained verifier reconstructs the 3-by-3 covariance transfer, characteristic polynomial, critical frontier and optimizer resultant symbolically; independently enumerates rational Bernoulli branch histories for the five-step finite checks; and compares the predicted optimizer against numerical spectral minimization for 99 success probabilities. Exact symbolic identities were confirmed and 405 path/moment tests plus 99 numerical optimization checks passed. The analytic proof in `RESULT.md`, not sampling, supplies uniqueness and all-real-parameter guarantees.

The stability-bound formula is known in an algebraically equivalent form for a different fresh-or-stale gradient model and is not claimed as the novel result. This report verifies only the stated erased-or-stale recurrence. The theorem is not a finite-horizon or pathwise rate claim, and neither source priority nor the mathematical reasoning has received an independent audit.
