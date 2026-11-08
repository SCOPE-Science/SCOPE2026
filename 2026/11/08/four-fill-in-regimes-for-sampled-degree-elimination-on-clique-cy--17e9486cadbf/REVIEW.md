# Scientific review: sampled-degree elimination on clique–cycle joins

## Correctness — PASS

For the precisely specified uniform-without-replacement candidate rule, every pre-hub rim deletion inserts one chord and preserves the clique–cycle join. A hub selected while at least four rim vertices remain makes the surviving graph complete, giving the exact excess \(\delta_k=(k-2)(k-3)/2\). Current degrees distinguish hub and rim vertices strictly until the remaining rim is a triangle, hence the exact hazard \(p_k=\binom hq/\binom{h+k}q\) for \(q\le h\), otherwise zero. The product of survival hazards yields the full distribution. Beta-binomial factorial moments establish the exact one-candidate mean; uniform tail expansions establish the other mean regimes and the sharp limiting tail. The standalone exact graph-state checker validates 491 comparisons and sanity tests, including 128 exhaustive distribution/normalization assertions and 5 independent full-permutation distributions. The infinite-scope statements are proved analytically, not inferred from finite testing.

## Originality — PASS, with residual risk

Relevant primary papers were inspected by statements and algorithms. The candidate-sampling scheme in Fahrbach et al. (2018) uses an approximate degree estimator, adaptive sketches, and exponential perturbations; it does not assert the fixed-\(q\) uniform sample law. Cummings et al. (2019) compute exact minimum-degree orderings efficiently rather than analyze this random restricted-candidate rule. Chen et al. (2020) randomize edges of Schur-complement cliques, not sampled vertex candidates. The closest item in a published mathematical findings index on wheel graphs concerns Löwner ellipsoids, not elimination fill; other nearby hits concern randomized matrix pivoting or greedy independent sets, neither of which logically supplies the claim. An accessible research ledger contains no claim of symbolic fill-in laws on clique–cycle joins. These comparisons support a qualified originality assessment, not a claim that unsuccessful searches prove priority. Exact precedence in less accessible specialized sparse-ordering literature remains uncertain.

## Mathematical value — PASS

The concrete object is a standard family of sparse matrix patterns with a small clique separator and a large cycle. The invariant is the exact number of new edges in Cholesky symbolic factorization, which directly affects storage and symbolic fill prediction. The contribution is more than a single example: a complete all-parameter finite probability law, sharp transitions in expected excess fill across four sampling budgets, a nontrivial limiting distribution, and a sharp heavy-tail/moment classification. It distinguishes high-probability small fill from heavy-tail-affected expected fill for the two- and three-candidate rules. It does not claim numerical performance benefits, arbitrary-graph results, or a new minimum-degree algorithm.

## Closest literature and limits

- Fahrbach et al. (2018), arXiv:1804.04239, Sections 1, 3, and 5: sampled approximate-degree candidates under an adaptive data-structure model; different selection law and theorem target.
- Cummings, Fahrbach, Fatehpuria (2019), arXiv:1907.12119, introduction, Section 2 and main results: exact minimum-degree ordering complexity, no present distribution or asymptotic profile.
- Chen, Liang, Biros (2020), arXiv:2011.07769, Sections 1, 3 and 4: sparsified Schur-complement edge sampling and ordering comparisons, but not fixed-size random pivot-candidate selection.
- Rothberg and Eisenstat (1998), DOI:10.1137/S0895479896302692: prior bottom-up node-selection strategies; only abstract-level material was accessible in this review.

Remaining scientific limitations: fixed hub count, clique–cycle join structure, exact symbolic fill only, and unresolved specialist publication precedence. Computed checks do not provide independent validation.

Self-review: passed. Independent audit: not yet performed.
