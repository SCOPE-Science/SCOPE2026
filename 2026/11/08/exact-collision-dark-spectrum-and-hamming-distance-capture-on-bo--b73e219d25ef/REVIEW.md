# Self-review: Boolean-hypercube collision-dark theorem

## Correctness: PASS

The statement fixes the symmetric two-boson Hilbert space, the adjacency hopping convention, all positive on-site loss rates, the normalized site-pair input and the Hamming distance. The no-jump contraction argument proves that the only nondecaying states are Hermitian hopping eigenvectors with zero collision diagonal. The Walsh character decomposition splits each simultaneous-translation momentum into one nonzero diagonal image per distinct energy. Its ranks sum exactly to \(2^{d-1}(d+2)\), leaving \(2^{d-1}(2^d-d-1)\) protected dimensions. A normalized bright-direction projector is explicitly given, with distinct total momenta preventing hidden collisions at coincident energy.

The localized capture law is derived from complete bright-overlap sums. Its crucial Krawtchouk dual orthogonality identity is stated with correct normalization, and the binomial rearrangement is exact. The dependence on site-specific loss rates is eliminated by the positivity of the loss operator, not by assuming translation invariance of the dissipative generator. Exact modular observability-rank calculations and separately implemented orthonormal spectral-projector calculations pass for every dimension \(1\) through \(4\). The claim is for all dimensions \(d\ge2\) by proof, not by finite extrapolation. No claim is made about finite decay times, disorder or interactions.

## Originality: PASS on examined evidence, with historical-priority limits

Four relevant primary texts were inspected materially: Moore and Russell's one-particle hypercube Walsh-walk paper (arXiv:quant-ph/0104137, Section 3), Krovi and Brun's degeneracy/continuous-walk dark-state paper (arXiv:quant-ph/0606094, Section IV.C), Štefaňák et al.'s two-particle discrete line meeting problem (arXiv:0705.1985, introductory model and method), and Gamble et al.'s bosonic graph Hamiltonian paper (arXiv:1002.3003, Section II and the strongly regular graph analysis). The first provides the underlying Walsh spectrum; the second gives the general survival mechanism; the third studies finite-time coincidences for a different walk; and the fourth supplies a two-boson basis/graph Hamiltonian. None of the inspected results determines the full on-site collision-absorbing \(Q_d\) two-boson subspace or its Hamming-distance binomial-tail law.

Comparable internal mathematical claims on one-particle hypercube sinks and two-boson collision losses on cycles, stars and multipartite graphs were checked for mathematical implication. Their graph families and detector geometry do not contain the claimed two-boson hypercube family. Semantic search for exact aliases, both via the published mathematical-results index and the primary-literature web, produced no decisive equivalent or dominating result. This is evidence-limited originality, not a uniqueness certificate. A hidden or unindexed equivalent enumeration remains the main risk.

## Mathematical value: PASS

This gives an all-dimension, arbitrary-positive-loss classification for the natural two-boson collision detector on the Boolean cube, not a single sampled instance. It quantifies an exponential dark subspace, gives an exact Hamming-distance-resolved eventual capture law for *every* initially separated site pair, proves strict distance monotonicity and supplies the uniform-pair average \(d/(2^d-1)\). The dependence on collision geometry, unlike one-particle vertex absorption, is the central physical/mathematical distinction. The exact finite-system law provides a meaningful baseline against classical almost-sure meeting, even though no many-body interaction or finite-time rate is treated.

## Closest sources and residual risks

- C. Moore and A. Russell, arXiv:quant-ph/0104137, initially posted 2001-04-29; full Section 3 supplies the one-particle Walsh eigenbasis.
- H. Krovi and T. A. Brun, arXiv:quant-ph/0606094, initially posted 2006-06-10; Section IV.C describes general nonhitting invariant subspaces.
- M. Štefaňák et al., arXiv:0705.1985, initially posted 2007-05-14; coined-discrete infinite-line fixed-time meeting probabilities.
- J. K. Gamble et al., arXiv:1002.3003, initially posted 2010-02-16; two-particle Hamiltonian and SRG isomorphism setting.

Residual risks are unindexed previous two-boson hypercube collision analyses and model extensions with nonzero interactions, zero loss at some sites, time-dependent noise or finite-time observables. Scientific and access comparisons are not independent validation.

Self-review: passed. Independent audit: not yet performed.
