# Scientific assessment

## Correctness — PASS
The vertex count and fixed-edge occupancy probabilities follow by deleting one or two disjoint matched pairs; same-row/column joint occupancy is zero. These three cases generate the full covariance matrix and, by an exact row/column-sum identity, all its Frobenius eigenvalues with multiplicities summing to the full ambient dimension. The strict middle-to-low gap is certified by the real, simple, positive zeros of ordinary Laguerre polynomials: the matching-size distribution is an unequal-parameter Bernoulli sum with variance strictly smaller than the binomial variance at the same mean. The high-dimensional limits follow from Perron's *complex-domain* Laguerre formula, whose local uniformity permits analytic differentiation for deficiency moments. Rational exact enumeration at orders 2–4 and large-size numerical checks corroborate but are not substitutes for those arguments.

## Originality — PASS (priority provisional)
Heuer–Striker (2020) identifies and counts these vertices, rather than their uniform-vertex covariance operator. Eisley–Matsushita–Vindas-Meléndez (2024) studies graph matching polytopes via Gorensteinness and integer decomposition. A published John-ellipsoid result is for precisely this polytope and uses its same three symmetry modules, but the extremal inscribed-ellipsoid operator is not the covariance of uniformly sampled vertices and its eigenvalues have different asymptotic orders. Searches for random rook placements, uniform partial permutations, vertex covariance, eigenvalues, and equivalent row/column contrasts yielded no recorded dominating theorem. Existing Laguerre zero/asymptotic inputs are explicitly credited and not claimed new. Residual risk: a legacy random-matching covariance calculation under different nomenclature, especially within older statistical literature.

## Mathematical value — PASS
The uniform vertex cloud is a canonical discrete geometric measure on a full-dimensional polytope; its covariance determines quadratic directional dispersion, principal axes, and whitening. The theorem completely determines this operator, proves a nontrivial strict spectral hierarchy *for every dimension*, and gives the sharp \(2\sqrt n\) growth of its anisotropy. The separation between nearly constrained row/column modes and unconstrained doubly centered modes persists despite the full-dimensional support. This is not implied by the combinatorial vertex count or by the optimization geometry of John's ellipsoid, and provides a reusable exact benchmark for discrete isotropic-position questions.

## Limitations and independent assessment
The claim excludes volume-uniform sampling, fixed matching rank and unequal bipartition sizes; the spectral asymptotics use classical complex Laguerre theory. Historical priority beyond accessible sources is provisional. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
