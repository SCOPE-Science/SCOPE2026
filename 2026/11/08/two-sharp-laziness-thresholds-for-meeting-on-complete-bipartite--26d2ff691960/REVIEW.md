# Scientific review: bipartite synchronous meeting-time phase diagram

## Correctness

**PASS.** The full three-class transient matrix is obtained by independent-step probability counting, including the meeting probabilities discarded from each row. For \(p\in(0,1)\), absorption occurs with finite mean, so first-step equations have a unique solution. Algebraic elimination gives explicit rational class means; subtracting them yields a common positive denominator and two strictly increasing quadratic sign polynomials. Values at \(p=1/3\), \(p=1/2\), and \(r=(5-\sqrt{17})/4\) prove each phase interval and uniqueness. Degenerate star and balanced cases are handled separately. The independently constructed full ordered-position product-chain computation, reduced only by exchange of the two walkers and not by bipartition class, passed 31,129 exact assertions. The general theorem follows from algebra, not the finite check.

## Originality

**PASS, with historical-priority risk.** Alpern–Zeng (arXiv:2111.05958, Sections 2, 4.2 and 5.1) use the same independent lazy-walk gathering setup on cycles, lines, and grids, not the exact two-threshold bipartite initial-geometry phase diagram. Oliveira–Peres (arXiv:1807.06858) provide general meeting and coalescence bounds, not the class-ordering identities. Sakumoto–Ohsaki (arXiv:2005.11161) offer broad spectral/approximation calculations but explicitly assume a nonbipartite graph in their spectral setup and do not derive the biclique thresholds. Eguchi et al. (arXiv:2305.11590) have only one agent scheduled to move per step, a different process. Other directed random-graph meeting results are asymptotic, not finite exact. Scientific-query searches of the relevant published-result index and the existing research titles found no statement or stronger result implying the sharp crossings. This is best-knowledge assessment, not a universal priority proof. The related Warwick Zeng thesis (2023) was only accessible through indexed excerpts; its complete text could not be checked, which is a named residual risk.

## Value

**PASS.** The mean rendezvous delay of independently walking agents depends on initialization even on symmetric networks. The theorem gives a complete, exact and all-order classification of *every* distinct initial placement on the natural bipartite family and identifies a universal balancing probability where the entire initial-state dependence vanishes. For unbalanced graphs, the optimal and worst-case starting placements switch at separate sharp parameters, with explicit universal extremal bounds and asymptotics. This resolves a motivated finite-state stochastic-ordering boundary at the level of expected first meetings, not just a numerical example.

## Limits and closest literature

The theorem concerns common laziness, synchronous discrete steps, vertex-only meeting, and expectations; it does not characterize optimal choice of laziness or meeting-time stochastic dominance. The central related paper is Alpern–Zeng (2021), which treats the same motion mechanism on other graph families and a different extremal question. The possible broader thesis coverage remains unverified. No independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
