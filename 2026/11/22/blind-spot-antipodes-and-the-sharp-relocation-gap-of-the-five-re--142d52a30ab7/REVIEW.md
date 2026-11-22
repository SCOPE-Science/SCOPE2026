# Scientific review of the Clebsch blind-spot relocation theorem

## Correctness — PASS

The sixteen-vertex graph is specified both by a Cayley XOR model and by an isomorphic empty/singleton/pair model. Translation and five-generator permutation automorphisms reduce the power-domination classification to six explicit small representatives. Their closed-neighborhood and forcing calculations show that every minimum set is exactly an independent triple or induced path, each with an initially unobserved triple that is itself a minimum set of the opposite type. The involution follows from two representative checks. The relocation edge numbers follow from two orbit-specific degree calculations. Finite exhaustive shortest-path verification uses explicit adjacency predicates and breadth-first search on all 320 states; each program recomputes all 51,040 pair distances and the sharp 160-pair locality penalty. Both standalone scripts completed successfully from the actual package files. The claimed scope is exactly finite and all boundary cases of sizes one through three were checked.

## Originality — PASS with residual historical priority risk

The preprint arXiv:2201.01798v1 and its later complete journal text define and study general power-domination reconfiguration; their enumerated graph classes do not include the Clebsch graph or this blind-spot involution. The MathWorld and Brouwer graph references provide identification and strong regularity but do not provide power-dominating sets or their relocation distances. Other indexed Clebsch classifications concern distinct identifying, locating or metric-resolution predicates and do not imply the three-sensor power-domination result. Searches also covered folded-five-cube terminology and exact parameter/count variants. These comparisons support novelty under present evidence, but cannot exclude an unindexed or unpublished identical result.

## Value — PASS

The structural fact that the three vertices left unseen after initial observation form the unique farthest optimum under physically local rearrangement is a direct coupling between monitoring propagation and reconfiguration geometry, not a numerical census alone. The involution partitions 320 optima into 160 sharply extremal pairs; the two feasible induced-subgraph classes exhibit different slide degrees although unrestricted exchange is regular. This exact benchmark is naturally motivated by the cost of rearranging optimum sensor placements while retaining full network observability. No extrapolation to wider graph families is asserted.

## Closest sources and limitations

- Bjorkman et al., *Power domination reconfiguration*, https://arxiv.org/html/2201.01798v1 (general framework, different exact graph families); later journal version https://doi.org/10.1007/s44007-025-00187-5 .
- E. W. Weisstein, *Clebsch Graph*, https://mathworld.wolfram.com/ClebschGraph.html (graph identification and parameters only).
- Brouwer, *Clebsch graph*, https://jaanos.github.io/tables/graphs/Clebsch.html (folded cube/complement distinction).

Computations are complete for this named graph but are not a classification of power domination on all strongly regular or folded-cube graphs. The possibility of an undetected historical equivalent remains. Both checkers are same-project computational verification, not external independent audit.

Self-review: passed. Independent audit: not yet performed.
