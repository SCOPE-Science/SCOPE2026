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

The pointwise identity and quantile-region equivalence follow analytically for any Borel probability supported on a full-dimensional simplex. The key strict inequality in the cap argument handles atoms and boundary mass without continuity assumptions. The empirical median reduction is exact at every sample size.

The supplied `verify.py` was executed from this file's companion package path using `python verify.py`. Its output was `EXACT_OK 15707`. The assertions use rational coordinates, enumerate all subsets of small finite samples against the translate-exclusion feasibility criterion, and test quantile depth regions, empirical maximizers, uniform-model evaluations and boundary-supported measures.

Limits: Enumerations are finite supporting checks and cannot establish the universal statements without the displayed proof. The criterion requires all probability mass to lie in the chosen testing simplex. No independent mathematical audit has been performed.
