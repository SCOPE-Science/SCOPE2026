# Scientific assessment: integer diffusion on \(K_{2,n}\)

## Correctness — PASS

The definition fixes synchronous chip diffusion and normalizes translation by the first hub. The proof independently establishes the necessary-and-sufficient edge-sign reversal criterion for a two-cycle using an acyclic nonnegative edge energy. It then bounds each hub-to-leaf gap by \(n+1\), classifies all leaf labels relative to the two hub values into five disjoint bands, and obtains exact allowed intervals with the coupled update values \(U\) and \(V\). The multinomial formula accounts for all labelled leaves, includes ties and empty intervals, and is valid for every integer \(n\ge1\). The same argument produces the separate equal-hub formula.

The bound \(2n-2\) for the hub gap when \(n\ge3\) is proved by exhausting the cases of interior, tied and exterior leaf populations. A family with all leaves at one internal level realizes every gap of magnitude \(2,\ldots,2n-2\), and an exterior family realizes gap one. Equality forces all leaves to occupy one level, establishing uniqueness at the maximum. Pairing the fixed-point condition with the initial vertex charges proves the sole fixed configuration is constant. The assertion that *initial* periodicity has least period at most two uses the established general diffusion theorem, not finite testing.

`count_formula.py` evaluated the exact formula for \(1\le n\le10\). `direct_check.cpp` independently applied the vertex rule twice to all 9,602,861 normalized configurations in the rigorously bounded range for \(1\le n\le5\); every total and positive-gap population matched. Both code outputs are embedded. This does not constitute an infinite computational proof: the unrestricted scope is certified only by the written mathematical argument and the cited general period theorem.

## Originality — PASS with historical-priority qualification

The 2016 diffusion-game paper proves eventual periodicity for complete bipartite graphs (Theorem 2.11) and a general two-cycle edge criterion (Theorem 3.1). Its accessible full HTML text does not enumerate initially periodic translation classes of \(K_{2,n}\) or give a two-hub gap law. The 2017 general theorem proves eventual periods one or two on every finite graph; the inspected complete accessible text has no recurrent-state enumeration. Neither result logically yields the explicit five-population sum or sharp hub-gap distribution without a new family-specific count.

Nearby established recurrent-state results concern complete graphs, cycles and double stars under the same diffusion rule. Complete graphs lack the two nonadjacent-hub symmetry; double stars have leaves adjacent to one hub, not both. The four-cycle specialization \(K_{2,2}\) is covered by the known cycle census and is not represented as new. The substantive new parameter range is \(n\ge3\). Comparisons using indexed mathematical findings and exact-language searches did not identify stronger or equivalent results; the nearest indexed objects use different graph processes, often irreversible diffusion or finite-field parity automata. A failed indexed search is not a proof of novelty, and potentially unindexed prior enumerations remain possible.

## Mathematical value — PASS

Recurrent-state counts modulo uniform charge translation are natural finite invariants of integer diffusion; unlike eventual-period bounds, they measure the size and composition of the periodic part of the phase space. The infinite two-hub family \(K_{2,n}\) is the first complete bipartite family beyond stars that requires *two coupled* hub updates. The formula is a complete labelled count for every size, and the sharp range plus unique extremal state identify a geometric constraint on recurrence that the period-length theorem does not reveal. The distinct initial counts \(299,2915,36455\) for \(n=3,4,5\) make the new counts reproducible and testable. No claim is made about transient basin sizes, asymptotic growth, or fixed-mass grading.

## Closest literature and residual risks

Duffy–Lidbetter–Messinger–Nowakowski (arXiv:1609.05792, initial public version 2016-09-19), especially Sections 2.3 and 3.1; Long–Narayanan (arXiv:1704.04295, initial public version 2017-04-13), Theorem 1.1. The remaining priority risk is an unindexed enumeration for complete bipartite diffusion; specialized work outside the inspected primary texts may exist. General edge reversal, eventual period dichotomy, the known four-cycle count, and former complete-graph/double-star counts are excluded from the novelty claim.

Self-review: passed. Independent audit: not yet performed.
