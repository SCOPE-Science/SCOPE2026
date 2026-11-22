# Self-review: optimal strong odd colorings of \(S(K_5)\)

## Correctness — PASS

All original vertices must use different colors, as each pair shares a degree-two subdivider and a repeated neighbor color twice is not odd. This gives the five-color lower bound. A listed representative uses five colors and satisfies all neighborhoods. Once original colors are normalized to root names, each subdivider has exactly three permitted labels, with no other variables. Color classes correspond bijectively to edge-disjoint odd-degree subgraphs of the four remaining roots, of which exactly fifteen types are possible for any fixed color (empty, single edge, matching, three-star, complete four-clique). The explicitly stated exact-cover recurrence completely counts their partitions, yielding 201; its matching-only restriction yields 6. Independently enumerating every one of the 59,049 normalized assignments on the fifteen-vertex graph gives the same numbers, local profile counts and six nonoverlapping automorphism orbits. The group action is all of \(S_5\), because roots and subdividers have distinguishable degrees. There is no extrapolation from a partial finite search. Scripts and their actual outputs are attached.

## Originality — PASS, provisional historical priority

The minimum five-color value is already known from Caro et al., arXiv:2509.20763, Proposition 17(i), and is explicitly disclaimed as new. Its full relevant subsection was inspected: it gives the minimum and constructions for arbitrary \(n\), not the optimal-partition count at \(n=5\), not its separation from square colorings, and not the six symmetry orbits. Kwon--Park (arXiv:2401.11653) gives the definition and sparsity results. Caro et al. (arXiv:2410.02336) investigates planar bounds and graph products. Targeted searches of these texts, open literature, accessible earlier records, graph aliases, and the exact integers \(201,195,6,24{,}120\) did not expose a stronger theorem or tabulation covering this census. Related completely subdivided biclique colorings are distinct objects, not a reduction. Residual risks: an unindexed optimal-coloring table, graph-coloring software archive, or later publication may contain the same finite fact; the available evidence cannot certify world-wide priority.

## Value — PASS

For a canonical five-root incidence graph already known to require five colors, the central question is whether optimizing the strong odd chromatic number enforces the square-coloring constraint and how many genuinely new parity solutions remain. The answer is quantitatively and structurally nontrivial: 201 optima instead of 6, 195 not square-colorings, and six symmetry orbits. At smaller admissible equal-bound order \(n=3\), degree-two root neighborhoods force square-coloring; \(n=5\) is the first odd-order complete-subdivision case with an optimal five-color non-square family. Thus the finite count tests rigidity at the first nontrivial point of a natural graph sequence, not an arbitrary parameter slice. The exact-cover class characterization and orbit representatives make the fact reusable for parity-coloring enumeration algorithms. No all-order enumeration is claimed.

## Limits

Finite calculation is exhaustive only for \(S(K_5)\). The general chromatic-number theorem and classical total coloring are prior. Historical priority remains provisional. Independent assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
