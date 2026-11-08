# Scientific assessment

## Correctness — PASS

The theorem has two linked components: an exact activity-rate distribution on finite cactus graphs and an asymptotic two-rate saturation law for equal-length cycle bouquets. For the first, the finite-graph circulation theorem [1, Theorem 3] gives each individual trajectory's rate. A direct three-color flow-conservation identity gives the exact CCA/GHM factor three. A cactus has no simple cycles besides its blocks, and its block-edge sets are disjoint. The root-color plus modular edge-increment construction establishes a bijection rather than merely a heuristic independence assertion. Consequently its exact count has no missing cut-vertex corrections. For the second component, near-endpoint trinomial coefficients satisfy the displayed exact binomial sum, making the event probability and Poisson parameter explicit. The second-highest winding has expected occurrence tending to infinity and completes the claimed two-point limit. Complete state-space simulations of nine small cactus graphs, in both models, agree with the exact counts. The verification code was executed after extracting the final embedded files.

## Originality — PASS, with explicit dependence on known results

Gravner–Lyu–Sivakoff [1, Theorem 3] already prove the pointwise maximum-cycle-circulation formula for any finite graph, and Doba [2, Section 7] already gives the GHM maximum-cycle-density rule. Neither pointwise result supplies a complete population distribution over the initial colorings of arbitrary connected cactus graphs or the critical two-rate Poisson window in a growing bouquet. The 1995 infinite-lattice GHM study [3] does not give these graph-family counts. Searches for cactus cycle-winding distributions, finite-graph GHM rate populations, and rare maximal bouquet activity did not identify a covering paper. A prior unpublished or differently described modular-flow enumeration remains a priority risk; the novelty claim is restricted to the counting distribution and its arithmetic saturation window.

## Mathematical value — PASS

Rate distributions are natural observables in excitable-network dynamics when the initial coloring is random. The cactus class is broad enough to include articulation sharing, bridge attachments, chains of cycles and bouquets, yet admits a complete exact enumeration. The especially distinctive feature is a sharp arithmetic trichotomy in the number of cycles required to attain maximal excitation. At its critical exponential scale, global activity concentrates on exactly the highest and second-highest rates with nondegenerate Poisson weights. This is more informative than applying the known pointwise criterion to one configuration and provides a nontrivial finite-to-large-network transition. It does not claim a new generic extreme-value theorem.

## Closest literature and scope

[1] J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, Theorem 3 and the random-unicyclic discussion.

[2] N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), Section 7.

[3] R. Fisch, J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), introduction and model statements.

The result does not establish precise transient times or periodic orbit lengths. Exhaustive verification is finite and cannot replace the proof's infinite parameter argument. Absolute historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
