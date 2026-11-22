# Scientific assessment of the Heawood general-position homotopy claim

## Correctness — PASS

The claimed domain is precisely the fourteen-vertex incidence graph of the Fano plane. Its general-position complex is determined by shortest-path equality on all triples. The executable certificate independently reconstructs all 478 faces, verifies 225 legal distinct codimension-one pairs and exhaustively checks acyclicity of the **entire** 1,610-arrow Hasse orientation. Exactly one critical zero-cell, 21 one-cells and six three-cells remain; there are no critical two-cells. Discrete Morse theory gives the CW model. The six three-dimensional cells attach to a graph, for which \(\pi_2\) vanishes, proving the integral sphere wedge. Separately implemented signed modular homology calculations agree. The complete matching and all assumptions are encoded in `verify_heawood_gp.py`.

## Originality — PASS against inspected evidence

The full accessible text of Iršič–Klavžar–Rus–Tuite (2024) was inspected in its sections on basic examples, graph operations and unimodality, including references and conclusions. It defines general-position polynomials and works with particular graph classes, but gives neither a Heawood general-position complex computation nor any dominating homotopy classification. Manuel–Klavžar (2017) supplies foundational general-position work about networks and maximum sets; Ceballos–Doolittle (2023) studies different Heawood-derived cell structures. The closest published indexed descriptions of Fano cap, Heawood independence, two-independence, neighborhood, Rips and domination complexes have different admissible face conditions. The known bipartite-corona general-position homotopy theorem has degree-one leaves, which the cubic Heawood graph lacks, and does not specialize to this result. No direct covering statement was identified in the checked material; search incompleteness and unavailable full texts of some adjacent indexed records remain residual risks.

## Value — PASS

The Heawood graph is the smallest cubic graph of girth six and the point–line incidence graph of the Fano plane, a canonical benchmark rather than an arbitrary graph slice. The complete mixed-degree integral homotopy classification captures 21 fundamental circle classes and six independent three-sphere classes with no degree-two homology. A face polynomial or known maximum general-position-set size cannot determine this homotopy type or its torsion-freeness. The fact gives a concrete topological benchmark for geodesic-avoidance complexes on finite incidence geometries without asserting a general theorem beyond the graph proved.

## Limits and comparison

Independent external audit is absent. The calculation is finite but exhaustive; its proof depends on a reproducible, exact acyclic-matching certificate rather than numerical inference. A published equivalent calculation hidden from indexed retrieval remains possible. The Fano cap complex has different vertices and face constraints, and equality of a rank-six Betti number in a different degree is not coverage.

Self-review: passed. Independent audit: not yet performed.
