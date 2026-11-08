# Self-review

## Correctness

PASS. The original closed-neighborhood minority rule is conjugated to the precise dual majority rule with flips at neighbor ties. For odd \(n\), the two complementary count ranges give a constructive path to a polarized absorbing configuration. For even \(n\) with at least one undeleted matching pair, the only balanced obstruction is destroyed by firing the undeleted-index vertex; all states again have a route to a polarized absorbing configuration. At full deletion, odd degrees make cut improvement strict, and both half-shore inequalities force exact pairwise complementarity in dual coordinates. Independent direct transition-graph and local-equilibrium enumeration agree with the theorem. See `verify_transitions.py`, `verify_equilibria.py`, their output files and the proof in `RESULT.md`.

## Originality

PASS, with qualified historical priority. The closest model reference is Rouquier–Regnault–Thierry (arXiv:1011.5119), which establishes general bipartite minority duality and energy arguments, but does not present this one-edge restoration threshold or family-specific closed-class census in the inspected full text. Lampis (arXiv:2104.13097; ICALP 2021) gives a general framework for locally optimal cuts and Nash equilibria, not this named graph-family classification. Search comparisons also included stable-cut synonyms, crown graphs, matching-deleted bicliques, and relevant published graph-invariant records. The old classical central-binomial count as a sequence is not itself asserted to be new. A possibly overlooked local-Max-Cut example remains a residual priority risk.

## Value

PASS. The graph family is the natural interpolation between the biclique and its crown graph by deleting a matching. The theorem identifies a **sharp last-edge transition**: every proper deleted submatching supports only globally optimal recurrent configurations, whereas the final edge deletion creates exponentially many permanently frozen, asymptotically half-optimal configurations. This separates multiplicity of local equilibria, global optimization and the effect of tie-breaking by one microscopic edge perturbation in a dense network. The exact classification and entropy discontinuity have substantive use in anti-coordination and local-search stability comparisons beyond reproducing a numerical table.

## Scope and risks

All results use uniform single-site closed-neighborhood minority updates and tie retention. The time to absorption and basin probabilities remain unknown. General weak local optimality when some degrees are even is distinct from dynamical absorption. Historical priority is subject to unindexed equivalent statements; no claim of independent validation is made.

Self-review: passed. Independent audit: not yet performed.
