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

Execute `python3 verify.py` in the same directory as these documents. This uses only the Python 3 standard library and a deterministic random seed. At preparation it printed `PASS: 84948 exact/algebraic/numerical comparisons (finite evidence, not a proof)`.

The verifier independently integrates the covariance kernels using exact rational arithmetic at 99 sample fractions, compares the canonical noiseless optimizer against its closed form, confirms phase-boundary identities at rational parameter values, evaluates the objective over 700 sampled parameter pairs and 121 test sites each, and evaluates four near-critical square-root expansions.

The displayed theorem is analytic: global uniqueness follows from the sign of the quadratic in the derivative of the exactly derived conditional risk. Exhaustive checks over continuous parameter spaces are not implied by the finite verifier; no external independent mathematical audit has been performed. Publication priority and other Gaussian models remain unverified.
