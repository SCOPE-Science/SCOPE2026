# Self-review

## Correctness — PASS

The claim is for every integer \(n\ge3\), \(r\ge2\), on the power of the simple \(n\)-cycle. The decisive lemma is that a pair at underlying cycle distance at most \(2r\) has a common internal neighbour in the powered graph (when distance is at least two), and repeated midpoint forcing reaches a consecutive pair. For \(r\ge2\), that pair propagates around the entire underlying cycle. Conversely a \((2r+1)\)-packing admits no outside vertex with two selected neighbours by the triangle inequality. Cyclic gaps of length at least \(2r+1\) yield the exact \(n/k\) multiplicity formula; the empty set, singleton sets and full set are separately counted. A direct adjacency checker, independent closure simulator, and independent cyclic-composition computation corroborate the proof. The radius-one counterexample shows why the hypothesis matters.

## Originality — PASS, provisional

The relevant complete 2026 primary manuscript examines tree/ordinary-path recurrences, threshold graphs, graph-wide algorithms and complexity but does not give the cycle-power structural characterization or all-cardinality formula. The 2021 unit-interval-graph paper quotes a known stronger percolation theorem for 2-connected chordal graphs; that **covers the corresponding path-power observation**, which is therefore excluded from this claim. Theorem 3.2 does not cover nonchordal cycle powers, including \(C_6^2\). Queries using ordinary and induced convexity, distance packing, cycle powers, threshold-two bootstrap percolation, and graph polynomials revealed no covering result; this is evidence but not a uniqueness proof. Relevant indexed mathematical findings on cycle powers concern different topological complexes. An undiscovered older result or an unrecognized equivalent formulation remains a genuine historical-priority risk.

## Mathematical value — PASS

Counting \(P_3\)-convex sets was recently shown computationally hard even on restricted graphs; an entire nonchordal two-parameter graph family now has a complete characterization and closed all-cardinality polynomial. The structural reduction to cyclic packings is stronger than a numerical optimum and identifies every feasible set and the exact number of maximum proper sets. The key dynamics hinge on radius at least two; the cycle geometry and periodic gap combinatorics supply a natural, not arbitrarily selected, enumeration problem.

## Sources and remaining risks

The principal complete source inspected was the 2026 Dourado–Grippo–Lin–Protti arXiv manuscript; the 2021 González–Grippo–Safe PDF was inspected through its definitions and unit-interval/2-connected-chordal Section 3. The known 2-connected-chordal theorem and its inability to cover \(C_6^2\) are disclosed explicitly. Direct experiments only cover finite ranges, while the written proof is universal. Independent audit and comprehensive external priority certification have not been performed.

Self-review: passed. Independent audit: not yet performed.
