# Review of the minimum power-domination slide classification

## Correctness — PASS

The proof starts with a precise observed/unobserved subdivision-edge criterion. A surviving cycle in the graph on unselected original vertices cannot be observed, while any forest is peeled after selected original vertices force observation of every original vertex. This yields a sharp size bound and an exhaustive two-type optimum classification, including the exceptional edge-selected singleton case on the six-cycle. Every legal slide lies between the two types, and each type-B state is the unique midpoint of a Johnson edge. The exact subdivided-Johnson distance formulas prove the stated radius, diameter, and all state eccentricities. Exhaustive bitset propagation (`check_small.py`, orders 3–7) and independently programmed set-based propagation (`check_independent.py`, orders 3–6) agreed; the second code checked the edge-bijection through order 16. A finite check is not being substituted for the infinite proof.

## Originality — PASS, with residual risk

Bong et al. (arXiv:2205.09668v1, 19 May 2022) develop general token-addition/removal theory with primary MSC 68R10, not optimal sensor slides on fully subdivided complete graphs. Bjorkman et al. (arXiv:2201.01798v1, 5 January 2022, and the open-access later version) initiate power-domination reconfiguration and leave token-sliding questions open. Their relevant sections, including the actual available full texts, were inspected. Indexed exact-object searches and a semantic mathematical-record comparison found no result that implies the same family-specific Johnson-subdivision theorem. Same-object paired- and total-domination works address different predicates. The optimizer-count numbers are also pentagonal pyramidal numbers (OEIS A002411), but an integer-sequence coincidence does not establish the present sensor/slide interpretation. Unindexed historical material and unread ancillary results in other-predicate work are residual priority risks; no absolute uniqueness is claimed.

## Mathematical value — PASS

The result is an all-order, explicit optimal-monitoring classification and a canonical reconfiguration graph, not an arbitrary finite parameter census. It identifies a structural mechanism by which link subdivision produces a bipartite sensor-mobility geometry and gives exact relocation distances; the bounded six-slide diameter contrasts with an unbounded minimum sensor budget. The forest obstruction also supplies a direct mathematical reason for the optimizer types. It offers a concrete benchmark for adjacency-constrained optimal migration without asserting an unproved general algorithm or extension.

## Limits

Only full one-step subdivisions of complete graphs and minimum-cardinality power domination are covered. No universal statement for general subdivided graphs, unrestricted jumps, or all-cardinality sets is established. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
