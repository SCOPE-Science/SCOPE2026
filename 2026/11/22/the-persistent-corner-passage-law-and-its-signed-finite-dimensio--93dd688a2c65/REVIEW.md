# Self-review

## Correctness — PASS

The claimed chain is stationary on the uniform binary cube, with independent coordinate flips of probability \(a/d\) for fixed \(a>0\) and \(d>2a\). From the corner, the exact return probability is \(u_d(k)=((1+(1-2a/d)^k)/2)^d\). The stationarity/first-entrance renewal identity gives the exact mean and the Laplace transform of passage. A binomial central-concentration argument evaluates the limiting return Green function, and a fourth-order Taylor expansion with exponentially small tails gives the signed \(1/d\) coefficient. The conditional uninterrupted corner-run length is geometric. A pure-Python checker corroborates the finite identities for dimensions 1 through 7 (with admissible rational flip rates) and tests the asymptotic coefficient; 225 assertions passed. Tests do not prove the infinite-dimensional claims, which follow from the written argument.

## Originality — PASS against inspected evidence

Tanzi–Tenaglia, *Stability of quasi-stationary measures in high-dimensional products of mixing Markov chains* (arXiv:2609.10178, 2026, Hypothesis 1 and Theorems 2.1–2.2), assumes a fixed underlying chain with contraction bounded away from one. The present one-bit contraction \(1-2a/d\) tends to one. Their quasi-stationary density theorems do not entail this exact stationary-corner first passage formula or its finite-size coefficient. Černý–Gayrard, *Hitting time of large subsets of the hypercube* (arXiv:math/0611242, 2006, Theorems 1.1–1.3), studies the single-coordinate-at-a-time simple walk and target families; its point-hitting references are classical background, not the synchronous independent-flip result. Nestoridi, *A non-local random walk on the hypercube* (arXiv:1507.05690, 2015), flips a fixed number of chosen coordinates and establishes mixing bounds. Peixoto–Marcondes, *Stopping Times of Random Walks on a Hypercube* (arXiv:1709.02359, 2017), establishes hitting/return laws for the nearest-neighbor and lazy one-coordinate walks, not independent simultaneous flips. Related publicly indexed findings on cube walks concern resets, mixing, and coordinate exploration rather than the stated stationary corner Green-function asymptotics. We found no statement or stronger theorem covering the signed \(1/d\) correction. This absence is not proof of historical uniqueness: Kemperman's 1961 stationary-passage monograph was not inspected in full, and a specialized theorem may exist in broader rare-event theory.

## Value — PASS

A fixed-corner target has stationary mass \(2^{-d}\), yet the first-entry rate on that natural scale is \(1-e^{-a}\), not one: short return clusters change the macroscopic clock. The signed coefficient \(a^2e^{-a}(3e^{-a}-1)/[2(1-e^{-a})^3]\) locates a natural \(a=\log3\) approach-direction boundary and supplies a quantitative finite-dimension correction for calibrating rare passage in slowly mixing coordinate products. This is a motivated stochastic boundary effect, rather than an arbitrary numerical slice. It does not assert uniformity near the crossover or a full Poisson-cluster process.

## Closest literature and limitations

The exact return/renewal identity is classical and not itself claimed to be new. The two main relevant differences are the vanishing one-coordinate spectral gap and the precise finite-dimensional signed correction. A fixed \(a>0\), stationary start and one corner are necessary. The closest historical point-hitting theory may deserve independent priority review.

Self-review: passed. Independent audit: not yet performed.
