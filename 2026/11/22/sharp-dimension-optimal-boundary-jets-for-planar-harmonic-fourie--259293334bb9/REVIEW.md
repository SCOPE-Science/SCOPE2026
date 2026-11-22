# Scientific review: sharp dimension-optimal boundary jets for planar harmonic Fourier bands

## Correctness — PASS

The statement precisely concerns all complex planar harmonic polynomials of degree at most \(L\), the complete Cartesian order-\(k\) jet at each of \(M\) equally spaced points on any positive-radius circle, and arbitrary nonnegative integers \(L,k\). The harmonic decomposition into positive/negative Fourier modes has dimension \(2L+1\). Harmonicity identifies the full local jet with value, holomorphic derivatives, and antiholomorphic derivatives, giving \(2k+1\) channels. A DFT separates residue classes and positive/negative falling-factorial Vandermonde blocks. The value row contributes exactly one additional rank under the claimed condition. This proves the exact rank formula, and the frequency-count argument proves the globally sharp node threshold. The tangential-only comparison is a separate ordinary Fourier Vandermonde argument.

The included checker independently constructs integer residue blocks and unreduced complex jet matrices and passes 10,514 assertions. It checks finite parameter ranges only; the universal assertion depends on the explicit algebraic proof. No uniform noise-stability conclusion follows from injectivity.

## Originality — PASS under stated comparisons

The May 6, 2021 full-text article by Berriochoa et al. addresses Laurent-polynomial interpolation on circle nodes, with trace derivatives and convergence, not complete two-dimensional harmonic jets or the rank formula for all bandwidths and jet orders. The 2014 full-text paper by Cachafeiro et al. similarly treats Laurent-value and first/second Laurent-derivative conditions. The relevant theorems and subsequent arbitrary-node discussion of Bojanov and Xu's full-text bivariate polynomial paper concern radial derivatives and a larger ambient polynomial space with different node numbers; they neither yield the present full-jet alias blocks nor imply the dimension-optimal \(\lceil(2L+1)/(2k+1)\rceil\) construction. General derivative interpolation on manifolds (Chandrasekaran et al., 2017) concerns approximation and existence at sufficiently high degree, not this finite Fourier exact-rank theorem.

Published research-index matches concerning harmonic-grid rank, Fock first-jet sampling and Laurent interpolation were compared by their actual observation spaces, domains, and implications, not by title alone. The existing results do not supply an implication to the claim as stated. The residual priority risk is an older or unindexed theorem about complete harmonic jets or a general Birkhoff interpolation theorem specializing directly to this rank identity. This best-knowledge novelty judgment is not a certification of historical uniqueness.

## Value — PASS

Sampling a harmonic band with complete spatial derivatives is a natural boundary-measurement problem. The theorem achieves the unavoidable information-theoretic limit for every degree and jet order, rather than merely showing generic interpolation. The exact deficiency formula covers *all* sparse grid sizes and gives an FFT-and-confluent-Vandermonde reconstruction structure. The distinction between \(2k+1\) harmonic jet channels and \(k+1\) tangential-only channels translates to a quantitative saving in sensor count; for first jets the critical site count is \(\lceil(2L+1)/3\rceil\) instead of \(L+1\) for tangential-only first-order data. This is a structural, naturally motivated result and not a small isolated computation.

## Closest literature and limits

1. Berriochoa et al., *Mechanical Models for Hermite Interpolation on the Unit Circle* (2021), DOI 10.3390/math9091043 — complete text on Laurent interpolation.
2. Cachafeiro et al., *Hermite Interpolation on the Unit Circle Considering up to the Second Derivative* (2014), DOI 10.1155/2014/808519 — Laurent derivatives through second order, not harmonic interior jets.
3. Bojanov and Xu, *On a Hermite Interpolation by Polynomials of Two Variables* (2000) — bivariate polynomial radial-derivative interpolation on concentric circles.
4. Chandrasekaran, Gorman and Mhaskar, *Minimum Sobolev Norm Interpolation of Derivative Data* (2017), arXiv:1710.01419 — background only; abstract inspected.

No claims about optimal conditioning, perturbation robustness, spatial dimensions above two, or historical uniqueness are made. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
