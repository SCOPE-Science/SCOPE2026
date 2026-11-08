# Scientific review

## Correctness
PASS. The normal is represented by a mean-centered isotropic Gaussian on the zero-sum subspace; the projection volume uses the exact formula of Pandis (arXiv:2601.18436, Theorem 1.2). The section's face counts follow from crossing vertex subsets. Expansion of normalized Gaussian absolute deviations gives the even influence function \(U\), while the centered sign count has odd influence function \(W\); the standard Gaussian moments yield variances \(1-3/\pi\) and \(1-2/\pi\), and zero cross-covariance. A bivariate CLT gives independent Gaussian limits. Fixed-degree binomial-polynomial expansion yields the joint chi-square face deficits. Explicit spherical and bivariate-Gaussian calculations give finite shadow moments. The supplementary verifier passed 387 checks; numerical checks are not treated as proof.

## Originality
PASS, with residual historical priority risk. Pandis's paper establishes the projection identity and extrema but not this joint law. Earlier central simplex-section results establish face-count marginals but do not address the shadow of the same oriented hyperplane. Prochno–Thäle–Tuchel's arXiv:2412.16054 Theorem A is for a fixed-dimensional random subspace of an \(\ell_p\)-ball; Baci et al. arXiv:2005.04911 use uniformly sampled simplex points, not Haar normals. Searches for an equivalent joint projection/section fluctuation theorem did not identify one. The result requires a joint influence-function argument not supplied by any one of these references; absence from searches is not a general proof of novelty.

## Value
PASS. The same random direction governs both orthogonal shadow volume and central section face complexity, so asymptotic independence is not automatic from either known marginal law. The result identifies two different fluctuation scales and laws (Gaussian versus common chi-square) and their explicit variances; the exact finite shadow moments give calibrations for stochastic geometric simulations and connect extremal projection formulas with random combinatorial sections. No arbitrary parameter slice is introduced.

## Closest literature and limits
Pandis (2026) provides the critical shadow identity. Known central-section Gaussian-sign-imbalance formulas provide the section marginal. Fixed-rank \(\ell_p\)-ball projection CLTs do not subsume this codimension-one simplex regime. An unindexed equivalent identity or an unpublished comparison remains possible; independent priority review is recommended. Fixed-rank limits only, and no Berry–Esseen rate is asserted.

Self-review: passed. Independent audit: not yet performed.
