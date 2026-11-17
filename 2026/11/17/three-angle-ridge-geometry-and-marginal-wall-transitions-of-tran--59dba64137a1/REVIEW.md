# Review of the transportation-polytope ridge geometry theorem

## Correctness

**PASS.** The statement fixes the intrinsic Frobenius metric, strictly positive margins, and all cases \(m,n\ge3\), including exact threshold equalities. The proof obtains strict positive support from the fractional Hall criterion, determines pairwise facet adjacency from the possible missing neighbors of one or two rows, and excludes non-ridges by a third independent forced-zero coordinate. The projector is exactly \(P_m\otimes P_n\), giving the three claimed normal products and interior-angle signs. The balanced multiplicities and limit of the scaled mean follow by direct counting and monotonicity of \(\arcsin(t)/t\). Numerical LP and exact Gram spot checks support, but do not replace, the proof.

## Originality

**PASS, with historical-priority risk.** De Loera and Kim's 2013 survey, specifically Lemma 2.17, already establishes the single-coordinate facet criterion and the support-graph framework; Warrington's 2016 paper establishes the tangent-space orthogonal bases; Blanchard–De Loera–Louveaux 2020 concern monotone paths. None of the materially inspected texts states the combined complete two-facet marginal chamber classification with its intrinsic dihedral spectrum. These constituent methods are classical, and the earlier monograph cited for individual facets was not checked in full: an implicit or unindexed combination is a genuine residual risk. Literature search and the absence of a close exact record are not proofs of worldwide uniqueness.

## Value

**PASS.** The result gives a complete codimension-two angular invariant for a standard all-positive transportation-polytope family, including a sharp marginal-wall decision rule applicable without enumerating vertices or solving an LP per pair. It distinguishes which geometric properties are shape-only and which change under margins and identifies a \(3\times3\) exception in the central family. The strict mean/typical-angle asymptotic split makes the metric classification useful beyond mere face counts. It is an exact complete natural classification, not an arbitrary low-dimensional sample.

Self-review: passed. Independent audit: not yet performed.
