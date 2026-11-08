# Self-review: matched-channel constrained fastest mixing

## Correctness

PASS. The admissible fixed-probability and interval-constrained sets are compact and invariant under simultaneous matched-pair permutations and bipartition interchange. Averaging is feasible and cannot raise the centered spectral norm. This reduces the global problem to two off-diagonal edge types and a holding probability. The constant, bipartition-sign, pair-symmetric zero-sum, and pair-antisymmetric zero-sum spaces exhaust all \(2m\) eigenvectors, yielding a fully explicit three-mode objective. Two affine lower bounds hold for every feasible design and exactly match the two feasible formulas on opposite sides of \(2/(3m)\). The interval formula follows by minimizing the resulting V-shaped curve. The attached exact-rational test independently checks the eigenspaces and algebraic formulas; its finite sampling does not establish the universal theorem.

## Originality

PASS on inspected evidence, with qualified priority. Boyd, Diaconis and Xiao (2004, section 7.1) solve the ordinary balanced complete-bipartite problem: the unrestricted \(1/3\) optimum is known. Boyd, Diaconis, Parrilo and Xiao (2009, Theorem 3.1 and section 5.4.2) cover the edge-transitive crown endpoint and give generic symmetry reduction and the unrestricted bipartite formula. Jafarizadeh (2010, section III) solves distinct layered complete multipartite topologies. Their statements and hypotheses do not provide the closed-form fixed matched-edge-probability frontier or the two-sided capacity interval formula. Matching-deleted crown graph facts alone do not determine intermediate matched probabilities. Specialized unindexed papers and alternative capacity-constraint terminology remain risks; search absence is not certification.

## Value

PASS. Requiring or capping designated matched transitions is a natural resource constraint for a two-class communication network. The result gives the entire exact performance frontier, the universal optimally balanced matched probability, distinct slopes for under- and over-allocation, and an explicit stochastic design for any interval. The full parameter classification is more informative than a single optimal SLEM or a general SDP formulation; no unproved network-wide application or all-optimizer uniqueness is claimed.

## Limitations and references

The proof concerns symmetric stochastic chains with holding and uniform equilibrium; it does not optimize every finite-time distance or classify all nonsymmetric optimal matrices. The exact rational checker provides finite spot tests only. The primary comparisons were Boyd, Diaconis and Xiao, *SIAM Review* 46 (2004), 667–689; Boyd, Diaconis, Parrilo and Xiao, *SIAM J. Optim.* 20 (2009), 792–819; and Jafarizadeh, arXiv:1008.2588 (2010). The claimed finding has no independent audit.

Self-review: passed. Independent audit: not yet performed.
