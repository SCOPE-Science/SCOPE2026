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

# Verification of the mathematical result

Run `python check.py` from the directory containing this document. The script uses Python standard-library `math` and `random`, no internet and no scientific dependencies. It evaluates the polar Gaussian wedge integral numerically, confirms the closed form on 75 sample-size/scale configurations, checks the atom coefficient on five sample sizes, tests four seeded direct Monte Carlo samples, and checks two large-size smooth-limit approximations. All 86 tests passed in the working environment.

The exact analytical proof in `RESULT.md` is the basis for the universal claims. In particular no finite numerical tests certify every sample size, positive margin variance, or the absence of other unbiased estimators. The Cauchy--Schwarz argument concerns only the independent single-term debiaser and primitive conditional sample costs.

Independent scientific validation has not been performed.
