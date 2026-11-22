# Review of the one-descent permutation swap-graph classification

## Correctness — PASS

The unique-descent, two-increasing-block representation is exact, including boundary indices. Only three swaps near the descent can be legal. The two outside swaps are characterized by exact cross-block inequalities; the central swap is legal when exactly one of the two neighboring comparisons reverses, including two endpoint-only cases. Both outside inequalities and the endpoint cases force the same two explicit path templates. Each path edge is exhibited, its other incident edges are ruled out, and distinct paths are separated by the invariant inverse-descent position for consecutive values. Eulerian counting supplies the isolated-vertex multiplicity. The embedded standalone enumeration checks all proposed graph edges and components through length nine, and all within-component pair distances through length eight. Finite checks complement, not replace, the proof.

## Originality — PASS with historical-priority risk

The closest directly inspected 2023 source, Ito–Yamanaka–Hirayama–Kobayashi, addresses all linear extensions of a fixed poset, which form a connected adjacent-transposition graph; it does not imply the disconnected Eulerian level-set geometry. Mütze's 2023 survey gives the broader Gray-code context. Smith's 2014/2016 fixed-descent permutation work uses the unrelated pattern-containment order. Published neighboring permutation reconfiguration families constrain derangements, fixed points or pattern avoidance rather than one-descent levels. OEIS A324172 already records the same scalar formula for another combinatorial class, so the scalar sequence is explicitly **not** claimed as new: the complete swap-graph decomposition and exact reachability are the distinct contributions. No relevant accessible source established an equivalent statement; an unindexed equivalent remains a risk.

## Value — PASS

The statement classifies a natural Eulerian stratum under the smallest possible permutation edit. It gives not merely counts but every component, every shortest reachable route, all degree classes, and the exponential scarcity of mobile states. This proves that the obvious adjacent-swap Markov chain cannot mix on fixed-one-descent permutations—a substantive feasibility boundary for constrained permutation generation and sampling.

## Scope and limitations

The claim does not apply to fixed descent position, two or more descents, nonadjacent swaps, or altered feasibility rules. The global graph is disconnected. The historical-priority judgment is best-knowledge and not an independent scholarly audit. No external formal proof certification is asserted.

Self-review: passed. Independent audit: not yet performed.
