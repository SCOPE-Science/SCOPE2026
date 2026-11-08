# Review: sharp fixed-mean clocked-qubit purity classification

## Correctness — PASS

For the exactly specified equilibrium-renewal interpretation, \(\Pr(A=a)=\Pr(L>a)/\mu\) and the finite geometric sum give \(z=(1-\mathbb E[i^L])/[\mu(1-i)]\), so purity is \(1/2+|1-\mathbb E i^L|^2/(4\mu^2)\). The two explicit pointwise support inequalities provide dual lower certificates with equality only on \(\{1,3\}\) and \(\{1,3,4\}\), and the fourth-root-of-unity triangle bounds give the upper certificates. Strict equality cases and the remaining residue-class optimizers follow from the same inequalities. The convexity of the fixed-mean probability-law set and continuity of purity prove interval completion. The companion standard-library checker uses exact rational arithmetic for 69,251 diagnostic assertions; these finite tests support but do not prove the universally quantified theorem.

## Originality — PASS, qualified

Wald, Yao, Platini, Hooley and Carollo, *Stochastic resetting in discrete-time quantum dynamics* (arXiv:2410.11497, first posted 2024-10-15), develop the discrete-time framework, geometric resetting, resonances and non-Poissonian convergence. Their full accessible article, including its non-Poissonian section and appendices, does not supply a prescribed-average-interval stationary-purity range, its three thresholds or an optimizer classification for the quarter-turn gate. Sevilla and Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting* (arXiv:2209.05643, first posted 2022-09-12), derive general continuous-time renewal density and purity formulas. Because intervals are not restricted to positive integer ticks there, a continuous-time envelope does not imply the exact discrete-lattice sharp lower floor and equality cases. The same distinction applies to related continuous-time fixed-mean purity classifications. No queried relevant research record or targeted published-literature search produced a statement implying the whole claimed theorem. Searches are not a proof of priority: specialized unindexed lattice-moment optimization or renewal analyses remain a material risk.

## Value — PASS

A quarter-turn Clifford gate is a canonical physically motivated discrete phase clock. At an unchanged expected reset budget, the complete interval answers which steady ensemble purities are attainable, which schedules are extremal, and when dephasing is exactly possible. The optimizer structures change sharply at three distinct mean intervals, which exposes integer-tick physics not captured by allowing arbitrary real reset durations. This is a structural classification, not merely a benchmark value. The narrow ideal-gate scope and equilibrium-renewal initialization are essential limitations, and no hardware robustness is proved.

## Closest literature and remaining limitations

- Wald et al., arXiv:2410.11497, full accessible article sections 2–4 and appendices: necessary discrete-time resetting context but not this fixed-budget classification.
- Sevilla and Valdés-Hernández, arXiv:2209.05643, full accessible preprint: general continuous-time formulas; reset support and therefore extremal feasible sets differ.
- The general moment-problem convexity machinery may imply a version of the result not identified in the targeted search. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
