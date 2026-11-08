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

# Reproducibility and verification

**Analytical basis.** The proof uses Brownian scaling and Wick's formula to compute the quadratic reward's first and second moments; regular variation and Breiman's lemma for its right tail; normal/stable iid domains of attraction; renewal-age tightness and random-index convergence. These analytical inputs, and the exact Pareto and independent-restart hypotheses, are necessary for the infinite-horizon claim.

**Executable diagnostics.** Run `python checker.py` after installing NumPy and SciPy. It checks exact moment constants against independent Karhunen–Loève and covariance-integral calculations, compares Brownian quadratic-area Laplace transforms, independently computes a stable-law fractional moment, verifies the sign and scaling of its characteristic exponent, checks Pareto normalization and critical coefficients, and tests sampled complete-cycle rewards.

**Limitations.** Finite sample checks do not establish almost-sure or weak limits and do not prove originality. Independent scientific audit has not been performed. No external verifier or certification is implied.
