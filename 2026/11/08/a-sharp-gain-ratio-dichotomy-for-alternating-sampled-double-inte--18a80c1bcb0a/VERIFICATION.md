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

# Reproducible checks

Use Python 3 with the dependency in `requirements.txt`, then run `python verify_periodic_pd.py`. The standalone script derives the exact single-step determinant/trace and the two-step Jury-margin polynomial using symbolic identities; it also checks the critical boundary values and the explicit rational instability witness.

The second verifier uses `fractions.Fraction` to compute the transition matrices and strict Jury inequalities independently over \(9{,}227\) rational sampled cases, including explicit destabilizing samples throughout the open gain-ratio window. `verification_output.txt` records the actual execution status.

# Proof and reproducibility limits

Only the analytic Jury inequalities and boundary-reduction argument establish the universal assertions over all positive real gains and all admissible periods. Neither the rational grid nor symbolic equality checks constitute exhaustive numerical verification of all real parameter values. The analysis does not cover arbitrary switching among more than two sampling intervals. No external independent validation has been performed.
