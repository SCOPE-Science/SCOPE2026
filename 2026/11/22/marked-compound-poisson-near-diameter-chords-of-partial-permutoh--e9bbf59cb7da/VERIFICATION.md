---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The top-k label classification gives exactly (m)_k vertices of rank k. The norm bound is saturated only at rank n, and nonnegativity makes disjointness equivalent to zero cross term. Thus the known diameter equality cases count to the exact unconditional atom for independent ordered draws with replacement. On the event that both draws are full rank, W is the inner product divided by n². The centered permutation covariance has eigenvalue (Q_n−S_n²/m)/(m−1) on the mean-zero space and vanishes on constants; squaring and taking its trace gives the stated variance. An independent m=4,n=2 hand count gives atom 24/289, conditional mean 9/16 and variance 121/768. In the critical regime the hypergeometric overlap has all falling-factorial moments tending to λ^r, and at each fixed overlap size the two ordered samples of scaled labels converge to independent uniform marks. Tightness of the overlap and full-rank probability 1−O(1/(m−n)) transfer this compound-Poisson limit to the actual draws. The critical zero probability follows separately from the exact no-overlap product, so does not rely on weak convergence at an atom. In the subcritical and supercritical cases, the conditional mean and relative variance give the stated mean-scale limits, using Markov and Chebyshev respectively; the overlap mean bound and the exponential no-overlap bound give the corresponding zero-atom limits.

## originality

PASS

The prior diameter, equality classification, and standard permutation/hypergeometric formulas are inputs, not novel results. The supported distinct contribution is the uniform arbitrary vertex-pair deficit law, particularly the marked critical law and related atom transition; it is neither the edge spectrum nor the pair-distance law of the different doubly substochastic matrix model.

## value

PASS

A worst-case diameter does not indicate whether a typical ordered pair attains it or how it misses when it does not. The result identifies a sharp birthday-scale transition and the nontrivial weight distribution of rare overlaps, not merely a contact census. It is a usable native-metric benchmark for uniform vertex pairs with a distinct normalization on either side of the transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
