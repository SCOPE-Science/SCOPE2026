# Review of the Gray graph minimum-sensor theorem

## Correctness — PASS

The theorem's domain is the uniquely specified 54-vertex Gray incidence graph, with propagation time counting the initial domination step as round one and only simultaneous later forcing. `verify_grid.cpp` and `verify_lcf.cpp` separately enumerate all 3,162,510 five-subsets and 25,827,165 six-subsets, establish a minimum of six, and agree on the entire point/line-by-time spectrum. They independently reconstruct the full 880,632-vertex token-slide graph, its 3,412,368 edges, its degree distribution and connectedness. `verify_slowest_orbits.py` verifies the explicit LCF/isomorphism certificate and the two exhaustive maximal-delay symmetry orbits. The evidence is finite complete enumeration, not numerical sampling; no infinite-family generalization follows from it.

## Originality — PASS, with historical limits

The closest primary power-domination paper, Bjorkman et al., arXiv:2201.01798 (2022), develops the generic monitoring and reconfiguration framework but has no Gray-graph six-sensor classification. Allie et al., arXiv:2510.02211 (2025), prove general propagation-radius bounds, not the exact Gray time distribution. The highly relevant published Gray-graph efficient-open-domination result solves a distinct size-18 exact-neighbor-code problem with three- and six-element trades; it cannot imply size-six dynamic forcing placements or their one-edge slide connectivity. MathWorld/graph tables supply the geometry and 1,296 automorphisms but not the target invariants. Semantic record searches and accessible own claims showed no equivalent or dominating exact statement. An unindexed prior computation remains possible, and no negative search establishes uniqueness.

## Value — PASS

The Gray graph is the smallest cubic semisymmetric graph, so its 27 point and 27 line vertices cannot be interchanged by automorphisms. The theorem provides a complete, computationally reproducible monitoring benchmark in which optimal placement counts differ by shore, all minimum configurations remain locally reconfigurable, and propagation delays range over six distinct values. Exactly two full symmetry orbits explain the slowest placements. This is a natural exact classification of optimization, reconfiguration and latency on a canonical graph, not an unmotivated labelled-instance census.

## Scope and evidence limits

The finite computation is accompanied by two independent graph encodings and three standalone checkers. It neither proves an infinite-family formula nor determines the slide diameter or larger-cardinality monitoring distributions. An external independent proof audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
