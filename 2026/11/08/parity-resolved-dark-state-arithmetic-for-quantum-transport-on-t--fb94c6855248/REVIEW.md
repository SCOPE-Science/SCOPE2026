# Scientific review: parity-resolved quantum transport on theta networks

## Correctness — PASS

The exact finite-dimensional loss model is specified with adjacency hopping, two strictly positive and potentially unequal terminal rates, and three paths of at least two edges each. The proof first identifies the loss-free reducing subspace using the norm-decay identity and finite-matrix spectral stability. Restriction to each arm gives a Dirichlet sine basis. The two junction conditions separate resonant arm modes by the parity of their longitudinal indices. The mode-wise nullity then becomes the number of compatible arm pairs minus an all-compatible triple correction. This yields the claimed closed gcd formula, full-capture criterion, and localized survival projector. No extrapolation from finite simulations is used.

The reproducibility programs independently compared analytic and spectral projectors for 343 length triples and 4116 internal positions; 28 propagations with unequal loss rates gave 282 further localized checks. The normalized initial state and common onsite shift do not change the conclusion. The finite-time numerical checks corroborate, but do not establish, the all-length result.

## Originality — PASS on examined evidence, with residual priority risk

The closest general prior art is Caruso and collaborators, arXiv:0901.4454 (Appendix A.5), which describes how loss-free eigenstates arise from network degeneracies but solves a fully connected network, not the two-terminal three-path graph. Le and collaborators, arXiv:1707.07482 (section 2.1), already state the isolated-path sine spectrum and discuss dark states in paths, lattices, complete graphs and cylinders. Razzoli and collaborators, arXiv:2011.13794, study a Laplacian walk and one trap, rather than an adjacency walk with two positive-rate sinks. Their general spectral approaches and the standard sine basis are explicitly acknowledged; neither examined work states or directly implies the closed three-path gcd-parity classification without new junction-cancellation analysis.

The relevant published-record comparisons include a three-path theta-graph algebraic gnarledness result (a graph-metric invariant, not absorption), quantum-graph Robin and commensurate-resonance work (different continuum operators and boundary conditions), and specific graph transport results on other architectures. A similar result formulated in spectral graph controllability or metric-graph language cannot be categorically excluded. A failed search is not being presented as a novelty proof.

## Mathematical value — PASS

The result supplies a natural, complete, infinite-family detector-placement classification for three-corridor quantum networks. A pair of paths sharing a standing-wave denominator need not protect anything: lengths \((2,4,3)\) produce complete capture, whereas \((2,2,3)\) protect one mode. The exact two-equal-arm law produces localized survival probability \(1/2\) on those arms and zero on a coprime third arm; the three-identical-arm law gives \(2/3\). These precise, independently motivated transport probabilities and the exceptional gcd-two obstruction distinguish the result from a routine exercise about sine eigenvectors.

## Limits and priority

Nonuniform hopping, dephasing, interacting excitations, additional traps and finite-time transport are not classified. Historical priority remains provisional. The scientific contribution is the explicit arithmetic criterion and projector; the foundational dark-subspace principle and isolated-path spectrum are prior knowledge.

Self-review: passed. Independent audit: not yet performed.
