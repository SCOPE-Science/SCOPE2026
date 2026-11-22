# Self-review

## Correctness — PASS
The theorem has the explicit scope q>=3, m>=2 and mu>0, two nonempty probe supports and independent Rademacher signs. The three spectral projectors produce the complete Green-kernel entries and the variance identity (1) without hidden approximation. The integer-valued imbalances have parity m, and the fixed-sum extremal argument treats both |S|<=m and |S|>m, proving all equality cases, not merely constructing a good partition. The sharp positive gap for odd q follows algebraically. `verify.py` successfully passed 109166 exact-rational assertions, including exhaustive small-parameter color-count classifications and direct inverse checks. The proof, rather than the checks, justifies all dimensions and all finite positive shifts.

## Originality — PASS (provisional publication priority)
The closest primary published mathematical framework is Frommer, Rinelli and Schweitzer (2023), Theorem 3.3 and Lemma 3.5, whose fixed-partition Rademacher variance formula is acknowledged and used. Their material inspected does not solve the global q>=3 complete multipartite partition optimization. Switzer and collaborators (2021) instead examine displaced-lattice trace probing. A published complete-bipartite shifted-Laplacian optimum treats q=2, including an unequal-part transition, but does not include odd q>=3 nor the forced one-part split and its exact penalty. The detailed source/implication comparisons and actual queries are in `AUDIT.json`. The central residual risk is a differently formulated weighted multipartite MaxCut theorem; an independent publication-priority review has not been performed.

## Mathematical value — PASS
A two-solve budget cannot properly color a graph with three or more independent multipartite classes. The theorem optimizes the natural stochastic-probing variance over all imperfect two-color designs, not only over preselected graphs or symmetric guesses, and classifies every minimizer for arbitrary part count, size, and positive shift. Odd part counts always require dividing exactly one class, with a positive closed-form penalty for refusing to do so. The concrete q=3,m=2 example saves 4/37 of the best whole-part-only variance. This is a mathematical test case for fixed-cost probing; the highly symmetric family admits easier deterministic trace calculation, so no actual runtime improvement is asserted.

## Scientific limits and nearest literature
The result does not address weighted, unequal-part, correlated-probe, or more-than-two-probe designs. Previously known general stochastic-probing identities and exact complete-bipartite special cases remain prior work; potential exact weighted-MaxCut implications remain an explicit risk. No independent validation or publication-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
