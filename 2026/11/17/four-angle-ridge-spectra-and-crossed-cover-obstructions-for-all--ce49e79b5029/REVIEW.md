# Scientific review

## Correctness — PASS

The statement is for every finite poset on at least two elements in the standard coordinate Euclidean metric. Every facet is indexed by an augmented Hasse cover. Two such covers collapse exactly two degrees of freedom if their quotient preorder remains antisymmetric; the proof classifies all possible failures for two covers into (i) an alternate element in a two-step interval and (ii) a crossed pair of disjoint covers. The outer-normal products then give all four angle classes and the multiplicities without statistical assumptions. The standalone checker independently determines actual facet-intersection ranks from all order-preserving binary vertices for all 5,230 naturally labeled posets of sizes two through six, and compares every facet pair with the formulas; 400 seeded examples at seven and eight elements also pass. The infinite result uses the combinatorial proof, not the finite runs. Boundary conventions and the dimension-two case were checked.

## Originality — PASS, with priority limitations

Stanley's standard facet representation and Geissinger/Pegel's face-partition characterization are prior results, not contributions claimed here. In particular, Pegel's compatibility characterization gives a general decision method that could reconstruct incidences indirectly, so originality does not reside in inventing compatible partitions or in the elementary normal-inner-product identity. The new explicit assertion is that **only two named forbidden local patterns** suffice for every facet pair, together with a closed four-angle multiplicity spectrum for all standard order polytopes. The accessible full-text sections of Ahmad–Fourier–Joswig (2023), Pegel (2016), Freij-Hollanti–Lundström (2023), and Mori (2024) do not state these formulas. A previously known rooted-tree special case is subsumed, but not repeated as a new special-case finding. Semantic searches did not locate an equivalent formula; this cannot establish priority, and an implicit derivation in a prior source remains the leading risk.

## Mathematical value — PASS

The complete metric ridge classification applies to arbitrary finite posets rather than a sampled family, and turns the otherwise global compatible-partition test into local Hasse path/rectangle obstructions. The crossed-cover correction is essential: a four-element complete two-level poset already supplies a counterexample to the naive claim that all disjoint cover facets meet in ridges. The formula distinguishes whether a candidate ridge is acute, right or obtuse, provides exact multiplicities, and yields a closed calculation for complete two-level posets. These are natural codimension-two invariants in convex-polytope geometry, with direct potential for testing order/chain face-vector phenomena and metric realizations.

## Closest literature and limitations

- C. Pegel, *The Face Structure and Geometry of Marked Order Polyhedra* (arXiv:1610.01393): Theorem 3.14 and facet correspondence, a broader prior combinatorial encoding but no explicit complete Euclidean dihedral-angle spectrum located in the inspected text.
- I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets* (arXiv:2309.01626): Theorem 2.1 recalls the classical compatible-partition description; Theorem 4.1 treats face-vector comparisons in a special poset class.
- R. Freij-Hollanti, T. Lundström, *f-vector inequalities for order and chain polytopes* (arXiv:2312.13890): broader face-vector inequalities via sums, but not the metric formula.
- A. Mori, *Triangular faces of the order and chain polytope of a maximal ranked poset* (arXiv:2404.00263): triangular two-face counts, not codimension-two Euclidean dihedral classification.

The theorem does not address arbitrary affine scaling, general marked posets, or chain polytopes. Priority remains subject to further literature examination, especially the possibility of an equivalent unindexed consequence of the classical partition characterization.

Self-review: passed. Independent audit: not yet performed.
