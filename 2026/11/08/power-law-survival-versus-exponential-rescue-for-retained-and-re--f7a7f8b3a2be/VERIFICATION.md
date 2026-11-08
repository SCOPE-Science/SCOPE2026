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

The central proof is self-contained in `RESULT.md` and separates the known inverse-local-time identity from the new heavy-tail transfer. Its structural checks are: (1) Brownian first-boundary-contact local-time inverse normalization; (2) one-cycle point-mass/exponential reward distribution; (3) concentration despite reward-duration dependence; (4) regularly varying survival sandwich; (5) fresh independent-threshold restart transform and positive exponential moment; (6) Lomax mean criterion and optimum corollary.

Run `python CHECK.py` with Python 3 and SciPy. It verifies the reward distribution using an independent reflection-principle integral, the exponential-mixture moment generating function, the reward rate constant, independent fresh-Lomax renewal means, the rate optimum and asymptotic regular-variation ratios. It does not numerically prove a limit over all times or uniqueness of published precedence. The source comparisons in `AUDIT.json` retain residual priority risk, and no independent audit has been performed.
