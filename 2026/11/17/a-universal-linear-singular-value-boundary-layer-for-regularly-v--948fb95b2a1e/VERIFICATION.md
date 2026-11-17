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

# Reproducibility and scope

The analytical proof depends on five reconstructable facts: the exact binomial log-weight recurrence; monotonicity of the resulting singular values; uniform convergence for regularly varying sequences away from zero; an exponentially small binomial exceptional set with logarithmically controlled weight ratios; and a Potter-envelope summable tail when \(\beta p>1\). Every infinite-rank step is justified in `RESULT.md`.

The standalone standard-library script `check.py` verifies the one-step update and binomial expectation by independent finite iterations; computes normalized operator and Schatten coefficients on several increasing binomial counts; and checks the counting profile with finite cutoffs. Numerical residuals do not establish universal asymptotics or originality.

No independent audit or external mathematical validation has been performed. The first-public timestamp is from the arXiv submission history. Priority remains provisional because not all plausible earlier full texts were available.
