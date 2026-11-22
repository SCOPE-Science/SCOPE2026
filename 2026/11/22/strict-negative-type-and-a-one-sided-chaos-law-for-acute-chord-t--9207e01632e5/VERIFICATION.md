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

The mathematical argument derives the exact acuteness belt-minus-cap kernel, computes all nonconstant Funk--Hecke eigenvalues by a beta integral, obtains uniform convergence and negative type, and then applies the canonical Hoeffding decomposition with a finite-harmonic central limit theorem and a uniform \(L^2\) tail estimate.

Run `python3 verify.py` with Python 3. The supplied checker numerically re-integrates the kernel and the first twelve harmonic eigenvalues, compares the spectral trace and squared mass against exact formulae, verifies the algebraic Hoeffding variance decomposition at multiple sample sizes, and independently simulates the Euclidean acute-region event at three prescribed chord separations. The observed execution ended with `ALL_CHECKS_PASSED`.

The numerical truncations and simulations are not exhaustive proofs of infinite-dimensional convergence, novelty, or independent validation. The upper-support statement follows from the absolutely summable exact spectrum and nonnegative independent chi-square terms; the uniqueness of the optimizer requires the full harmonic separation argument. No external mathematical audit has been performed.
