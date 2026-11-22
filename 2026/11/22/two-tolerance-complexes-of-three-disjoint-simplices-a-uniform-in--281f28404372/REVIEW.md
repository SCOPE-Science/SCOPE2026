# Scientific review: three-block two-tolerance homotopy

## Correctness — PASS

The claim concerns three pairwise disjoint **filled** simplices of arbitrary sizes at least two. Every set of vertices is assigned unambiguously by its three block counts. The proof derives both pair intersections and the triple intersection exactly. Their integral Mayer–Vietoris sequences give a primitive inclusion of the triple-intersection second homology into each pair intersection, while their first-homology incidence map is an integral signed isomorphism. Consequently, the three-set Mayer–Vietoris spectral sequence has no hidden torsion or differentials and gives free groups of the stated ranks in precisely degrees three and four. Generalized van Kampen, Hurewicz, a four-dimensional homotopy-colimit model, the low-dimensional Whitehead exact sequence and Whitehead's theorem upgrade the integral homology to the asserted **homotopy** equivalence. The proof applies to every allowed integer triple, including size-two blocks.

The finite checker exhausts all faces and the complete boundary matrices for six profiles. The first four profiles pass in characteristics two, three and five, and the other two in characteristic two. Auxiliary integer Smith forms for profiles \((2,3,3)\) and \((3,3,3)\) have exclusively unit nonzero invariants. None of the finite computations is presented as an infinite proof. Residual correctness risk is concentrated in the homotopy-colimit and integral spectral-sequence arguments, which deserve independent scrutiny.

## Originality — PASS with residual priority risk

The fully inspected relevant portions of Selvaraja (arXiv:2611.14384v1; especially Section 4, Theorem 4.2 and Corollary 4.3) provide collapsibility bounds, not this uniform two-dimensional homotopy decomposition. Kim–Lew (Combinatorica 2023; especially Theorem 1.5 and the two-disjoint-facets example) gives bounds and a two-block sphere, not a formula for arbitrary three blocks. Existing recorded work already establishes a single nine-vertex profile \((3,3,3)\), which is explicitly excluded from the novelty claim. Other nearby one-tolerance, strictly one-dimensional input, and two-block results concern different simplicial complexes or parameters. Published mathematical-index comparisons were run for generic and exact formulations; none yielded a dominating all-size theorem. Indexing and visibility are imperfect, so independent publication-priority verification remains outstanding. The substantive new assertion is the all-size integral homotopy classification, not any isolated previously known profile.

## Mathematical value — PASS

This is a complete infinite three-parameter homotopy classification in a natural family of tolerance complexes of chordal clique graphs. It computes the full integral homotopy type, rather than only Euler characteristic, homological dimension or field-dependent bounds. It identifies a sharp structural transition between a single homology degree and two degrees and makes the Leray upper bound sharp for all triples with two blocks of size at least three. The primitive integral comparison is necessary to exclude torsion. The \((2,3,m)\) family gives an explicit unbounded mixed-dimensional witness. No unrelated downstream application is assumed or claimed.

## Scope and residual risks

The result does not classify all tolerance complexes, and the proof has not been independently reviewed. An equivalent all-size classification could exist in literature not indexed or accessible during this comparison. The finite checker cannot rule out errors in the general spectral-sequence reasoning.

Self-review: passed. Independent audit: not yet performed.
