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

# Reproducibility

The analytical argument and scope are in `RESULT.md`. To reproduce the finite checks using only Python's standard library, run `python3 verify.py`. The program checks exact categorical covariance identities at rational probability parameters; numerical brackets and values for the two stationary roots; positivity of the derivative-convexity numerator at sampled points; and exact finite multinomial moments, including their observed approach to the stated limiting coefficient.

A completed execution reported `PASS: 296 deterministic assertions`. These are finite checks only. The existence, uniqueness, and global-optimality assertions rely on the displayed analytic derivative and strict-convexity identity, which can be verified by elementary differentiation. The standard Gaussian absolute-product identity is justified in the proof by differentiation and integration.

There has been no independent mathematical audit. In particular, the calculations do not certify historical priority, optimize arbitrary three-bin profiles, or supply a maximizing parameter for each finite sample size.
