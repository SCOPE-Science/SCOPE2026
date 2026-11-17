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

The standalone `verify.py` reconstructs the row-centered Gram identities symbolically, checks \(\det A(r,s)=(1-s)(1+s-2r^2)\), verifies the exact one-step reduction to the meridian and its scalar map, and checks the two endpoint Taylor constants. It also evaluates full Pearson correlations on 530 reproducibly sampled admissible matrices, including 15 diagonal equality cases and 15 rank-deficient boundary cases, then iterates the exact scalar map independently for 700 steps and checks all three basin outcomes.

Observed output: `VERIFY_OK symbolic_identities=11 case_total=530 basin_counts= {'left': 239, 'right': 276, 'equal': 15, 'boundary': 15} local_superattraction=3/2 local_mixed_multiplier=1/sqrt(3)`.

These are finite reproducibility tests rather than an infinite proof; the proof is a global scalar sign and monotonicity argument valid on the full stated domain. The source's full-dimensional global convergence theorem and invariant meridian are prior, not independently validated here. Independent audit has not been performed.
