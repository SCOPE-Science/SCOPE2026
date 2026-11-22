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

# Verification of the Brownian quadratic-energy one-bit theorem

The proof in `RESULT.md` establishes the infinite-parameter and unrestricted-encoder result. Execute `python verify.py` after installing the `mpmath` dependency indicated in `requirements.txt`. The captured successful output is `verification_output.txt`, and its values were compared to an independently executed high-precision tail-probability calculation.

The verifier checks exact fractional covariance identities, the unquantized one-site optimum, normal tail integration by independent quadrature, the scalar critical equation, and the Bayes conditional decoder moment identities. The code also samples the monotone centroid-ratio inequality. Finite numerical samples are **not** presented as proof of threshold uniqueness or of global optimization over Borel encoders; those properties follow from the analytic rearrangement and monotone-likelihood-ratio/hazard arguments.

The scientific result does not cover noisy, adaptive, or multiple-point sensors. No independent mathematical audit is represented by these checks.
