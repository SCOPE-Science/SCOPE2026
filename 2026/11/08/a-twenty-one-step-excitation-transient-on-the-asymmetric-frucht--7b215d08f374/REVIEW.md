# Self-review

## Correctness: PASS

The precise 18-edge graph and ternary local update are explicitly specified. The total state space contains exactly \(3^{12}\) configurations. The proof uses exact indegree peeling of the complete functional graph, primitive-cycle traversal, and reverse topological propagation of transient lengths. An independently implemented path-memoization traversal on an LCF-labeled isomorphic graph agrees on all 74 temporal classes, primitive periods and the three sharp 21-step witnesses. Both executable programs passed from their actual packaged paths; full outputs and an independent census digest are embedded. This is exhaustive finite computation, not extrapolation or a claim about other cubic graphs.

## Originality: PASS, with residual priority risk

The closely relevant 2016 primary paper by Gravner, Lyu and Sivakoff provides a general initial-circulation characterization of synchronization and asymptotic activity on finite graphs. Its Theorem 3 and proof, inspected in the primary full text, do not enumerate the Frucht graph's seven primitive periods, their 1979 orbit multiplicities, exact 74 first-entry/period cells, or its 21-update maximizers. MathWorld and NetworkX establish that both graph descriptions represent the canonical Frucht graph; they contain no corresponding dynamics. Published mathematical-record queries and searches for equivalent terms and stronger coverage found no exact table. A separately indexed earlier or unpublished table remains a historical-priority risk; a negative search is not treated as a proof of uniqueness.

## Mathematical value: PASS

The standard asymmetric cubic Frucht graph gives a natural finite benchmark with no graph automorphism compression. Its complete excitation census reveals a maximum first-entry delay larger than its vertex count and diameter, attained by just three configurations, alongside a nontrivial mixture of seven primitive periods. These are motivated temporal invariants of a canonical graph and offer an exact comparator for finite network excitation models. The claim is not generalized beyond its proved finite scope.

## Limitations

All state-space enumeration is computer-assisted but exhaustive and reproducible. The graph and local excitation rule are fixed. This does not assert a universal upper bound, a universal transient-to-size comparison, or a historical novelty guarantee. The absence of a separate independent audit is explicit.

Self-review: passed. Independent audit: not yet performed.
