# Scientific assessment of the rank-one robust sampling theorem

## Correctness — PASS

The exact objective is the supremum of squared current-row mass divided by the probability selected from the reference. The upper bound is derived by a coordinate orthogonality estimate and weighted Cauchy, and is reached by an explicit orthonormal pair. The elementary one-parameter optimizer is checked at both boundaries; the uniform-reference coordinate adversary provides a matching lower bound **against every sampling policy**. The analytic proof covers all real \(m\ge2\) and \(0\le\theta\le\pi/2\), including reference zeros. The standalone standard-library checker passed 11,050 supporting assertions; experiments are not used in place of universal proof. The stated Bernstein corollary is only a bounded-summand upper bound.

## Originality — PASS, with residual historical risk

Fakih--Grigori--Pierce, arXiv:2607.22194v1, analyze target-leverage row sampling with a current/target inflation term for CP-ALS. Unlike that analysis, the new claim optimizes over arbitrary distributions based on a rank-one reference under an angle cap and proves a piecewise *equality* with a matching lower bound. Larsen--Kolda, arXiv:2006.16438, discuss leverage-based tensor sampling and deterministic high-leverage inclusion; only an abstract-level comparison was available. Derezinski et al., PMLR 99 (2019), optimize estimator errors under response uncertainty rather than this coordinate-inflation loss. Raj--Musco--Mackey, PMLR 108 (2020), develop local sensitivity for finite-sum objectives and quadratic-proxy leverage bounds, rather than a sharp angular two-vector minimax game; relevant published PDF sections were inspected. Related published mathematical records on coordinate energy contraction, adaptive pivoting and Haar subspace descent do not directly imply the present quantifiers. Literature searches cannot establish absolute priority; an unindexed equivalent or an uninspected theorem remains possible.

## Value — PASS

Cached leverage sampling can assign zero probability to newly activated rows even under arbitrarily small positive drift. This theorem gives an *all-policy* optimal repair, its exact angle-dependent mixture weight, and a sharp switch to uniform sampling. The resulting sampling-weight factor is the coefficient in standard bounded-summand concentration calculations. This is a natural algorithmic design boundary, not an assertion of improved full tensor decomposition or tail-minimaxity. Rank-one scope and the requirement to know the drift angle are significant limitations.

Self-review: passed. Independent audit: not yet performed.
