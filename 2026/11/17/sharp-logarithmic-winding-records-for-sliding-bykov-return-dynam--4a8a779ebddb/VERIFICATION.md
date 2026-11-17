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

# Reproducibility and boundaries

The proof is analytical and does not require code. To verify it, read source [1] in the order indicated below: (1) equations (17) and (18) establish the branch-position exponent \(2\pi/|\kappa|\); (2) equation (23) and the following inequality establish uniform inverse-derivative comparability; (3) Lemma 5.4, especially its check of (C6), establishes uniform relative Hölder control and contraction; (4) Theorem B and Appendix C, Proposition C.4 establish conformal and equivalent invariant probabilities. The new finite-word bounded-distortion and quasi-Bernoulli arguments are explicit in RESULT.md and should be reconstructed before accepting the stochastic conclusions.

In particular, check the distinction between marginal exponential tails (insufficient by themselves for the lower record bound) and the stronger uniform *prefix-conditional* inequality, which drives the avoidance-probability bound without independence. Check the boundary exponential moment at its critical exponent, where the lower tail bound forces divergence. A finite shift of the branch index changes only multiplicative constants, not exponential rates.

There are no experimental logs, borrowed proof certificates or external validation claims. The sections remain fixed, and no uniformity as the section radius tends to zero is claimed. Independent audit: not performed.
