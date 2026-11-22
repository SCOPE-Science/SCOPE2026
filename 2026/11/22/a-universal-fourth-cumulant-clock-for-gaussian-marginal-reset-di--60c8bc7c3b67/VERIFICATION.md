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

Run `python verify.py` with Python 3, NumPy and SciPy available. The checker computes scalar two-time joint moments by exponentiating a polynomial-generator matrix for multiple non-Gaussian refresh laws and verifies the stationary Gaussian moment hierarchy. An independent nonsymmetric two-dimensional case evaluates the four-moment mixture using the conditional Gaussian propagator and tests the tensor and complete inverse-covariance contraction. The recorded result is 156 deterministic checks passed. The symbolic proof, not the finite checks, establishes the arbitrary-dimension identity and parameter quantifiers.

The reset source is independently nonnegative under the stated rate conditions. The observation domain is any fixed positive lag and exact stationary ensemble quantities. No finite-sample inference bound, global publication priority, external proof assistant, or independent scientific validation has been performed.
