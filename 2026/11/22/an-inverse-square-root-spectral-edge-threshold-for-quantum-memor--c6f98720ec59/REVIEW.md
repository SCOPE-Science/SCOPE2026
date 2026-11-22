# Self-review

## Correctness

**PASS.** The state is normalized for every fixed \(0\le\alpha<1\); the exact rank-one density kernel and purity reduction follow from the known uniform-memory resetting solution. The singular autocorrelation integrals have three proven regimes, including an exact antiderivative at critical exponent. The Kummer response has a width \(r/\sqrt{2\log(rt)}\), and its uniform near-zero asymptotic and Gaussian majorant justify the rescaled integral. The beta/gamma prefactors and factor \(1/8\) at the logarithmic critical edge were independently reconstructed. Finite mpmath checks corroborate kernel identities without standing in for asymptotic proof.

## Originality

**PASS, with stated search limitations.** The closest prior mathematical result proves the ordinary coefficient for bounded energy density. At and above the critical singularity, that prior hypothesis fails and its coefficient \(\int w^2\) is infinite, so it does not imply the new law. The originating quantum-memory paper furnishes the scalar response and related dynamics, but no inspected claim provides the singular-edge critical factor. Semantic searches for van Hove density, square-root edge, memory-reset purity, spectral singularities and logarithmic crossover returned the bounded-density paper as closest; searches cannot establish absence of unindexed equivalents. A relevant part of the originating full text was accessible but not every section, making independent priority checking necessary.

## Value

**PASS.** An inverse-square-root singularity is the natural one-dimensional band-edge density-of-states exponent. The critical extra \(\log\log(rt)\) and the sharp supercritical exponent determine when the bounded-density purity approximation fails, creating an exact classification of a motivated physical spectral boundary rather than an arbitrary parameter sample. No claim is made about other observables or arbitrary multi-band Hamiltonians.

## Closest literature and limitations

- G. de Mauro, M. Kulkarni and S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1 (August 3, 2026), source of the response kernel.
- *A Schatten threshold and a logarithmic purity law for quantum resetting with memory* (October 25, 2026), source of the bounded-density purity law, which has a distinct hypothesis and no finite coefficient at the singular boundary.
- DLMF §13.7 is used for the standard special-function asymptotic; it does not establish the singular spectral autocorrelation theorem.

The result is fixed-parameter, exact for the stated pure-state family and does not assert independent novelty certification. Unindexed literature remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
