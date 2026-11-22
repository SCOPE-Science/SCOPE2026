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

The exact observation formula is obtained by conditioning on the four occupancy states and the exponential race. Direct substitution into the printed inverse formulas proves the uniform identification assertions within the strictly positive domain. The two rational witness tables were checked using exact `fractions.Fraction` arithmetic: the three pairs of cause-label probabilities coincide, the latent covariances have opposite signs, and the fourth-window probabilities differ by exactly \(231/400000\).

`python check.py` executes the rational checks and 10,000 deterministic randomized balanced inversions plus 9,419 unbalanced inversions (remaining draws have marginal differences too small for the stipulated floating-point inversion test). Execution on the embedded checker printed all checks PASS. These numerical checks are auxiliary and cannot prove claims at the continuum level; the analytic inverse and exact witness provide that proof.

No field data, external experimental replication, independent audit, numerical conditioning guarantee, or general unequal-rate inference is claimed. The first public date associated with the motivating ecological source is 2024-07-24, as recorded by the publisher. The supporting historical literature has not been proved exhaustive.
