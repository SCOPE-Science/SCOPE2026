# Scientific review

## Correctness
**PASS.** The statement explicitly specifies ordinary Euclidean coordinates, rank-uniform vertex sampling, \(m\ge2n\), and sparse asymptotic limits. Proposition 5.7 of Heuer–Striker supplies the exact rank-\(k\) vertex count \((m)_k\); the direct nonnegative-norm inequality gives the diameter equality cases. Two independent random permutations yield the exact conditional mean and covariance formulas. The overlap is hypergeometric, and its factorial moments and uniform marks prove the critical compound-Poisson convergence. All eight finite enumerations, variance identities, and exact diametral atom checks passed using the embedded verifier. No finite check is used as an infinite proof.

## Originality
**PASS, subject to historical priority.** The original 2020 Heuer–Striker article provides vertex structure, facets, and volume questions; the full 2022 Behrend et al. preprint covers face enumeration and polytope volume/Ehrhart. The closest published metric findings give exact **diameter** and **edge** lengths, which do not determine the uniformly sampled arbitrary vertex-pair deficit law. Searched aliases included sparse permutation inner products, support collision statistics, diametral random pairs, and compound-Poisson marked overlaps. A generic sparse-permutation birthday calculation is mathematically related but neither of the cited primary polytope papers presents the stated geometric limit. Possible unindexed equivalent stochastic results are an explicit residual risk.

## Mathematical value
**PASS.** The diameter by itself is known; the new quantitative question asks whether a uniformly sampled pair of polytope vertices is *actually diametral* and how it falls short. The exact atom and the three-regime transition at \(n\asymp\sqrt m\) demonstrate a measurable geometric distinction invisible to the worst-case diameter and to adjacent-edge spectra. The critical marked product law gives nontrivial jump statistics rather than only a Poisson count.

## Closest literature and limitations
Heuer–Striker, arXiv:2012.09901, Proposition 5.7; Behrend et al., arXiv:2207.14253; published geometric diameter result and adjacent-edge-length result listed in RESULT.md. The result is restricted to sparse labels and uniform vertex pairs, not full-volume sampling or arbitrary aspect ratios. Priority claims are provisional pending independent literature review.

Self-review: passed. Independent audit: not yet performed.
