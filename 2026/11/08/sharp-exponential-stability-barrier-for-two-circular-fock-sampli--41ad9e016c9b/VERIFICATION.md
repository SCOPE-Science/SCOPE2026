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

The standalone `check.py` computes the exact Poisson-contact constants, checks the two-center covering inequality for 15,000 deterministic randomly chosen radius pairs, compares the full complex observation Gram with its predicted spectrum for degree at most 12, and evaluates the lower-frame exponent through degree 4,000 using logarithmic arithmetic. From this package it prints `TWO_RING_FOCK_CHECKS_PASS 19561`.

Analytical verification consists of (i) a direct finite Fourier sum, (ii) convexity and derivative comparisons establishing the unique two-interval level-set cover of the normalized degree interval, (iii) Stirling's formula with uniform \(O(\log(n+1))\) remainder at fixed positive scaled radii, and (iv) a compactification/subsequence argument excluding any sharper exponent from radius sequences of arbitrary growth. Numerical computations do not establish universal quantifiers.

The scientific comparison was made against the full-text Fock-polynomial MZ theorem (arXiv:2109.11825 / doi:10.1007/s00209-022-03087-4), multivariate Fock lattice results (arXiv:1905.09927), and Bergman/Hardy polynomial MZ results (doi:10.1007/s12220-020-00599-5). Older information-geometric two-center theorems could provide a more general equivalent scalar result and remain a priority uncertainty. No independent audit was performed.
