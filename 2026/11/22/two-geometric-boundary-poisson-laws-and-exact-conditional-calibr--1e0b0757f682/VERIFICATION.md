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

# Verification record

## Scope and reproducibility

The theorem concerns iid samples from the zero-based geometric distribution with a potentially sample-size-dependent success probability. The reproducible script `check.py` requires Python 3 standard library for exact arithmetic and optionally NumPy for Monte Carlo; invocation is `python check.py`. It tests the exact deterministic studentization identities for bounded tuples, the score variance in rational arithmetic, weak-composition normalizers, and conditional-tail p-value superuniformity on finite grids. It also simulates geometric samples by first drawing their zero count and then drawing the conditional sum of positive geometric observations, an exact distributional construction rather than an approximate sampler.

## Checks performed

`check.py`: 13,626 assertions passed. High-mean critical simulation at \(n=20000\), \(\lambda=1/6\), 40,000 replicates gave rejection fraction 0.155950, versus the limiting 0.153518. Near-degenerate critical simulation at \(n=100000000\), \(\lambda=1/6\), 40,000 replicates gave rejection fraction 0.148475, versus 0.153518. The extremely large second sample size was chosen because that boundary approaches the sparse Poisson limit slowly. The computed normal critical intensity was 0.176524554935, with limiting near-critical rejection 0.161821802509. Numerical results are reproducibility checks only; all infinite-sequence claims depend on the written proof.

## Scientific limits

No finite simulation proves weak convergence or sharp necessity. Exact fractions verify only finite algebraic subidentities; the proof must be read for Lyapunov and Poisson arguments. The original article's fixed-parameter central limit theorem must not be extended to moving parameters without the new proof. Critical-value ties were deliberately excluded from the explicit rejection-probability conclusion. Historical uniqueness is not guaranteed by the literature searches. Independent scientific audit has not been performed.
